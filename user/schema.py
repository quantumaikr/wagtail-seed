from ninja import ModelSchema

from user.models import User


# 사용자 정보 스키마
class UserSchema(ModelSchema):
    
    class Config:
        model = User
        model_fields = [
            'id', 'username', 'email', 'phone',
        ]
