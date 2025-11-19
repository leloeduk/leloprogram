from django.contrib import admin
from .models import Subject, Level, SchoolClass, TeachingProgram

# Admin pour Subject
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Admin pour Level
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Admin pour SchoolClass
@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    list_filter = ('level',)
    search_fields = ('name',)

# Admin pour TeachingProgram
@admin.register(TeachingProgram)
class TeachingProgramAdmin(admin.ModelAdmin):
    list_display = ('subject', 'school_class', 'year', 'author', 'pdf')
    list_filter = ('subject', 'school_class', 'year')
    search_fields = ('subject__name', 'school_class__name', 'author')
