from django.contrib.syndication.views import Feed
from blogsource.models import Blog

class LatestEntriesFeed(Feed):
    title = "Latest articles"
    link = "/latest/"
    
    def items(self):
        return Blog.objects.order_by('-posted')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body
