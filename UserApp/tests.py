from django.contrib.auth.hashers import make_password, check_password
from django.test import TestCase

# Create your tests here.


a = make_password('110')


check_password()