from django.db import models
import datetime as dt
from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        location = Location.objects.get(pk = id)
        return location

class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category
class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    # Image = models.ImageField(upload_to='photos/') 
    image = CloudinaryField('image')
    Image_location = models.ForeignKey('Location', on_delete=models.CASCADE)
    Image_category = models.ForeignKey('Category', on_delete=models.CASCADE)

    

    class Meta:
        ordering = ['name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    
    @classmethod
    def update_image(cls, id ,name, description , Image_location, Image_category):
        update = cls.objects.filter(id = id).update(name = name, description = description ,Image_location = Image_location,Image_category = Image_category)
        
    #return update
    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images
    @classmethod
    def get_image_by_id(cls, id):
        images = Image.objects.filter(id=id).all()
        return images
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(Image_category__name__icontains=search_term)
        return images
    @classmethod
    def filter_by_location(cls, Image_location):

        images_location = cls.objects.filter(Image_location__id=Image_location)
        return images_location
         
    def __str__(self):

        return self.name

