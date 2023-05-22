from django.contrib import admin
from .models import Person, StickyNote, Note

# Register your models here.
admin.site.register(Person)
admin.site.register(StickyNote)
admin.site.register(Note)