from rest_framework import serializers
from rest_framework import status

from credit.models import LoanRequest
from core.exceptions import DefaultViewException

import re


class LoanRequestSerializer(serializers.ModelSerializer):

    @staticmethod
    def validate_personal_id(value):

        pattern = r'^\d{7,9}$'
        # Use re.match to check if the input matches the pattern
        if not re.match(pattern, value):
            raise DefaultViewException(
                detail={"message": "El valor del ID personal debe ser un entero entre 7 y 9 dígitos."},
                code=status.HTTP_400_BAD_REQUEST
            )
        return value

    class Meta:
        model = LoanRequest
        fields = '__all__'
        read_only_fields = ('id',)
