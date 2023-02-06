from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# 이게 2개의 URL을 만들어 준다.
router.register('post', views.PostViewSet)
# 여기에는 urls가 리스트 형태로 들어있다. 그러니깐, 바로 위에서 register로 추가된 것도 생각해야하는 부분이다.
# router.urls

urlpatterns = [
    # 이렇게 해주면 mapping까지 끝난거라고 한다.
    # 흠.. 그나저나 이건 왜 문자열화시키지 않고 써줘도 되는거지?
    path('', include(router.urls)),
    path('public/', views.public_post_list)
]
