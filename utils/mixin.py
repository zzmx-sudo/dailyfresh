from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    """给原视图加登录验证"""
    @classmethod
    def as_view(cls, **initkwargs):  # 这里的as_view方法需要去看子类继承的View类中定义的as_view方法需要的参数
        # 子类继承LoginRequiredMixin类时，按多继承执行父类方法的先后顺序，当子类调用as_view方法时，会先在LoginRequiredMixin类中找as_view方法
        # 当LoginRequiredMixin类中也需要调用父类的as_view方法时，会去子类继承的其他父类种去找as_view方法
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
