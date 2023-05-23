from django.contrib import admin
from .models import StickyNote, Note

# Register your models here.
admin.site.register(StickyNote)
admin.site.register(Note)