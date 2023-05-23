from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('note', views.NoteViewSet)
router.register('stickynote', views.StickyNoteViewSet)

urlpatterns = router.urls