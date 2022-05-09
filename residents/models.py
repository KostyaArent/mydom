from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MaxValueValidator
from random import randint


class BaseLocation(models.Model):
    """Абстрактная базовая модель локации.
    :param title: название
    :type title: CharField
    """
    title = models.CharField(max_length=20, unique=True)


class Region(BaseLocation):
    code = models.IntegerField(unique=True, validators=[MaxValueValidator(999)])

    def __str__(self):
        return self.title


class Location(BaseLocation):
    TYPES = (
    ('district', 'Район'),
    ('town', 'Город'),
    ('street', 'Улица'),
    )
    type = models.CharField(max_length=300, choices = TYPES)

    def __str__(self):
        return self.title


class House(models.Model):
    """Модель Здания.
    :param number: Номер здания
    :type number: CharField
    :param region: Экземпляр класса Region
    :type region: ForeignKey
    :param district: Экземпляр класса District
    :type district: ForeignKey
    :param town: Экземпляр класса Town
    :type town: ForeignKey
    :param street: Экземпляр класса Street
    :type street: ForeignKey
    """
    number = models.CharField(max_length=20, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(Location, related_name='Район', on_delete=models.CASCADE, limit_choices_to={'type': 'district'})
    town = models.ForeignKey(Location, related_name='Город', on_delete=models.CASCADE, limit_choices_to={'type': 'town'})
    street = models.ForeignKey(Location, related_name='Улица', on_delete=models.CASCADE, limit_choices_to={'type': 'street'})

    def __str__(self):
        return f'{self.region}, {self.town}, {self.street}, {self.number}'


class User(AbstractUser):
    is_personnel = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)


class BaseResident(models.Model):
    address = models.ForeignKey(House, models.SET_NULL, null=True)
    is_confirmed = models.BooleanField(default=False)

    class Meta:
        abstract = True

class IndividualResident(models.Model):
    """Модель собственника физического лица.
    :param user: Экземпляр класса User
    :type user: ForeignKey
    :param own: Экземпляры класса Own
    :type own: ManyToManyField
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class EntityResident(models.Model):
    """Модель собственника юридического лица.
    :param title: краткое наименование юр.лица
    :type title: CharField
    :param full_title: полное наименование юр.лица
    :type full_title: CharField
    :param kpp: КПП
    :type kpp: CharField
    :param staff: Экземпляры класса User
    :type staff: ManyToManyField
    """
    title = models.CharField(default=0, max_length=50)
    full_title = models.CharField(default=0, max_length=100)
    itn = models.CharField(default=0, max_length=20)
    kpp = models.CharField(default=0, max_length=20)
    staff = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title


class BaseResidentRel(models.Model):
    entity_resident = models.ForeignKey(EntityResident, models.SET_NULL, blank=True, null=True, related_name='mtm')
    individual_resident = models.ForeignKey(IndividualResident, models.SET_NULL, blank=True, null=True, related_name='mtm')

    def __str__(self):
        if self.entity_resident is not None:
            return self.entity_resident.title
        elif self.individual_resident is not None:
            return self.individual_resident.user.username


class Own(models.Model):
    """Модель Помещения собственности.
    :param number: Номер помещения
    :type number: CharField
    :param house: Экземпляр класса House
    :type house: ForeignKey
    :param owners: Экземпляры класса BaseResident
    :type owners: ManyToManyField
    :param is_living: статус жилого помещения
    :type is_living: BooleanField
    """
    number = models.CharField(max_length=20, unique=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    owners = models.ManyToManyField(BaseResidentRel)
    is_living = models.BooleanField()

    def __str__(self):
        return f'{self.house}, {self.number}'


class Organization(BaseResident):
    """Модель обслуживающей организации.
    :param title: краткое наименование юр.лица
    :type title: CharField
    :param full_title: полное наименование юр.лица
    :type full_title: CharField
    :param kpp: КПП
    :type kpp: CharField
    :param staff: Экземпляры класса User
    :type staff: ManyToManyField
    """
    title = models.CharField(default=0, max_length=50)
    full_title = models.CharField(default=0, max_length=100)
    kpp = models.CharField(default=0, max_length=20)
    staff = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Code2FA(models.Model):
    code = models.IntegerField(default=1234)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Stage(models.Model):
    title = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.title


class Appeal(models.Model):
    CATEGORIES = (
        ('cleaning', 'Уборка'),
        ('water', 'Водоснабжение'),
        ('houseside', 'Придомовая территория'),
        )
    status = models.ForeignKey(Stage, on_delete=models.CASCADE)
    category = models.CharField(max_length=300, choices = CATEGORIES)
    owner = models.ForeignKey(BaseResidentRel, on_delete=models.CASCADE)
    address = models.ForeignKey(Own, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()
    responsible = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.pk)


class AppealPicture(models.Model):
    image = models.ImageField(upload_to='media/appeal/')
    appeal = models.ForeignKey(Appeal, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
