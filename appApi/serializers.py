from rest_framework import serializers
from .models import Package, Partner, SliderImage
from . import models
from appAuth.serializers import UserDetailsSerializer

# ========Serializers for Package======#
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ["image", "title", "price", "price_taka", "description"]


class PackageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ["title", "price", "description"]


class SliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImage
        fields = ["image1", "image2", "image3"]


# # ========Serializers for Deposit ======#


class DepositHistorySerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    class Meta:
        model = models.Deposit
        fields = ["id", "user", "amount", "transaction_id", "status"]


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deposit
        fields = ["user", "package_name", "amount", "send_number", "transaction_id"]


class DepositStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deposit
        fields = ["status"]


# # ========Serializers for Deposit ======#
class WithdrawHistorySerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    class Meta:
        model = models.Withdraw
        fields = ["id", "user", "amount", "bkash_number", "status"]


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Withdraw
        fields = ["user", "amount", "bkash_number", "msg"]


class WithdrawStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Withdraw
        fields = ["status"]


# # ========== Serializer for Partner========


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"
