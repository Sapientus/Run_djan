from django import template

register = template.Library()


def tags(quote_tags):
    return ', '.join([str(name) for name in quote_tags.all()])

def authors(author):
    return ', '.join([str(name) for name in author.all()])

register.filter('tags', tags)
register.filter('authors', authors)
