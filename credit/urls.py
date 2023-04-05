from django.urls import path, include
from rest_framework import routers

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from credit.api.viewsets import LoanRequestViewSet


router = routers.DefaultRouter()

router.register("loan-requests", LoanRequestViewSet, basename="loan-requests")

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
