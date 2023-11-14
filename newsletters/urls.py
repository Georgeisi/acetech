# in newsletters/urls.py
from django.urls import path
from .views import send_newsletterr,SubscriberViewSet
from rest_framework.routers import DefaultRouter


app_name = 'newsletters'

router = DefaultRouter()
router.register(r'subscribers', SubscriberViewSet, basename='subscriber')

urlpatterns = [
    path('send/<int:newsletter_id>/', send_newsletterr, name='send_newsletterr'),
    path('subscribe/', SubscriberViewSet.as_view({'post': 'create'}), name='subscribe'),
]

urlpatterns += router.urls

