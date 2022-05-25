from django.contrib import admin
from .models import duck
# Register your models here.



class AdminSnack(admin.ModelAdmin):
    list_display = ('title', 'price', 'purchaser', 'timestamp', 'updated')
  

admin.site.register(duck, AdminSnack)