from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from credit.api.serializers import LoanRequestSerializer
from credit.models import LoanRequest

from credit.api import swagger_schema


class LoanRequestViewSet(ModelViewSet):
    """ Provides CRUD operations for managing Loan Requests
    """
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        ser = LoanRequestSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        # TODO Add request to validate scoring
        return super().create(request, *args, **kwargs)



