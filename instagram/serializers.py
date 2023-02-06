from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post


# 중요!
# Serializer는 기본적으로 Form 데이터가 포함된 JSON 문자열을 생성해준다.

# Serializer 생성자의 첫번째 인자는 instance

# code line in here

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

class PostSerializer(serializers.ModelSerializer):
    # 이거를 이렇게 해주는 이유는 models에서 따로 정의는 되지 않았지만 사용해줘야할 때
    # 일종의 임시방편으로써 작동하게끔 써주는 것 같다.
    author_username = serializers.ReadOnlyField(source = 'author.username')
    # 이렇게도 사용이 가능하다.
    # author_email = serializers.ReadOnlyField(source = 'author.email')

    # 위의 클래스로 정의해준 것으로써 2개의 필드 인자를 이렇게 사용해줄 수도 있다.
    # author = AuthorSerializer()

    class Meta:
        model = Post
        fields = [
            'pk',
            # 'author',
            # 'author_email',
            'author_username',
            'message',
            'created_at',
            'updated_at'
        ]