from datetime import  datetime

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class GoodsCategory(models.Model):
    """
    商品的多级分类
    """
    CATEGORY_TYPE = (
        (1,"一级类目"),
        (2,"二级类目"),
        (3,"三级类目"),
    )

    name = models.CharField(max_length=30,default='',verbose_name="类别名",help_text="类别名")
    code = models.CharField(default='',max_length=30,verbose_name="类别code",help_text="类别code")
    desc = models.TextField(default="",verbose_name="类别描述",help_text="类别描述")
    # 设置目录树的级别
    category_type = models.IntegerField(choices=CATEGORY_TYPE,verbose_name="类目级别",help_text="类目级别")
    parent_category = models.ForeignKey("self",null=True,blank=True,verbose_name="父类级别",help_text="父目录",
                                        related_name="sub_cat",on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False,verbose_name="是否导航",help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")


    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name
        db_table = "goods_category"

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    品牌名，某一个大类下的宣传商标
    """
    category = models.ForeignKey(GoodsCategory,related_name="brands",null=True,blank=True,verbose_name="商品类目",on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30,default="",verbose_name="商标名",help_text="商标名")
    desc = models.TextField(default="",max_length=200,verbose_name="商标描述",help_text="商标描述")
    # 将图片上传至media的brands目录下
    image = models.ImageField(max_length=200,upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "宣传品牌"
        verbose_name_plural = verbose_name
        db_table = "goods_category_brand"

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory,null=True,blank=True,verbose_name="商品类目",on_delete=models.DO_NOTHING)
    goods_sn = models.CharField(max_length=50,default="",verbose_name="商品唯一货号")
    name = models.CharField(max_length=300,verbose_name="商品名")
    click_num = models.IntegerField(default=0,verbose_name="点击数")
    sold_num = models.IntegerField(default=0,verbose_name="销售量")
    fav_num = models.IntegerField(default=0,verbose_name="收藏量")
    goods_num = models.IntegerField(default=0,verbose_name="库存量")
    market_price = models.FloatField(default=0,verbose_name="市场价")
    shop_price = models.FloatField(default=0,verbose_name="本店价格")
    goods_brief = models.TextField(max_length=400,verbose_name="商品简短描述")
    goods_desc = UEditorField(verbose_name=u"内容",imagePath="goods/images/",width=1000,height=300,
                             default="")
    ship_free = models.BooleanField(default=True,verbose_name="是否承担运费")
    goods_front_image = models.ImageField(upload_to="goods/images/",null=True,blank=True,verbose_name="封面图")
    goods_front_image_url = models.CharField(max_length=300,default="",verbose_name="封面图商品链接")
    is_new = models.BooleanField(default=False,verbose_name="是否是新品")
    is_hot = models.BooleanField(default=False,verbose_name="是否是新品")

    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods,verbose_name="商品",related_name="images",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="",verbose_name="图片",null=True,blank=True)
    image_url = models.CharField(max_length=300,null=True,blank=True,verbose_name="图片url")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    首页轮播商品图
    """
    goods = models.ForeignKey(Goods,verbose_name="商品",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="banner",verbose_name="轮播图片")
    index = models.IntegerField(default=0,verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name