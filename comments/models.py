from django.db import models
from django.utils.six import python_2_unicode_compatible
# Create your models here.
class Comment(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=225)
	url = models.URLField(blank=True)
	text = models.TextField()
	created_time = models.DateTimeField(auto_now_add=True)

	#引入另一个app的数据库表
	post = models.ForeignKey('blog.Post')

	def __str__(self):
		return self.text[:20]
		