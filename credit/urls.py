from django.urls import path, include
from rest_framework import routers

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from credit.api.viewsets import LoanRequestViewSet


router = routers.DefaultRouter()

router.register(r"credit", LoanRequestViewSet, basename="credit")


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
