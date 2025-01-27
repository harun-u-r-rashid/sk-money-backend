from rest_framework import serializers
from .models import Package, Partner, SliderImage
from . import models


# ========Serializers for Package======#
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ["image", "title", "price", "description"]


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
    class Meta:
        model = models.Deposit
        fields = ["id","user","amount", "tran_id", "status"]


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deposit
        fields = ["user", "amount", "tran_id"]


class DepositStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deposit
        fields = ["status"]


# # ========Serializers for Deposit ======#
class WithdrawHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Withdraw
        fields = ["id","user", "amount", "b_number", "status"]


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Withdraw
        fields = ["user", "amount", "b_number", "msg"]


class WithdrawStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Withdraw
        fields = ["status"]


# # ========== Serializer for Partner========


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"
