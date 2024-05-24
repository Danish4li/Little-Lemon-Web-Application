from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title='IceCream', price=80, inventory=100)
    
    def test_get_all(self):
        pass
        # item = Menu.objects.get(title='IceCream')
        # self.assertEqual(str(item), 'IceCream : 80')