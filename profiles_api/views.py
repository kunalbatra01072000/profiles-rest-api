from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from rest_framework import viewsets


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


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializers

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list,create,retrieve,update,partial_update)',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new message"""
        serializer = self.serializer_class(data=request.data)

        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'hello {name} !'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """return obj by its id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """handle updating obj"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """partial update"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """delete object"""
        return Response({'http_method': 'DELETE'})
