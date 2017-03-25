from django.test import TestCase
from .models import location
from rest_framework.request import Request
from django.test import TestCase
from django.test import Client
from .views import locationlist


class ExapmplePostTest(TestCase):

  def setUpClass(self):
    self.client = Client()


''' Adding Account into the application '''

requestname='sdf'
requestlong=343
requestlag=434
def test_addAccount(self,request):
     location.name=requestname
     location.lag=requestlag
     location.long=requestlong
     location.save()


test_addAccount(request='POST')



