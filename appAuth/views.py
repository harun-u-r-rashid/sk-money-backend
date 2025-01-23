from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,

)
from django.contrib.auth.hashers import check_password

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from decimal import Decimal
from rest_framework import status
from rest_framework.response import Response

from . import serializers
from .models import User, OneTimePassword
from .utils import send_code_to_activate_user_account



# ========== User Registration =======
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        print(request.data)
        user = request.data

        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data = serializer.data

            send_code_to_activate_user_account(user_data["email"])
            return Response(
                {
                    "data": user_data,
                    "message": "A passcode has been sent to your email",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# =========== User Verify========#

class VerifyUserView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.OTPCodeSerializer

    def post(self, request):
        serializer = serializers.OTPCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp_code = serializer.validated_data.get("otp")

        try:
            user_code = OneTimePassword.objects.get(code=otp_code)
            user = user_code.user
            if not user.is_active:
                user.is_active = True
                user.save()
                return Response(
                    {"message": "Email verified successfully."},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"message": "Code is not valid"}, status=status.HTTP_204_NO_CONTENT
            )
        except OneTimePassword.DoesNotExist:
            return Response(
                {"message": "Passcode not provided.."},
                status=status.HTTP_400_BAD_REQUEST,
            )

# =======For USER LOGIN==========#
class LoginView(APIView):
    serializer_class = serializers.LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
  
        return Response(serializer.data, status=status.HTTP_200_OK)
    


# =======For USER LOGOUT==========#

class LogoutView(APIView):
    serializer_class = serializers.LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.data
        return Response(status=status.HTTP_200_OK)


# =======User Search View=======#


class SearchUserView(generics.ListAPIView):
        serializer_class = serializers.UserSerializer
        permission_classes = [AllowAny]

        def get_queryset(self):
            user_id = self.request.GET.get("id")
            if user_id:
                return User.objects.filter(
                    id = user_id
                )  
            return Response({"message":"User doesn't exists."})


