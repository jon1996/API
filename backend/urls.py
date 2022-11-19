from django.urls import path,include, re_path as url
from rest_framework import routers
from .views import report

router = routers.DefaultRouter()
router.register('report', report)


urlpatterns = [
    path('', include(router.urls)),
]
