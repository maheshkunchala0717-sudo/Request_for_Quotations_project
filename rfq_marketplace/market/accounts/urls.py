from django.urls import path
from .views import RFQListCreateView,RFQDetailView,QuatationListCreateView,QuatationDetailView,RegisterView,LoginView,SelectQuotationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from .views import (
    home,
    register_page,
    rfqs_page,
    rfq_details_page,
    create_rfq_page,
    edit_rfq_page,
    create_quotation_page,
    quotations_page,
    edit_quotation_page,)












urlpatterns=[path("rfqs/",RFQListCreateView.as_view(),name="rfq-list-create"),
             path("rfqs/<int:pk>/",RFQDetailView.as_view(),name="rfq-detail"),
             path("quatations/",QuatationListCreateView.as_view(),name="quatation-list-create"),
             path("quatations/<int:pk>/",QuatationDetailView.as_view(),name="quatation-detail"),
             path("register/",RegisterView.as_view(),name="register"),
             path("login/",LoginView.as_view(),name="login"),
             path("token/", TokenObtainPairView.as_view(), name="token"),
             path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
             path(
    "quatations/<int:pk>/select/",
    SelectQuotationView.as_view(),
    name="quatation-select"
),
path("", home, name="home"),
path("register-page/", register_page, name="register-page"),
path("rfqs-page/", rfqs_page, name="rfqs-page"),
path("rfq-details/", rfq_details_page, name="rfq-details"),
path("create-rfq/", create_rfq_page, name="create-rfq"),
path("edit-rfq/", edit_rfq_page, name="edit-rfq"),
path("create-quotation/", create_quotation_page, name="create-quotation"),
path("quotations-page/", quotations_page, name="quotations-page"),
path("edit-quotation/", edit_quotation_page, name="edit-quotation"),


]

