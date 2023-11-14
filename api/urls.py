from django.contrib import admin
from django.urls import path,include
from .views import CreateCrypto,editCrypto,GetBasedCategory,GetBasedCategorygift,CreateGiftcard
from rest_framework import routers



# router = routers.DefaultRouter()
# router.register(r'newsletters', NewsletterViewSet)
# router.register(r'subscribers', SubscriberViewSet)

urlpatterns = [
    path('edit/',editCrypto),
    path('create/', CreateCrypto),
    path('creategift/', CreateGiftcard),
    path('trade/<str:transaction>/', GetBasedCategory),
    path('giftcard/<str:transaction>/', GetBasedCategorygift),
    # path('api/', include(router.urls)),
    
]
