from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from db.base_model import BaseModel


# Create your models here.
class User(AbstractUser,BaseModel):
    """用户模型类"""

    # def generate_active_token(self):
    #     """生成用户签名字符串"""
    #     serializer = Serializer(settings.SECRET_KEY, 3600)
    #     info = {'confirm':self.id}
    #     token = serializer.dumps(info)
    #     return token.decode()

    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class AddressManager(models.Manager):
    """地址模型管理器类"""
    # 1.改变原有查询的结果集
    # 2.封装方法：用于操作模型类对应的数据表（增删改查）
    def get_default_address(self, user):
        """获取用户的默认收货地址"""
        try:
            # address = Address.objects.get(user=user, is_default=True)
            # 这里的self表示models.Manager类的对象，也就是objects，所以Address.objects直接用self代替
            address = self.get(user=user, is_default=True)
        except self.model.DoesNotExist:
            # 不存在默认收货地址时
            address = None

        return address


class Address(BaseModel):
    """地址模型类"""
    user = models.ForeignKey('User', verbose_name='所属账户', on_delete=models.CASCADE)
    receiver = models.CharField(max_length=20,  verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收货地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系方式')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    # 自定义一个模型管理器对象
    objects = AddressManager()

    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name
