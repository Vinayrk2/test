from django.db import models
from useraccount.models import ApplicationUser

class BookReview(models.Model):
    user = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.book_title}"