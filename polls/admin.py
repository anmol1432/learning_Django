'''
Make the poll app modifiable in the admin
But where’s our poll app? It’s not displayed on the admin index page.

Only one more thing to do: we need to tell the admin that Question objects have an admin interface. 
To do this, open the polls/admin.py file, and edit it to look like this:

polls/admin.py¶
from django.contrib import admin

from .models import Question

admin.site.register(Question)
'''
from django.contrib import admin
from .models import Question, Choice
from django.contrib.admin import AdminSite

# Register your models here to show in admin pannel.
admin.site.register(Question)
admin.site.register(Choice)