from django import template

register = template.Library()


@register.filter(name="in_group")
def in_group(user, group_name):
    if user.groups.filter(name=group_name).exists():
        return True
    else:
        return False
