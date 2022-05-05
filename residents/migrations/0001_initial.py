# Generated by Django 3.2.12 on 2022-04-13 23:10

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_personnel', models.BooleanField(default=False)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaseLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BaseResidentRel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('baselocation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='residents.baselocation')),
                ('type', models.CharField(choices=[('district', 'Район'), ('town', 'Город'), ('street', 'Улица')], max_length=300)),
            ],
            bases=('residents.baselocation',),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('baselocation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='residents.baselocation')),
                ('code', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(999)])),
            ],
            bases=('residents.baselocation',),
        ),
        migrations.CreateModel(
            name='Own',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True)),
                ('is_living', models.BooleanField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residents.house')),
                ('owners', models.ManyToManyField(to='residents.BaseResidentRel')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('title', models.CharField(default=0, max_length=50)),
                ('full_title', models.CharField(default=0, max_length=100)),
                ('kpp', models.CharField(default=0, max_length=20)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='residents.house')),
                ('staff', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndividualResident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EntityResident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=0, max_length=50)),
                ('full_title', models.CharField(default=0, max_length=100)),
                ('itn', models.CharField(default=0, max_length=20)),
                ('kpp', models.CharField(default=0, max_length=20)),
                ('staff', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='baseresidentrel',
            name='entity_resident',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtm', to='residents.entityresident'),
        ),
        migrations.AddField(
            model_name='baseresidentrel',
            name='individual_resident',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtm', to='residents.individualresident'),
        ),
        migrations.AddField(
            model_name='house',
            name='district',
            field=models.ForeignKey(limit_choices_to={'type': 'district'}, on_delete=django.db.models.deletion.CASCADE, related_name='Район', to='residents.location'),
        ),
        migrations.AddField(
            model_name='house',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residents.region'),
        ),
        migrations.AddField(
            model_name='house',
            name='street',
            field=models.ForeignKey(limit_choices_to={'type': 'street'}, on_delete=django.db.models.deletion.CASCADE, related_name='Улица', to='residents.location'),
        ),
        migrations.AddField(
            model_name='house',
            name='town',
            field=models.ForeignKey(limit_choices_to={'type': 'town'}, on_delete=django.db.models.deletion.CASCADE, related_name='Город', to='residents.location'),
        ),
    ]