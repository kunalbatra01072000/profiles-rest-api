from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """API View"""

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch ,post, put,delete )', 'Is similar to traditional django view',
            'give u the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
