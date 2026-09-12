from rest_framework import serializers
from .models import RFQ,Quatation,User
from django.utils import timezone


class RFQSerializers(serializers.ModelSerializer):
    buyer = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = RFQ
        fields = "__all__"

class QuatationSerializers(serializers.ModelSerializer):
    
    supplier = serializers.PrimaryKeyRelatedField(read_only=True)
    is_selected = serializers.BooleanField(read_only=True)


    class Meta:
        model = Quatation
        fields = "__all__"
        read_only_fields = ["supplier"]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0."
            )
        return value

    def validate_delivery_time(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Delivery time must be greater than 0 days."
            )
        return value

    def validate(self, data):
       rfq = data.get(
        "rfq",
        self.instance.rfq if self.instance else None
        )
       supplier = self.context["request"].user

       if rfq and rfq.dead_line < timezone.localdate():
          raise serializers.ValidationError(
            "The deadline for this RFQ has already passed."
        )

       existing_quotation = Quatation.objects.filter(
        rfq=rfq,
        supplier=supplier
    )

       if self.instance:
          existing_quotation = existing_quotation.exclude(
            pk=self.instance.pk
        )

       if existing_quotation.exists():
          raise serializers.ValidationError(
            "You have already submitted a quotation for this RFQ."
        )

       return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

