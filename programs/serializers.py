from rest_framework import serializers
from .models import Subject, Level, SchoolClass, TeachingProgram

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class SchoolClassSerializer(serializers.ModelSerializer):
    level = LevelSerializer(read_only=True)
    class Meta:
        model = SchoolClass
        fields = '__all__'

class TeachingProgramSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    school_class = SchoolClassSerializer(read_only=True)
    
    class Meta:
        model = TeachingProgram
        fields = '__all__'
