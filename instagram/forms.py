from django.forms import ModelForm
from .models import Post


# 기본원리 중요!
# forms.py는 기본적으로 Form 태그가 포함된 HTML을 생성해준다.

# form 생성자의 첫번째 인자는 data

class PostForm(ModelForm):
    class Meta:
        models = Post
        fields = '__all__'