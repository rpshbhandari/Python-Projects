# filepath: d:\Examination\CBE\apps\home\templatetags\custom_filters.py
from django import template
from django.forms.boundfield import BoundField
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='add_class')
def add_class(field: BoundField, css_class: str) -> BoundField:
    """
    Adds a CSS class to a form field widget.
    """
    try:
        existing_classes = field.field.widget.attrs.get('class', '')
        field.field.widget.attrs['class'] = f"{existing_classes} {css_class}".strip()
        return field
    except AttributeError as e:
        raise ValueError("Invalid field passed to add_class filter.") from e