from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import obtain_auth_token


from .serializers import UserSerializer

Login = obtain_auth_token


class LogoutAPIView(APIView):
    pass


class UserRegistration(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = (UserSerializer, )


    def post(self, request):

        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                "message" : "user create"
            })


        return Response({'message': user_serializer.errors})
