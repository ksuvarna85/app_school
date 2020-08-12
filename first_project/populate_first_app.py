import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic,Webpage,AccessRecords
from faker import Faker

fakgen=Faker()
topics=['search','social','marketplace','news','games']
def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        top=add_topic()
        fake_url=fakgen.url()
        fake_date=fakgen.date()
        fake_name=fakgen.company()
        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acc=AccessRecords.objects.get_or_create(name=webpg,date=fakgen.date())[0]
if __name__ == '__main__':
    print('populatin')
    populate(20)
    
    print('compleated')
