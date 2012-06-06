from django.contrib.syndication.views import Feed
from blogsource.models import Blog

class LatestEntriesFeed(Feed):
    title = "mirka's photoblog"
    link = "/gwhitehawk/"
    description = "the better ones of my photos"
   
    def items(self):
        return Blog.objects.order_by('-posted')[:5]

    def item_title(self, item):
        result = "/gwhitehawk" + item.get_absolute_url()
        return result

    def item_description(self, item):
        return item.body
