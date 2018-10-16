"""vue_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,include,re_path

import xadmin
from  vue_shop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token
from goods.views import GoodsListViewSet,CategoryViewSet

router = DefaultRouter()

router.register('goods',GoodsListViewSet,base_name='goods')
# # 将get请求和list绑定，类似apiview中的get函数
# goods_list = GoodsListViewSet.as_view({
#     'get':'list'
# })

router.register('categorys',CategoryViewSet,base_name='categorys')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),

    # rest framework登录调试
    path('api-auth/', include('rest_framework.urls')),

    re_path('media/(?P<path>.*)',serve,{"document_root":MEDIA_ROOT}),

    path('ueditor/', include('DjangoUeditor.urls')),

    # #商品列表页,用来router就不需要用此法
    # path('goods/',goods_list,name="goods-list"),
    # 只需要将router在此配置，就可实现get和list，create,post的绑定
    path('',include(router.urls)),
    path('docs/',include_docs_urls(title='幕学生鲜')),

    # drf自带的token认证模式
    path('api-token-auth/',obtain_auth_token),
    # jwt的token认证接口
    path('login/',obtain_jwt_token),
]