from django.shortcuts import render
# from django.views.generic.base import View
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

from .models import Goods,GoodsCategory
from .serializers import GoodsSerializer,CategorySerializer
from .filters import GoodsFilter
# Create your views here.

# class GoodsListView(APIView):
#     """
#     list all goods
#     """
#     def get(self,request,format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(goods,many=True)
#         return Response(goods_serializer.data)
#
#     def post(self,request,format=None):
#         # 获取到前端传入的数据post get 等
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
# 最简版，ListAPIView继承了ListModelMixin和GenericAPIView
class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100

class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    商品列表页,分页，搜索，排序，过滤
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_class = GoodsFilter
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    filter_fields = ('name','shop_price')
    search_fields = ('name','goods_desc','goods_brief')
    ordering_fields = ('sold_num', 'shop_price')


    # def get_queryset(self):
    #     # 价格大于100的
    #     price_min = self.request.query_params.get('price_min',100)
    #     if price_min:
    #         self.queryset = Goods.objects.filter(shop_price__gt=price_min)
    #     return self.queryset


class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    # 获取一级分类，然后在序列化是将二级三级分类序列化至一级分类里面，类似googs中的序列化category
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer