from django.contrib import admin
from users.models.custom_user_model import CustomUser

# Register your models here.

admin.site.register(CustomUser)
