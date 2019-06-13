import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ormpro.settings')
import django
django.setup()

from testapp.models import *  #jis table me kaam karna h uska naam
from faker import Faker
from random import *
fake=Faker()


def populate(n):
    for i in range(n):
        fno=randint(1000,5000)
        fname=fake.name()
        fsal=randint(10000,80000)
        fcity=fake.city()

        employee.objects.get_or_create(ename=fname,ecity=fcity,esal=fsal,eno=fno)

populate(25)


#by default file ka output console pe aata h ....
