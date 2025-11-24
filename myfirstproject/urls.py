from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from students.views import StudentViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
