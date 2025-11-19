from rest_framework import viewsets
from .models import Subject, Level, SchoolClass, TeachingProgram
from .serializers import SubjectSerializer, LevelSerializer, SchoolClassSerializer, TeachingProgramSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer

class TeachingProgramViewSet(viewsets.ModelViewSet):
    queryset = TeachingProgram.objects.all()
    serializer_class = TeachingProgramSerializer
