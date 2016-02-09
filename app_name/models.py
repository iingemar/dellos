from django.db import models


class Ingredient(models.Model):
    index = models.IntegerField(null=True, blank=True, default=0)
    name = models.CharField(max_length=300, null=True, blank=True)

    def __unicode__(self):
        return self.name


class FoodCategory(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Food(models.Model):
    index = models.IntegerField(null=True, blank=True, default=0)
    name = models.CharField(max_length=300, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, null=True, blank=True)
    comment = models.CharField(max_length=300, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True, default=0)
    category = models.ForeignKey(FoodCategory, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_ingredients(self):
        return ' / '.join(i.name for i in self.ingredients.all())