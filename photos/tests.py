from django.test import TestCase
from photos.models import Image,Location,category


# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.nairobi= Location(name = 'Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

     # Testing Save Method for locations
    def test_save_location(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)


# class ImageTestClass(TestCase):
#     #setup method
#     def setUp(self):
#         self.myImage=Image(image = 'image', name = 'Nature', description='Nature is beautiful')

#     #Test instance