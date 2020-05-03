from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class HelloApiView(APIView):
    """API View"""

    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch ,post, put,delete )', 'Is similar to traditional django view',
            'give u the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message ': message})

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method': 'DELETE'})
