from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from core.exceptions import DefaultViewException
from credit.api.serializers import LoanRequestSerializer
from credit.models import LoanRequest


class LoanRequestViewSet(ModelViewSet):
    """Provides CRUD operations for managing Loan Requests"""

    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        ser = LoanRequestSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        approved = pre_score(request.data["personal_id"])

        request.data["approved"] = approved

        return super().create(request, *args, **kwargs)


def pre_score(personal_id):
    # TODO mover esto a un funcion helper, sacar el import fuera. Usar variables de entorno

    pre_score_status = True
    import requests
    url = f"https://api.moni.com.ar/api/v4/scoring/pre-score/{personal_id}"
    response = requests.request("GET", url)

    if not response.status_code == status.HTTP_200_OK:

        raise DefaultViewException(
            detail={
                "message": "El servidor externo no esta funcionando"
            },
            code=status.HTTP_410_GONE,
        )

    request_approved = response.json()["status"]
    if request_approved == "rejected":
        pre_score_status = True
    return pre_score_status
