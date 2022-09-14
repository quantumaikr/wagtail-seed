import os

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


class GoogleLogin(SocialLoginView):
    authentication_classes = [] # disable authentication
    adapter_class = GoogleOAuth2Adapter
    callback_url = os.environ.get('FRONTEND_CALLBACK_URL', 'http://localhost:3000/login')
    client_class = OAuth2Client



class NaverLogin(SocialLoginView):
    authentication_classes = [] # disable authentication
    adapter_class = NaverOAuth2Adapter
    callback_url = os.environ.get('FRONTEND_CALLBACK_URL', 'http://localhost:3000/login')
    client_class = OAuth2Client


class KakaoLogin(SocialLoginView):
    authentication_classes = [] # disable authentication
    adapter_class = KakaoOAuth2Adapter
    callback_url = os.environ.get('FRONTEND_CALLBACK_URL', 'http://localhost:3000/login')
    client_class = OAuth2Client