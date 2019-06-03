from django import template
from datetime import datetime, date, time


register = template.Library()


@register.filter
def format_date(value, in_date):
    time_now = datetime.now()
    time_now = time_now.timestamp()
    if time_now - in_date < 600:
        value = 'Только что'
    elif ((time_now - in_date) < 86400) and ((time_now - in_date) > 600):
        value = '{} часов назад'.format(int((time_now - in_date)//3600))
        if int((time_now - in_date)/3600) < 1:
            value = 'Менее часа назад'
    elif (time_now - in_date) > 86400:
        value = datetime.fromtimestamp(in_date)
        value = '%s-%s-%s' % (value.year, value.month, value.day)
    return value

@register.filter
def format_score(value, in_score):
    if in_score < -5:
        value = 'Все плохо'
    elif (in_score > -5) and (in_score <= 5):
        value = 'Нейтрально'
    elif in_score > 5:
        value = 'Хорошо'
    return value


@register.filter
def format_num_comments(value, in_num):
    if in_num == 0:
        value = 'Оставьте комментарий'
    elif (in_num > 0) and (in_num <= 50):
        value = in_num
    elif in_num > 50:
        value = '50+'
    return value


@register.filter
def format_selftext(value, count):
    in_text = value.split()
    value = ' '.join(in_text[:count]) + '...' + ' '.join(in_text[-count:])
    return value



