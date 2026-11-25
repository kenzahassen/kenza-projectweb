from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdminPers(admin.ModelAdmin):
    fieldsets = (
        ("Description", {
            "fields": ("reason", "status", "prescription"),
        }),
        ("Date + Duration", {
            "fields": ("appointment_date", "duration_minutes"),
        }),
        ("Patients/Doctors", {
            "fields": ("doctor", "patient"),
        }),
        ("Planification", {
            "fields": ("created_at", "updated_at"),
        }),
    )
    readonly_fields = ("created_at", "updated_at")