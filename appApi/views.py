from django.shortcuts import render
from django.utils.timezone import now
from . import serializers
from . import models

from appAuth.models import User

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from rest_framework import status
from rest_framework.response import Response


# ======== View for Package===========


class PackageListView(generics.ListAPIView):
    queryset = models.Package.objects.all()
    serializer_class = serializers.PackageSerializer
    permission_classes = [AllowAny]


class PackageCreateView(generics.CreateAPIView):
    serializer_class = serializers.PackageSerializer
    permission_class = [AllowAny]
    queryset = models.Package.objects.all()

    def create(self, request, *args, **kwargs):
        # profile = request.data["profile"]
        title = request.data["title"]
        price = request.data["price"]
        description = request.data["description"]

        # owner = Profile.objects.filter(id=profile).first()

        package = models.Package()
        # package.profile = owner
        package.title = title
        package.price = price
        package.description = description

        package.save()

        return Response(
            {"message": "Package created successfully"}, status=status.HTTP_201_CREATED
        )


# class PackageUpdateView(generics.UpdateAPIView):
#     serializer_class = PackageUpdateSerializer
#     permission_classes = [AllowAny]
#     queryset = Package.objects.all()
#     look_field = "pk"

#     def perform_update(self, serializer):
#         serializer.save()
#         return serializer.data


# class PackageDeleteView(generics.DestroyAPIView):
#     serializer_class = PackageSerializer
#     permission_classes = [AllowAny]
#     queryset = Package.objects.all()

#     lookup_field = "pk"

#     def destroy(self, request, *args, **kwargs):
#         package = self.get_object()
#         package.delete()

#         return Response(
#             {"message": "Project deleted successfully."},
#             status=status.HTTP_204_NO_CONTENT,
#         )


# ==========Slider Image RetriveView ============


class SliderImageView(generics.ListAPIView):
    queryset = models.SliderImage.objects.all()
    serializer_class = serializers.SliderImageSerializer
    permission_classes = [AllowAny]


# # ======== View for Deposit ===========


class DepositHistoryView(generics.ListAPIView):
    queryset = models.Deposit.objects.all()
    serializer_class = serializers.DepositHistorySerializer
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def get_queryset(self):
        user = self.request.user  # This will be the authenticated user
        print("User", user)
        return models.Deposit.objects.filter(user=user)


class AllDepositHistoryView(generics.ListAPIView):
    queryset = models.Deposit.objects.all()
    serializer_class = serializers.DepositHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return models.Deposit.objects.filter(status="PENDING")


class DepositCreateView(generics.CreateAPIView):
    serializer_class = serializers.DepositSerializer
    permission_class = [AllowAny]
    queryset = models.Deposit.objects.all()

    def create(self, request, *args, **kwargs):
        user = request.data["user"]
        amount = request.data["amount"]
        tran_id = request.data["tran_id"]

        owner = models.User.objects.filter(id=user).first()
        is_tran_id = models.Deposit.objects.filter(tran_id=tran_id)

        if amount < 100:
            return Response(
                {"message": "Minimum deposit amount 100$."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if is_tran_id:
            return Response(
                {"message": "Transaction ID already exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        deposit = models.Deposit()
        deposit.user = owner
        deposit.amount = amount
        deposit.tran_id = tran_id
       
        
        deposit.save()

        return Response(
            {"message": "Deposited " f"{amount}" "tk. Wait for approval."},
            status=status.HTTP_201_CREATED,
        )


class DepositStatusUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.DepositStatusUpdateSerializer
    permission_classes = [AllowAny]
    queryset = models.Deposit.objects.all()
    look_field = "pk"

    def perform_update(self, serializer):

        deposit = self.get_object()
        amount = deposit.amount

        profit = (amount*0.01)
        print(amount)
        user = deposit.user
        user.balance += amount
        user.profit += profit
        deposit.profit_start_date = now().date()
        print(user.balance)
        user.save()
        serializer.save()
        return serializer.data


# # ======== View for Withdraw ===========


# class WithdrawHistoryView(generics.ListAPIView):
#     queryset = Withdraw.objects.all()
#     serializer_class = WithdrawHistorySerializer
#     permission_classes = [AllowAny]


# class WithdrawCreateView(generics.CreateAPIView):
#     serializer_class = WithdrawSerializer
#     permission_class = [AllowAny]
#     queryset = Withdraw.objects.all()

#     def create(self, request, *args, **kwargs):
#         profile = request.data["profile"]
#         amount = request.data["amount"]
#         tran_id = request.data["tran_id"]

#         owner = Profile.objects.filter(id=profile).first()
#         # print(owner.balance)

#         if amount < 500:
#             return Response(
#                 {"message": "Minimum withdraw amount 500 tk."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         if owner.balance < amount:
#             return Response(
#                 {"message": "Insufficient balance."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         withdraw = Withdraw()
#         withdraw.profile = owner
#         withdraw.amount = amount
#         withdraw.tran_id = tran_id
#         withdraw.save()

#         return Response(
#             {"message": "Withdrawn " f"{amount}" "tk. Wait for approval"},
#             status=status.HTTP_201_CREATED,
#         )


# class WithdrawStatusUpdateView(generics.UpdateAPIView):
#     serializer_class = WithdrawStatusUpdateSerializer
#     permission_classes = [AllowAny]
#     queryset = Withdraw.objects.all()
#     look_field = "pk"

#     def perform_update(self, serializer):

#         withdraw = self.get_object()
#         amount = withdraw.amount
#         print(amount)
#         profile = withdraw.profile
#         profile.balance -= amount
#         print(profile.balance)
#         profile.save()
#         serializer.save()
#         return serializer.data


# ======== View for Partner ===========


class PartnerListView(generics.ListAPIView):
    queryset = models.Partner.objects.all()
    serializer_class = serializers.PartnerSerializer
    permission_classes = [AllowAny]
