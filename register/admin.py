from django.contrib import admin
from .models import Applicant, Formsubmited, Documents

# Register your models here.
admin.site.register(Applicant)

admin.site.register(Formsubmited)

admin.site.register(Documents)