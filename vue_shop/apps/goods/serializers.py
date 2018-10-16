from rest_framework import serializers

from .models import Goods,GoodsCategory,GoodsCategoryBrand

class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    sub_cat =CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategoryBrand
        fields = '__all__'
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
#
#     def create(self, validated_data):
#         """
#         接收前端传入的数据并序列化
#         :param validated_data:
#         :return:
#         """
#         return Goods.objects.create(**validated_data)

class GoodsSerializer(serializers.ModelSerializer):
    # 对于外键关联的序列化,直接在此实例化该外键实例的序列化，覆盖默认的category
    category = CategorySerializer()
    class Meta:
        model = Goods
        # fields = ('name','click_num','market_price','add_time')
        fields = '__all__'