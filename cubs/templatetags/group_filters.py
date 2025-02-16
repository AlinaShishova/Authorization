from django import template

register = template.Library()

@register.filter
def in_group(user, group_name):
    """
    Фильтр возвращает True, если пользователь состоит в группе с именем group_name,
    иначе False.
    """
    return user.groups.filter(name=group_name).exists()
