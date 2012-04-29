from django.db import models
from django.db.models import permalink

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blogsource.Category')
	
    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('blogsource.views.view_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('blogsource.views.view_category', None, { 'slug': self.slug })

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Blog)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60])) 

class Image(models.Model):
    post = models.ForeignKey(Blog)
    image = models.ImageField(upload_to='img', max_length=500)

class Link(models.Model):
    post = models.ForeignKey(Blog)
    link = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.link[:100]))
