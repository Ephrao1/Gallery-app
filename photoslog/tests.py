from django.test import TestCase
from .models import Location,Category,Image


# Create your tests here.
class LocationTestClass(TestCase):
    #Setup Method
    def setUp(self):
        self.loc = Location(name="America")
        self.loc.save_location()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.loc,Location))
    
    def test_save_method(self):
        self.loc.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
    
    def test_delete_method(self):
        self.loc.save_location()
        self.loc.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update(self):
        location = Location.get_location_id(self.loc.id)
        location.update_location('Nairobi')
        location  = Location.get_location_id(self.loc.id)
        self.assertTrue(location.name == 'Nairobi')

class CategoryTestClass(TestCase):
    #setup Method
    def setUp(self):
        self.teflon = Category(name="designs")
        self.teflon.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.teflon, Category))

    def test_save_method(self):
        self.teflon.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.teflon.save_category()
        self.teflon.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update(self):
        category = Category.get_category_id(self.teflon.id)
        category.update_category('Fashion')
        category = Category.get_category_id(self.teflon.id)
        self.assertTrue(category.name == 'Fashion')

class ImageTestClass(TestCase):
    #set up Method
    def setUp(self):
        self.loc = Location(name='America')
        self.loc.save_location()

        self.teflon = Category(name='designs')
        self.teflon.save_category()

        self.image = Image(name='image test', description='reagan test', Image_location=self.loc, Image_category=self.teflon)
        self.image.save_image()
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))


    def test_update_image(self):
        self.image.save_image()
        image = Image.update_image( self.image.id, 'test update', 'my test',self.loc, self.teflon)
        upimage = Image.objects.filter(id = self.image.id)
        print(upimage)
        self.assertTrue(len(upimage) > 0)    

    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images) > 0)
    
    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images) == 1)

    def test_search_by_category(self):
        found_img = self.image.search_by_category(self.teflon)
        image = Image.objects.all()
        self.assertTrue(found_img, image)

    def test_filter_by_location(self):
        images = Image.filter_by_location('1')
        print(images)
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        self.image.delete_image()
        self.teflon.delete_category()
        self.loc.delete_location()
        

       
