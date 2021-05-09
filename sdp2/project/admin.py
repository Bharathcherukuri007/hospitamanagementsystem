from django.contrib import admin

# Register your models here.
from .models import User, Appointment, Prescription, DoctorAdvice

admin.site.register(User)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(DoctorAdvice)
