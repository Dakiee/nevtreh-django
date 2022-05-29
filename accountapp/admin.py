from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Facebook)
admin.site.register(Page)
admin.site.register(Post)
admin.site.register(Group)
admin.site.register(City)
admin.site.register(Country)
