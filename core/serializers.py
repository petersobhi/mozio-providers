from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from rest_framework_gis.serializers import GeometryField
from phonenumber_field.serializerfields import PhoneNumberField

from .models import Provider, ServiceArea

User = get_user_model()


class ProviderLoginSerializer(LoginSerializer):
    # Remove username field from login serializer
    username = None


class ProviderRegisterSerializer(RegisterSerializer):
    username = None
    email = serializers.EmailField(required=False)
    name = serializers.CharField(required=True, write_only=True)
    phone_number = PhoneNumberField(required=True, write_only=True)
    language = serializers.CharField(help_text=_("Language code in ISO format"))
    currency = serializers.CharField(help_text=_("Currency code in ISO format"))

    def get_cleaned_provider_data(self):
        return {
            'name': self.validated_data.get('name', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'language': self.validated_data.get('language', ''),
            'currency': self.validated_data.get('currency', ''),
        }

    def create_provider(self, user, validated_data):
        """
        Create the `Provider` instance, given the validated data.
        """
        Provider.objects.create(user=user, **validated_data)

    def custom_signup(self, request, user):
        self.create_provider(user, self.get_cleaned_provider_data())


class ProviderSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='provider.name', max_length=50)
    phone_number = PhoneNumberField(source='provider.phone_number')
    language = serializers.CharField(source='provider.language', max_length=3)
    currency = serializers.CharField(source='provider.currency', max_length=3)

    class Meta:
        model = User
        fields = ('email', 'name', 'phone_number', 'language', 'currency')

    def update(self, instance, validated_data):
        provider_data = validated_data.pop('provider', {})
        name = provider_data.get('name', None)
        phone_number = provider_data.get('phone_number', None)
        language = provider_data.get('language', None)
        currency = provider_data.get('currency', None)

        user = super(ProviderSerializer, self).update(instance, validated_data)

        provider = user.provider
        if provider_data:
            if name:
                provider.name = name
            if phone_number:
                provider.phone_number = phone_number
            if language:
                provider.language = language
            if currency:
                provider.currency = currency
            provider.save()
        return instance


class ServiceAreaSerializer(serializers.ModelSerializer):
    polygon = GeometryField(help_text=_("A polygon in GeoJSON, WKT EWKT or HEXEWKB format"))
    provider = serializers.CharField(source='provider.name', read_only=True)

    class Meta:
        model = ServiceArea
        fields = '__all__'
