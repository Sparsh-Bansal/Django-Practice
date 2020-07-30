import os
import django
import random
from first_project.firstapp.models import Topic , WebPage , AccessRecord
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')


fakegen = Faker()

topics = ['Search' , 'Social' , 'Marketplace' , 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create()