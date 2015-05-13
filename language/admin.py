from django.contrib import admin

# Register your models here.
from language.models import Quiz, Video

admin.site.register(Quiz)
admin.site.register(Video)
