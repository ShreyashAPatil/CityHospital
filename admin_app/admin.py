from django.contrib import admin

# Register your models here.
from . models import *



admin.site.register(Doctor)
admin.site.register(Speciality)

admin.site.register(Shift)

admin.site.register(Nurse)
admin.site.register(Gender)
admin.site.register(Room_Service)