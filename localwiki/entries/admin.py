from django.contrib import admin
from .models import WikiPage #import all models from our directory

admin.site.register(WikiPage)