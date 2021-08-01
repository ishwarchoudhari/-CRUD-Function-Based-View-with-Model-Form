from django.contrib import admin
from .models import User


# Register your models here.
# Registering models here including id by creating a class and using decorators
# then Create a superUser to check them in admin pannel
@admin.register( User )
class UserAdmin( admin.ModelAdmin ):
    list_display = ('id','name','email','contact')
