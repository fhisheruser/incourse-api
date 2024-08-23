# courses/models.py

from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.title

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # This already creates a 'course_id' field
    year = models.PositiveIntegerField()
    semester = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.course.title} - {self.year} Semester {self.semester}"
