import datetime
from django import forms
from django.forms import fields


class MonthYearWidget(forms.MultiWidget):
    """
   A widget that splits a date into Month/Year with selects.
   """
    def __init__(self, attrs=None):
        months = (
            ('', 'Month'),
            ('', '---'),
            ('01', 'Jan (01)'),
            ('02', 'Feb (02)'),
            ('03', 'Mar (03)'),
            ('04', 'Apr (04)'),
            ('05', 'May (05)'),
            ('06', 'Jun (06)'),
            ('07', 'Jul (07)'),
            ('08', 'Aug (08)'),
            ('09', 'Sep (09)'),
            ('10', 'Oct (10)'),
            ('11', 'Nov (11)'),
            ('12', 'Dec (12)'),
        )

        year_now = int(datetime.date.today().year)
        year_digits = range(year_now, year_now + 10)
        years = [(year, year) for year in year_digits]
        years.insert(0, ("", "---"))
        years.insert(0, ("", "Year"))

        widgets = (forms.Select(attrs=attrs, choices=months), forms.Select(
            attrs=attrs, choices=years))
        super(MonthYearWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.month, value.year]
        return [None, None]

    def render(self, name, value, attrs=None):
        try:
            value = datetime.date(month=int(
                value[0]), year=int(value[1]), day=1)
        except:
            value = ''

        return super(MonthYearWidget, self).render(name, value, attrs)


class MonthYearField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        """
        Have to pass a list of field types to the constructor, else we
        won't get any data to our compress method.
        """

        all_fields = (
            fields.CharField(),
            fields.CharField(),
        )
        super(MonthYearField, self).__init__(all_fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            s = data_list[0]
            month = int(s) if s else 1
            s = data_list[1]
            year = int(s) if s else datetime.date.today().year

            return datetime.date(year=year, month=month, day=1)
        return None
