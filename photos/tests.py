from django.test import TestCase
from photos.models import Image,Location,Category


# Create your tests here.

class ImageTestClass(TestCase):
    #setup method
    def setUp(self):
        self.myImage=Image(image = 'image', name = 'Nature', description='Nature is beautiful')

    #Test instance