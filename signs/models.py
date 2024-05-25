from django.db import models

# Create your models here.


class CategorySigns(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category_signs'

    def __str__(self):
        return self.name


class RoadSigns(models.Model):

    name = models.CharField(max_length=100)
    category = models.ForeignKey(CategorySigns, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.FileField(upload_to='video', blank=True, null=True)
    doc = models.FileField(upload_to='doc', blank=True, null=True)
    audio = models.FileField(upload_to='audio', blank=True, null=True)



    class Meta :
        db_table = 'road_signs'

    def __str__(self):
        return f"{self.category.name} | {self.name}"

