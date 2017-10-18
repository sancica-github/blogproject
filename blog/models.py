from django.db import models
#下面是一个坑，还需要进行填补，为什么导入User
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse

# Create your models here.
class Category(models.Model):
 	#django会默认创建一个id列
 	name = models.CharField(max_length = 100)
 	def __str__(self):
 		return self.name

class Tag(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name

#下面构造了一个编辑器
#该装饰器用于兼容python2
@python_2_unicode_compatible
class Post(models.Model):
	#文章标题
	title = models.CharField(max_length = 70)
	#文章正文
	body = models.TextField()
	#创建时间&最后修改时间
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()

	#文章摘要，设置blank=true，可设置为空
	abstract = models.CharField(max_length = 200, blank = True)

	#文章与分类和标签的对应
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank = True)
	#作者
	author = models.ForeignKey(User)
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk':self.pk})

	#定义内部类，规定该类的内部的一些属性，下面指定默认的排序方式
	class Meta:
		ordering = ['-created_time', 'title']