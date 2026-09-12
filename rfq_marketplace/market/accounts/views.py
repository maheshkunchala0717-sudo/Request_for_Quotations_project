from django.shortcuts import render
from .models import RFQ,Quatation
from .serializers import RFQSerializers,QuatationSerializers,UserSerializer,LoginSerializer
from rest_framework import generics,filters
from .permissions import IsBuyer,IsSupplier,IsBuyerOwner,IsSupplierOwner
from rest_framework.views import APIView
from django.shortcuts import render

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class RFQListCreateView(generics.ListCreateAPIView):
    queryset=RFQ.objects.all()
    serializer_class = RFQSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    search_fields = [
        "product_service",
        "description",
        "deliver_location",
    ]

    filterset_fields = [
        "deliver_location",
        "quantity",
        "dead_line",
    ]

    def get_queryset(self):
        if self.request.user.role == "buyer":
            return RFQ.objects.filter(buyer=self.request.user)

        if self.request.user.role == "supplier":
            return RFQ.objects.all()

        return RFQ.objects.none()

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)
  

class RFQDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=RFQ.objects.all()
    serializer_class=RFQSerializers
    permission_classes=[IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ["PUT","PATCH","DELETE"]:
            return [IsBuyerOwner()]
        return [IsAuthenticated()]


    def get_queryset(self):
        if self.request.user.role == "buyer":
            return RFQ.objects.filter(
                buyer=self.request.user
            )

        if self.request.user.role == "supplier":
            return RFQ.objects.all()

        return RFQ.objects.none()

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsBuyerOwner()]

        return [IsAuthenticated()]


class QuatationListCreateView(generics.ListCreateAPIView):
    queryset = Quatation.objects.all()
    serializer_class = QuatationSerializers

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsSupplier()]
        return [IsAuthenticated()]

    def get_queryset(self):
        if self.request.user.role == "supplier":
            return Quatation.objects.filter(
                supplier=self.request.user
            )

        if self.request.user.role == "buyer":
            return Quatation.objects.filter(
                rfq__buyer=self.request.user
            )

        return Quatation.objects.none()

    def perform_create(self, serializer):
        serializer.save(supplier=self.request.user)




class QuatationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Quatation.objects.all()
    serializer_class=QuatationSerializers
    
    
    def get_permissions(self):
            if self.request.method in ["PUT","PATCH","DELETE"]:
                return [IsSupplierOwner()]
            return [IsAuthenticated()]
    



class SelectQuotationView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        try:
            quotation = Quatation.objects.get(pk=pk)
        except Quatation.DoesNotExist:
            return Response(
                {"error": "Quotation not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Only the buyer who owns the RFQ can select
        if request.user.role != "buyer":
            return Response(
                {"error": "Only buyers can select quotations."},
                status=status.HTTP_403_FORBIDDEN
            )

        if quotation.rfq.buyer != request.user:
            return Response(
                {"error": "You can only select quotations for your own RFQs."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Remove previous selection for this RFQ
        Quatation.objects.filter(
            rfq=quotation.rfq
        ).update(
            is_selected=False
        )

        # Select this quotation
        quotation.is_selected = True
        quotation.save()

        return Response(
            {
                "message": "Quotation selected successfully.",
                "quotation_id": quotation.id
            },
            status=status.HTTP_200_OK
        )


class RegisterView(generics.CreateAPIView):
    serializer_class=UserSerializer


class LoginView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    permission_classes=[]
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")

        print("Login Username :",username)
        print("Password Recieved:",bool(password))
        


        user=authenticate(username=username,password=password)
        print("AUTH RESULT:",user)
        if user is not None:
            token,created=Token.objects.get_or_create(user=user)
            return Response({'token':token.key,'role':user.role})  
        return Response({'error':'Invalid username or password'},

                        status=status.HTTP_401_UNAUTHORIZED) 




def home(request):
    return render(request, "index.html")


def register_page(request):
    return render(request, "register.html")


def rfqs_page(request):
    return render(request, "rfqs.html")


def rfq_details_page(request):
    return render(request, "rfq_details.html")


def create_rfq_page(request):
    return render(request, "create_rfqs.html")


def edit_rfq_page(request):
    return render(request, "edit_rfq.html")


def create_quotation_page(request):
    return render(request, "create_quotation.html")


def quotations_page(request):
    return render(request, "quotations.html")


def edit_quotation_page(request):
    return render(request, "edit_quotation.html")