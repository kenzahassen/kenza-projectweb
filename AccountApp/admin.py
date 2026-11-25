from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Doctor, Patient, Speciality

admin.site.register(User, UserAdmin)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Speciality)