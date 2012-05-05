from django import template
register = template.Library()

@register.filter(name='filterlinks')
def filterlinks(all_links, post):
    filtered = [];
    for link in all_links:
        if (link.post == post):
            filtered.append(link)
    return filtered 
