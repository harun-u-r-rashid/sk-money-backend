from django.shortcuts import render

from .serializers import (
    PackageSerializer,
    PackageUpdateSerializer,
    DepositSerializer,
    DepositHistorySerializer,
    WithdrawHistorySerializer,
    WithdrawSerializer,
    DepositStatusUpdateSerializer,
    WithdrawStatusUpdateSerializer,
    PartnerSerializer,
)
from .models import Package, Deposit, Withdraw, Partner
from appAuth.models import User, Profile

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
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [AllowAny]


class PackageCreateView(generics.CreateAPIView):
    serializer_class = PackageSerializer
    permission_class = [AllowAny]
    queryset = Package.objects.all()

    def create(self, request, *args, **kwargs):
        profile = request.data["profile"]
        title = request.data["title"]
        price = request.data["price"]
        description = request.data["description"]

        owner = Profile.objects.filter(id=profile).first()

        package = Package()
        package.profile = owner
        package.title = title
        package.price = price
        package.description = description

        package.save()

        return Response(
            {"message": "Package created successfully"}, status=status.HTTP_201_CREATED
        )


class PackageUpdateView(generics.UpdateAPIView):
    serializer_class = PackageUpdateSerializer
    permission_classes = [AllowAny]
    queryset = Package.objects.all()
    look_field = "pk"

    def perform_update(self, serializer):
        serializer.save()
        return serializer.data


class PackageDeleteView(generics.DestroyAPIView):
    serializer_class = PackageSerializer
    permission_classes = [AllowAny]
    queryset = Package.objects.all()

    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        package = self.get_object()
        package.delete()

        return Response(
            {"message": "Project deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


# ======== View for Deposit ===========


class DepositHistoryView(generics.ListAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositHistorySerializer
    permission_classes = [AllowAny]


class DepositCreateView(generics.CreateAPIView):
    serializer_class = DepositSerializer
    permission_class = [AllowAny]
    queryset = Deposit.objects.all()

    def create(self, request, *args, **kwargs):
        profile = request.data["profile"]
        amount = request.data["amount"]
        tran_id = request.data["tran_id"]

        owner = Profile.objects.filter(id=profile).first()

        if amount < 500:
            return Response(
                {"message": "Minimum deposit amount 500 tk."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        deposit = Deposit()
        deposit.profile = owner
        deposit.amount = amount
        deposit.tran_id = tran_id
        deposit.save()

        return Response(
            {"message": "Deposited " f"{amount}" "tk. Wait for approval."},
            status=status.HTTP_201_CREATED,
        )


class DepositStatusUpdateView(generics.UpdateAPIView):
    serializer_class = DepositStatusUpdateSerializer
    permission_classes = [AllowAny]
    queryset = Deposit.objects.all()
    look_field = "pk"

    def perform_update(self, serializer):

        deposit = self.get_object()
        amount = deposit.amount
        print(amount)
        profile = deposit.profile
        profile.balance += amount
        print(profile.balance)
        profile.save()
        serializer.save()
        return serializer.data
        # return Response({"message": f"Approved the deposit of {profile}. {amount}tk added to {profile}'s account."})


# ======== View for Withdraw ===========


class WithdrawHistoryView(generics.ListAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawHistorySerializer
    permission_classes = [AllowAny]


class WithdrawCreateView(generics.CreateAPIView):
    serializer_class = WithdrawSerializer
    permission_class = [AllowAny]
    queryset = Withdraw.objects.all()

    def create(self, request, *args, **kwargs):
        profile = request.data["profile"]
        amount = request.data["amount"]
        tran_id = request.data["tran_id"]

        owner = Profile.objects.filter(id=profile).first()
        # print(owner.balance)

        if amount < 500:
            return Response(
                {"message": "Minimum withdraw amount 500 tk."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if owner.balance < amount:
            return Response(
                {"message": "Insufficient balance."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        withdraw = Withdraw()
        withdraw.profile = owner
        withdraw.amount = amount
        withdraw.tran_id = tran_id
        withdraw.save()

        return Response(
            {"message": "Withdrawn " f"{amount}" "tk. Wait for approval"},
            status=status.HTTP_201_CREATED,
        )


class WithdrawStatusUpdateView(generics.UpdateAPIView):
    serializer_class = WithdrawStatusUpdateSerializer
    permission_classes = [AllowAny]
    queryset = Withdraw.objects.all()
    look_field = "pk"

    def perform_update(self, serializer):

        withdraw = self.get_object()
        amount = withdraw.amount
        print(amount)
        profile = withdraw.profile
        profile.balance -= amount
        print(profile.balance)
        profile.save()
        serializer.save()
        return serializer.data


# ======== View for Partner ===========


class PartnerListView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [AllowAny]
