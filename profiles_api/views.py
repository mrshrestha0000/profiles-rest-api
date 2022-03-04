from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiview = [
            'uses HTTP methods as function (get, post, patxh, put, delete)',
            'is similar to a traditional django view',
            'gives you the countrol over your application logic',
            'is mapped manually to urls'
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})

