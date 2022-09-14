
from ninja import Router
from typing import List

from .schema import *
from .models import User

# router
user_router = Router(tags=["사용자 관련 API"])


# 로그인 사용자 정보 조회
@user_router.get(
    '/',
    response=List[UserSchema], 
    summary="사용자 목록 조회", 
)
def get_user_list(request):
    user_list = User.objects.all()
    return user_list
