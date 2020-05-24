from django.views.generic.edit import CreateView

from violation.forms.violation import ViolationForm
from violation.viewmixins.violation import BaseViolationViewMixin


class BaseViolationView(BaseViolationViewMixin, CreateView):
    """
    To use this view, you must defined a form_class
    that inherits from either BaseViolationForm or ViolationForm
    """
