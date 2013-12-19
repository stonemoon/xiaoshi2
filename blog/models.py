from django.db import models
from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse

class Blog(models.Model):
	usr=models.ForeignKey(User)
	name=models.CharField(max_length=50)		
	def __unicode__(self):
		return self.name

class Post(models.Model):
	blog=models.ForeignKey(Blog)
	title = models.CharField(max_length=50)
#	slug = models.SlugField(uniq=True, max_length=255)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.name

#	class Meta:
#		ordering = ['-created']
#	def get_absolute_url(self):
#		return reverse('blog.views.post', args=[self.slug])
	
class Tag(models.Model):
	post = models.ForeignKey(Post)
	tag = models.CharField(max_length=50)
	def __unicode__(self):
		return self.tag

class Timestamp(models.Model):
	post = models.ForeignKey(Post)
	time_modified = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.time_modifie
# Create your models here.
