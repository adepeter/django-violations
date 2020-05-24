from django import forms


class RulesModelMultipleChoiceFieldWithId(forms.ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return '# %(rule_id)d %(rule_name)s' % {'rule_id': obj.id, 'rule_name': obj.name}
