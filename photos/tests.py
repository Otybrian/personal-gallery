from django.test import TestCase
from .models import Editor,Image,category, location
# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.brian= Editor(first_name = 'Brian', last_name ='Otieno', email ='brian@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.brian,Editor))

     # Testing Save Method
    def test_save_method(self):
        self.brian.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ImageTestClass(TestCase):
       # Set up method
    def setUp(self):
        #creating a new editor and saving
        self.brian= Editor(first_name = 'Brian', last_name ='Otieno', email ='brian@moringaschool.com')
        self.brian.save_editor()

        #creating a new category
        self.nature = category(name = 'mytest')
        self.nature.save()

        #creating a new location
        self.nairobi = location(name = 'mytest')
        self.nairobi.save()

        #creating a new image and saving
        self.new_image = Image(name = 'flower', description = 'beautiful', link = 'brian.com', editor = self.brian)
        self.new_image.save()
        self.new_image.category.add(self.nature)
        self.new_image.location.add(self.nairobi)


    def tearDown(self):
        Editor.objects.all().delete()
        category.objects.all().delete()
        location.objects.all().delete()
        Image.objects.all().delete()



class ImageTestClass(TestCase):
    def test_search_by_category(self):
        category=Image.objects.all()
        search_term='food'
        db_term=search_term
        if db_term !=search_term:
            return('no match')

        else:
            return(search_term)

