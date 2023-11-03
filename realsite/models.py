from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Writer(models.Model):
    creatorname = models.CharField(max_length=200,default='Name')
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    born_date = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='Male' 
    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="Age must be at least 1."),
            MaxValueValidator(100, message="Age cannot exceed 100."),
        ]
    )
    image = models.ImageField(upload_to='writer_images/', blank=True, null=True)

    def __str__(self):
        return f'{self.age}-year-old {self.gender} writer'

class Book(models.Model):
    booktitle = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='book_pictures/', blank=True, null=True)
    info = models.TextField()
    creator = models.ForeignKey(Writer, on_delete=models.CASCADE)
    release = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date', )

    def __str__(self):
        return self.booktitle

class Chapter(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='book_chapters')
    ctitle = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    story = models.TextField()
    chapter_number = models.IntegerField(default=0)

    def __str__(self):
        return self.title