from django.db import models

# Create your models here.

# 导入内建的User模型。
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
from PIL import Image
# 引入imagekit
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# 新闻数据模型
class NewsPost(models.Model):
    # 新闻作者。参数 on_delete 用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 新闻标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=100)

    # 新闻标题图
    avator = ProcessedImageField(
        upload_to='news/%Y%m%d',
        processors=[ResizeToFit(width=400)],
        format='JPEG',
        options={'quality': 100},
    )

    # 新闻正文。保存大量文本使用 TextField
    body = models.TextField()

    # 新闻创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    # 新闻更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    # 保存时处理图片
    def save(self, *args, **kwargs):
        # 调用原有的 save() 的功能
        new = super(NewsPost, self).save(*args, **kwargs)

        # 固定宽度缩放图片大小
        if self.avator and not kwargs.get('update_fields'):
            image = Image.open(self.avator)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.avator.path)

        return new

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
    	# ordering 指定模型返回的数据的排列顺序
    	# '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
    	# return self.title 将文章标题返回
        return self.title