from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import (
    JWTSerializer,
    UserDetailsSerializer,
)
try:
    from allauth.account import app_settings as allauth_settings
    from allauth.account.adapter import get_adapter
except ImportError:
    raise ImportError('allauth needs to be added to INSTALLED_APPS.')

from django.utils.translation import gettext_lazy as _
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    phone = serializers.CharField(required=False, max_length=11, allow_null=True, allow_blank=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['phone'] = self.validated_data.get('phone', '')

        return data

    def validate_phone(self, phone):
        if phone and User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError(
                _('A user is already registered with this phone number'),
            )

        return phone


class CustomJWTSerializer(JWTSerializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        user = super().get_user(obj)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta:
        model = User
        
        extra_fields = [
            'id', 'username', 'email', 'phone', 
            'groups',
        ]

        fields = ('pk', *extra_fields)
