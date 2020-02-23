from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.permissions import IsAuthenticated  -- for restricting all

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


# APIView
class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Return a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as function (get,post,put,patch,delete)',
            'Is similar to traditional django view',
            'Is mapped to manually to URLS'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ create hello msg with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ handle partial update of an object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an obkect """
        return Response({'method': 'DELETE'})


# ViewSet
class HelloViewSet(viewsets.ViewSet):
    """ Test API viewset """

    def list(self, request):
        """ Return a hello message """
        a_viewset = [
            'Uses action (list,create,retrieve,update,partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """ create hello msg with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method': 'RETRIEVE'})

    def update(self, request, pk=None):
        """ handle partial update of an object """
        return Response({'method': 'UPDATE'})

    def partial_update(self, request, pk=None):
        """ Delete an obkect """
        return Response({'method': 'PARTIAL UPDATE'})

    def destroy(self, request, pk=None):
        """ Delete an obkect """
        return Response({'method': 'DESTROY'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    # tuple authentication
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    # Search according to name and email in viewset
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """ handle creating user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ handles creating,reading and updating profile feed items """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
        # IsAuthenticated
    )

    def perform_create(self, serializer):
        """ sets the user profile to the logged in user """
        serializer.save(user_profile=self.request.user)
