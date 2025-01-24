from rest_framework import serializers
from .models import Package, Partner


# ========Serializers for Package======#
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ["image", "title", "price", "description"]


class PackageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ["title", "price", "description"]


# # ========Serializers for Deposit ======#


# class DepositHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Deposit
#         fields = ["profile", "amount", "tran_id", "status"]


# class DepositSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Deposit
#         fields = ["profile", "amount", "tran_id"]


# class DepositStatusUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Deposit
#         fields = ["status"]


# # ========Serializers for Deposit ======#
# class WithdrawHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Deposit
#         fields = ["profile", "amount", "tran_id", "status"]


# class WithdrawSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Deposit
#         fields = ["profile", "amount", "tran_id"]


# class WithdrawStatusUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Deposit
#         fields = ["status"]


# # ========== Serializer for Partner========


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"
