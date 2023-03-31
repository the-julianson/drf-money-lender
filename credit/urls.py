from django.urls import path, include
from rest_framework import routers

from credit.api.viewsets import LoanRequestViewSet


router = routers.DefaultRouter()

router.register("loan-requests", LoanRequestViewSet, basename="loan-requests")

urlpatterns = [
    path('api/', include(router.urls)),
]
