# -*- coding: utf-8 -*-


from django import forms
from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext as _
from django.db.models import Q
from .widgets import MonthYearWidget, MonthYearField


class SplitDateForm(forms.Form):

    def __init__(self, *args, **kwargs):
        field_name = kwargs.pop('field_name')
        super(SplitDateForm, self).__init__(*args, **kwargs)

        self.fields['%s' % field_name] = MonthYearField(
            label='', widget=MonthYearWidget(
                attrs={'class': 'auto-width'}
                ),
            localize=True, required=False)


class SplitDateFilter(admin.filters.FieldListFilter):
    template = 'custom_filters/date_filter.html'

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg_since = '%s_' % field_path
        super(SplitDateFilter, self).__init__(
            field, request, params, model, model_admin, field_path)
        self.form = self.get_form(request)

    def choices(self, cl):
        return []

    def expected_parameters(self):
        return [self.lookup_kwarg_since + "0", self.lookup_kwarg_since + "1"]

    def get_form(self, request):
        return SplitDateForm(data=self.used_parameters,
                             field_name=self.field_path)

    def queryset(self, request, queryset):
        if self.form.is_valid():
            if self.form.cleaned_data.items():
                field, value = self.form.cleaned_data.items()[0]
                if value:
                    q = Q(**{"%s__gte" % field: unicode(value)})
                    return queryset.filter(q)

        return queryset


# register the filter
admin.filters.FieldListFilter.register(
    lambda f: isinstance(f, models.DateField), SplitDateFilter)
