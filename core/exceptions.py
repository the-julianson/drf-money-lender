from rest_framework.exceptions import APIException
from rest_framework import status


class DefaultViewException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {}

    def __init__(self, detail=None, code=None, *args, **kwargs):
        self.status_code = code
        super().__init__(detail, code)
