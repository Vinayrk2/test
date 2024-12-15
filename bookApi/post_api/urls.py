from django.urls import path
from .views import PostReviewView

urlpatterns = [
    path('review/', PostReviewView.as_view(), name='post_review'),
]
