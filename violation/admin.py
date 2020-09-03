from django.contrib import admin

from violation.models import Rule, Violation


class RuleViolationInline(admin.StackedInline):
    model = Rule.violations.through


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    radio_fields = {'category': admin.HORIZONTAL}
    list_display = ['name', 'category', 'short_rule']
    list_filter = ['category']
    search_fields = ['name', 'category', 'description']
    ordering = ['name', 'category']
    save_on_top = True

    def short_rule(self, obj):
        return obj.description[:20]

    short_rule.short_description = 'Description'


@admin.register(Violation)
class ViolationAdmin(admin.ModelAdmin):
    readonly_fields = ['violator', 'created', 'modified']
    list_display_links = ['id', 'rules_violated']
    radio_fields = {'status': admin.HORIZONTAL}
    list_display = [
        'id',
        'reported_by',
        'violator',
        'item_of_violation_category',
        'item_of_violation',
        'object_id',
        'rules_violated',
        'date_reported',
        'status',
        'is_violated',
        'last_modified'
    ]
    ordering = [
        'reported_by',
        'violator',
        'is_violated',
        'status'
    ]
    list_filter = [
        'reported_by',
        'violator',
        'status',
        'is_violated'
    ]
    list_editable = ['is_violated', 'status']
    date_hierarchy = 'created'
    filter_horizontal = ['rules']
    list_per_page = 20

    def item_of_violation_category(self, obj):
        return obj.content_type

    item_of_violation_category.short_description = 'Item category'

    def item_of_violation(self, obj):
        return obj.content_object

    item_of_violation.short_description = 'Item of violation'

    def date_reported(self, obj):
        return obj.created

    date_reported.short_description = 'Date reported'

    def last_modified(self, obj):
        return obj.modified

    date_reported.short_description = 'Last action'

    def rules_violated(self, obj):
        rules = obj.rules.all()
        return ('%s' % ', '.join([rule.name for rule in rules]))

    short_description = 'Violated rules'

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.list_display
        return []
