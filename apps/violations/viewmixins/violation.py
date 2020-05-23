class BaseViolationViewMixin:

    def get_form_kwargs(self):
        kwargs = super().self.get_form_kwargs()
        kwargs['request'] = self.request
        kwargs['object'] = self.get_object()
