from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MyModelViewSet  

router = DefaultRouter()
router.register(r'mypost', MyModelViewSet) 
urlpatterns = [
    # ... other URL patterns ...
]

# Include the router's URL patterns in your urlpatterns
urlpatterns += router.urls

