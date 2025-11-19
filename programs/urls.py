from rest_framework import routers
from django.urls import path, include
from .views import SubjectViewSet, LevelViewSet, SchoolClassViewSet, TeachingProgramViewSet

router = routers.DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'levels', LevelViewSet)
router.register(r'classes', SchoolClassViewSet)
router.register(r'programs', TeachingProgramViewSet)

urlpatterns = [
    path('', include(router.urls)),
]