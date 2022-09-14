from ninja import NinjaAPI

from user.api import user_router


api = NinjaAPI()

# 라우터 등록
api.add_router('/user/', user_router)