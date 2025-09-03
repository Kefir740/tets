import django_filters
from .models import Tasks
from datetime import datetime, timedelta
from django.utils.dateparse import parse_date, parse_datetime


class TasksFilter(django_filters.FilterSet):
    deadline = django_filters.CharFilter(method='deadline_filter')

    class Meta:
        model = Tasks
        fields = ["deadline"]

    def deadline_filter(self, queryset, name, value):
        datetime_value = parse_datetime(value)
        date_value = parse_date(value)

        if datetime_value:
            return queryset.filter(deadline=datetime_value)

        elif date_value:
            start = datetime.combine(date_value, datetime.min.time())
            end = start + timedelta(days=1)
            return queryset.filter(deadline__gte=start, deadline__lt=end)
        else:
            return queryset  # некорректное значение — ничего не фильтруем

