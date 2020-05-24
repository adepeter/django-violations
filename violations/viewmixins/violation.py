class BaseViolationViewMixin:

    """
    This viewmixin supplies every get_form_kwargs needed for initialization
    Override methods here for further customization
    """

    def get_form_kwargs(self):
        """Add request and object keywords to BaseViolationForm()"""
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.add_request()
        kwargs['object'] = self.add_object()
        return kwargs

    def add_request(self):
        """:return: request"""
        return self.request

    def add_object(self, obj=None):
        "Object to be use in form"
        """
        ::param obj
        :return obj
        """
        return obj if obj is not None else self.get_object()
