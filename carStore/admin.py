from django.contrib import admin
from carStore.models import Brand, Car

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'deleted_at')
    
    search_fields = ('name',) 

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'factory_year', 'model_year', 'color', 'owner', 'photo', 'created_at')
    
    list_filter = ('brand', 'factory_year', 'model_year')
    search_fields = ('model', 'owner')

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)