from django import template

register = template.Library()

@register.inclusion_tag('utils/javascript_include_tag.html', takes_context=True)
def javascript_include_tag(context, name):
    context['javascript_scriptname'] = name
    return context


@register.inclusion_tag('utils/stylesheet_include_tag.html', takes_context=True)
def stylesheet_include_tag(context, name):
    context['stylesheet_filename'] = name
    return context


@register.inclusion_tag('utils/image_tag.html', takes_context=True)
def image_tag(context, src, id = None, classname = None):
    context['image_src'] = src
    context['image_id'] = id
    context['image_class'] = classname
    return context
