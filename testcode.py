import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from Main_app.models import *

topics = Topic.objects.all()
print(topics)
'''
for t in topics:
    print(t.text)
    print(t.data_added)
'''

Chess = Topic.objects.get(id=1)
print(Chess.text)

entries = Entry.objects.filter(topic=Chess)

for e in entries:
    print(e.text)
    print(e.data_added)

from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username)
    print(user.last_login)


