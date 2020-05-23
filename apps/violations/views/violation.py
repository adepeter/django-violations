from django.views.generic.edit import CreateView

from ..forms.violation import ViolationForm
from ..viewmixins.violation import BaseViolationViewMixin


class BaseViolationView(BaseViolationViewMixin, CreateView):
    form_class = ViolationForm
