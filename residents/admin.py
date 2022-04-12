from django.contrib import admin
from .models import (Region, Location, House, Own, IndividualResident,
    EntityResident, Organization, BaseResidentRel,)

# Register your models here.
admin.site.register(Region)
admin.site.register(Location)
admin.site.register(House)
admin.site.register(Own)
admin.site.register(IndividualResident)
admin.site.register(EntityResident)
admin.site.register(Organization)
admin.site.register(BaseResidentRel)
