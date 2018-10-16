from django_filters import rest_framework as filters
from django.db.models import Q

from goods.models import Goods


class GoodsFilter(filters.FilterSet):
    """
    商品的过滤器
    """

    pricemin = filters.NumberFilter(field_name='shop_price',lookup_expr='gte',help_text='大于等于本店价格')
    pricemax = filters.NumberFilter(field_name='shop_price',lookup_expr='lte',help_text='小于等于本店价格')
    # 类似django中的查询需要用到icontains包含查询
    # name = filters.CharFilter(field_name="name",lookup_expr='icontains')
    top_category = filters.NumberFilter(method='top_category_filter',field_name='category')

    def top_category_filter(self,queryset,name,value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields =['pricemin','pricemax','name']