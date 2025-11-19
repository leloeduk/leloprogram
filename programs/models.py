from django.db import models

# ----- DOMAINE / MATIÈRE -----
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)  # ex: Mathématiques, Physique
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# ----- NIVEAU (Primaire, Collège, Lycée…) -----
class Level(models.Model):
    name = models.CharField(max_length=100, unique=True)  # ex : Collège, Lycée

    def __str__(self):
        return self.name


# ----- CLASSE -----
class SchoolClass(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="classes")
    name = models.CharField(max_length=50)  # ex : 6e, 5e, 2nde

    class Meta:
        unique_together = ('level', 'name')

    def __str__(self):
        return f"{self.level.name} - {self.name}"


# ----- PROGRAMME D'ENSEIGNEMENT -----
class TeachingProgram(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="programs")
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, related_name="programs")
    year = models.PositiveIntegerField()  # ex : 2024
    author = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('subject', 'school_class', 'year')

    def __str__(self):
        return f"{self.subject.name} - {self.school_class} ({self.year})"
