from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BookReview
from .middleware import APIKeyAuthentication

class PostReviewView(APIView):
    authentication_classes = [APIKeyAuthentication]

    def post(self, request):
        user = request.user
        book_title = request.data.get('book_title')
        review = request.data.get('review')
        rating = request.data.get('rating')

        if not book_title or not review or not rating:
            return Response({'error': 'All fields are required (`book_title`, `review`, `rating`).'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                raise ValueError
        except ValueError:
            return Response({'error': 'Rating must be an integer between 1 and 5.'}, status=status.HTTP_400_BAD_REQUEST)

        book_review = BookReview.objects.create(
            user=user,
            book_title=book_title,
            review=review,
            rating=rating
        )

        return Response({
            'message': 'Review posted successfully',
            'review_id': book_review.id,
            'book_title': book_review.book_title,
            'rating': book_review.rating
        }, status=status.HTTP_201_CREATED)
        
    def get(self, request):
        reviews = BookReview.objects.all()
        return Response([{'id': review.id, 'book_title': review.book_title, 'rating': review.rating, 'review': review.review, 'user': review.user.username} for review in reviews], status=status.HTTP_200_OK)
