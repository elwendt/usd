from django.db import models


class Course(models.Model):

    name = models.CharField('Course Code', max_length=50, help_text='USD Course Code',
                            default='USD course name')
    title = models.CharField('Course Title', max_length=50, help_text='USD Course Title',
                             default='USD course title')

    def __str__(self):
        return self.course_name


class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=100, default='author name')
    bio = models.CharField(max_length=1000, default='author bio')

    def __str__(self):
        return self.author_name


# Create your models here.
class Papers(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, help_text='Enter the name of the assignment',
                            default='paper name')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book',
                               default='paper summary')

    def __str__(self):
        return self.assignment_name




