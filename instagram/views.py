from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .serializers import PostSerializer
from .models import Post

# Create your views here.
# generics.ListCreateAPIView으로 인자를 받게되면 post_list에 사용해야할 2개의 분기를 대신해줄 수 있다.
# class PublicPostListAPIView(generics.ListCreateAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# 클래스 기반 뷰
# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
        
# public_post_list = PublicPostListAPIView.as_view()

# 함수 기반 뷰
@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)

# 이것이 바로 아래의 정의된 2개의 함수를 대신할 viewsets 클래스다.
class PostViewSet(ModelViewSet):
    # 원하는 데이터 범위 (여기서는 all로써 '전체'를 의미하며 사용하지만)
    # get, filter등을 사용하여서 부분적으로 구별해 줄 수도 있다.
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs):
        # print 비추천, logger 추천
        # 테스트로 출력해주는 print들
        print('request.body: ', request.body)
        print('request.POST: ', request.POST)
        return super().dispatch(request, *args, **kwargs)
    

# 바로 아래의 2개 함수에 관하여 대체해줄 수 있는 것이 rest_framework의 viewsets이다.
# def post_list(request):
#     # 2개 분기
#     pass

# def post_detail(request, pk):
#     # request.method => 3개 분기
#     pass

# 데코레이터 사용 방법1
# @csrf_exempt
# def post_list(request):
#     pass

# 데코레이터 사용 방법2
def post_list(request):
    pass

post_list = csrf_exempt(post_list)
