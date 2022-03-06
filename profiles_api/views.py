from configparser import NoOptionError
import imp
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiview = [
            'uses HTTP methods as function (get, post, patxh, put, delete)',
            'is similar to a traditional django view',
            'gives you the countrol over your application logic',
            'is mapped manually to urls'
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})


    def post(self, request):
        """create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'

            return Response({'message':message})

        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )
        
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response ({'method': 'PUT'})


    def path(self, request, pk=None):
        """Hnadle a partial update"""
        return Response({'method':'PATCH'})

    
    def delete(self, requets, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'uses actions : list, create, retrive, update, partial update',
            'automatically maps to URLs using Routers',
            'provides more functionality with less code'
        ]

        return Response({'message': 'hello', 'a_viewset':a_viewset})


    def create(self, request):
        """create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'

            return Response({'message':message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk=None):
        """handle getting an object by its id"""
        return Response({'Http method':'GET'})


    def update(self, request, pk=None):
        """handle updating an object by its id"""
        return Response({'Http method':'PUT'})


    def partial_update(self, request, pk=None):
        """handle updateing the part of the object"""
        return Response({'Http method':'PATCH'})


    def destroy(self, request, pk=None):
        """handle removing an object"""
        return Response({'Http method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updateing profile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
