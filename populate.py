import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','protwo.settings')

import django
django.setup()

import random
from faker import Faker

from apptwo.models import Topic,Webpage,AccessRecord

fakedata = Faker()
topics = ['Search','Social','News','Article']

def add_topic():
    name = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    name.save()
    return name

def populate(N=5):

    for entry in range(N):
        
        # Get Topic for entry
        top = add_topic()

        # Create Fake Entry
        fake_name = fakedata.name()
        fake_url = fakedata.url()
        fake_date = fakedata.date()

        # Create New Web Entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # Create Fake Access Record
        accrec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Creating the database.... Please Wait")
    print(20)
    print('Data Complted!')
