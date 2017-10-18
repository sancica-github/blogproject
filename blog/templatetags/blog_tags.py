from django import template
from ..models import Post, Category

register = template.Library()

#将函数get_recent_posts装饰为simple_tag，就可以在模板中使用{% get_recent_posts %}
@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
	return Post.objects.dates('created_time','month', order='DESC')

@register.simple_tag
def get_categories():
	return Category.objects.all()