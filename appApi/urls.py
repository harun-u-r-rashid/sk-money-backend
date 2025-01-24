from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #    Packages URL
    path("list/", views.PackageListView.as_view()),
    path("create/", views.PackageCreateView.as_view()),
    path("update/<int:pk>/", views.PackageUpdateView.as_view()),
    path("delete/<int:pk>/", views.PackageDeleteView.as_view()),
    # # Deposit URL
    # path("deposit_history/", views.DepositHistoryView.as_view()),
    # path("deposit_create/", views.DepositCreateView.as_view()),
    # path("deposit_status_update/<int:pk>/", views.DepositStatusUpdateView.as_view()),
    # # Withdrawn URL
    # path("withdraw_history/", views.WithdrawHistoryView.as_view()),
    # path("withdraw_create/", views.WithdrawCreateView.as_view()),
    # path("withdraw_status_update/<int:pk>/", views.WithdrawStatusUpdateView.as_view()),
    # # Partner URL
    path("partner_list/", views.PartnerListView.as_view()),
]
