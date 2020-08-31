from django import forms
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ImproperlyConfigured
from django.db import NotSupportedError
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _

from violation.fields.rule import RulesModelMultipleChoiceField
from violation.models import Rule, Violation


class BaseViolationForm(forms.ModelForm):
    """ This is the base form for further customization """
    categories = None
    queryset = None
    dont_repeat_rules = False

    """
        This is the base form to display list of rules in a category
        1. ::categories: rules in specified categories to display
        2. ::queryset: rules queryset to display.
        3. ::dont_repeat_rules: allow whether to show already violated rule by an object
        or not. If set to False, rules already violated by an item will still be made available
        for other users to select.
    """

    rules = RulesModelMultipleChoiceField(queryset=None)

    class Meta:
        model = Violation
        fields = ['rules']

    def __init__(self, *args, **kwargs):
        self.object = kwargs.pop('object')
        self.request = kwargs.pop('request')
        self.rules_queryset = self.get_queryset()
        if self.dont_repeat_rules:
            self.rules_queryset = self.unique_rules_queryset()
        super().__init__(*args, **kwargs)
        self.fields['rules'].widget = forms.CheckboxSelectMultiple()
        self.fields['rules'] = RulesModelMultipleChoiceField(
            queryset=self.rules_queryset,
            widget=forms.CheckboxSelectMultiple
        )

    def get_queryset(self):
        if self.categories is None:
            if self.queryset is not None:
                queryset = self.queryset
                if isinstance(self.queryset, QuerySet):
                    queryset = queryset.all()
                else:
                    raise NotSupportedError('%s is actually not a QuerySet' % self.queryset)
            else:
                raise ImproperlyConfigured('self.categories or self.queryset is needed to load this form')
        else:
            queryset = Rule.objects.filter(
                category__in=[category for category in self.categories]
            )
        return queryset

    def clean_rules(self):
        """
        A validation check which ensures a user/item doesnt
        report an item more than ones
        """
        cleaned_rules = self.cleaned_data['rules']
        check_spam_violations = self.check_spam_rules(cleaned_rules, self.request.user)
        if check_spam_violations:
            raise forms.ValidationError(
                _('A rule cannot be reported twice for violation'),
                code='multiple_violations'
            )
        return cleaned_rules

    """
    This method is called to ensure a report action is not repeated twice.
    """

    def check_spam_rules(self, rules, user):
        violations = Violation.objects.filter(
            content_type=ContentType.objects.get_for_model(self.object),
            object_id=self.object.id,
            reported_by=user,
            rules__in=rules
        )
        return violations.exists()

    def unique_rules_queryset(self):
        """This method is called only when self.dont_repeat_rules is set."""
        qs = self.get_queryset()
        return qs.exclude(
            violations__isnull=False,
            violations__status__in=[
                Violation.VIOLATION_STATUS_PENDING,
                Violation.VIOLATION_STATUS_ACCEPTED
            ],
            violations__content_type=ContentType.objects.get_for_model(self.object),
            violations__object_id=self.object.id,
            violations__reported_by=self.request.user,
            violations__is_violated__isnull=True
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.reported_by = self.request.user
        instance.content_type = ContentType.objects.get_for_model(self.object)
        instance.object_id = self.object.id
        if commit:
            instance.save()
        return instance


class ViolationForm(BaseViolationForm):
    """
    This is just a sample form.
    Free to inherit it if you just want simple violation rules display
    """
    categories = ['general']