from django.contrib import admin
from models import Ingredient, Food, FoodCategory


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('index', 'name')
    list_display_links = ('name',)
    list_editable = ('index',)
    search_fields = ['name']


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('index', 'category', 'name', 'get_ingredients', 'price')
    list_display_links = ('name',)
    list_editable = ('index',)
    search_fields = ['name']


admin.site.register(Food, FoodAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)