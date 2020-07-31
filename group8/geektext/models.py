from django.db import models

class Books(models.Model):
    book_title = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    number_sold = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.book_title

