from django.contrib import admin
from audioServer.models import Song, Podcast, Audiobook

# Register your models here.
admin.site.register(Song)
admin.site.register(Podcast)
admin.site.register(Audiobook)