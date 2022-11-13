


from asyncio.windows_events import NULL

from django.shortcuts import render
from .models import Carousel, Team, Visa



from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny, BasePermission, SAFE_METHODS

from .serializers import SendPasswordResetEmailSerializer, TeamSerializer, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserSerializer, VisaSerializer, CarouselSerializer,UserSerializer
from aegc import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

# from django.contrib.auth.decorators import login_required
# Create your views here.

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }
    
class CarouselList(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated | ReadOnly]
    
    
    def get(self, request,slug=NULL, format=None):
        if slug == NULL:
            carousels = Carousel.objects.all()
            print(carousels)
            serializers = CarouselSerializer(carousels, many=True)
            # serializers.is_valid(raise_exception=True)
            return Response(serializers.data) 
        else:
            carousel = Carousel.objects.get(slug = slug)
            serializer = CarouselSerializer(carousel)
            return Response(serializer.data) 
        
    # @login_required(login_url='/accounts/login/')
    def post(self, request,format = None):
        
            data  = request.data
            serializers = CarouselSerializer(data=data)
            if serializers.is_valid():
                serializers.save()
                return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
            
            return Response({'msg':'Data not created'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def patch(self, request,slug=NULL,format = None):
            if slug != NULL:
                data  = request.data
                carousel = Carousel.objects.get(slug = slug)
                serializers = CarouselSerializer(carousel,data=data,partial=True)
                if serializers.is_valid():
                    serializers.save()
                    return Response({'msg':'Data created'},status=status.HTTP_206_PARTIAL_CONTENT)
            
            return Response({'msg':'Data not created'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self,request, slug=NULL, format=None):
        if slug != NULL:
            obj = Carousel.objects.get(slug = slug)
            obj.delete()
            return Response("Item successfully deleted")
        
        return Response({"msg":"Unsuccessfull"},serializers.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TeamList(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated | ReadOnly]
    
    
    def get(self, request,slug=NULL, format=None):
        if slug == NULL:
            team = Team.objects.all()
           
            serializers = TeamSerializer(team, many=True)
            # serializers.is_valid(raise_exception=True)
            return Response(serializers.data) 
        else:
            team = Team.objects.get(slug = slug)
            serializer = TeamSerializer(team)
            return Response(serializer.data) 

class VisaList(APIView):
    def get(self, request, format=None):
        visas = Visa.objects.all()
        print(visas)
        serializer = VisaSerializer(visas, many=True)
        return Response(serializer.data) 


# ....................login and resgistration..............

class UserRegistrationView(APIView):
#   renderer_classes = [UserRenderer]
    permission_classes=[AllowAny]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
#   renderer_classes = [UserRenderer]
    permission_classes=[AllowAny]
    authentication_classes=[JWTAuthentication]
    
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class UserChangePasswordView(APIView):
#   renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  authentication_classes=[JWTAuthentication]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

class SendPasswordResetEmailView(APIView):
#   renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
#   renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)

