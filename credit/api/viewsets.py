from rest_framework.viewsets import ModelViewSet

from credit.api.serializers import LoanRequestSerializer
from credit.models import LoanRequest


class LoanRequestViewSet(ModelViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
