====================
DJANGO-VIOLATION APP
====================
***********
Description
***********
Django-violations is a very simple app which serves the purpose of violation.
It can easily be plugged into any django app of your choice with just little line
of code/customization but with robust function.

************
Requirements
************
Python >= 3.0
Django >= 2.1

Installation
------------
``>>>pip install django-violation``

Usage
-----
A. Settings.py
++++++++++++++
Add django_violations to list of installed_apps in your settings.PY
INSTALLED_APPS = [
    ...
    'django_violations'
]

B. VIEWS.PY
++++++++++++
``">>from .forms import MyCustomViolationForm"``
# where MyCustomViolationForm will be created later

However, you must pass 'request' and 'object' to subclass of form
(in or case, we are using MyCustomViolationForm)
Example of Implementation
FBV
def report_item(request, id):
    .....
    post = get_object_or_404(ItemToReport, id=id)
    form = MyCustomViolationForm(request=request, object=post)

C. FORMS.PY
++++++++++++
1. Subclass ViolationForm, a module of django_violations
``>> from django_violations.forms import ViolationForm``
2. Set either "categories" or "queryset" on this subclass
from django_violation.forms import ViolationForm

class MyOwnViolationForm(ViolationForm):
    categories = ['user', 'forum'] #where forum and general are categories

or Using queryset to return QuerySet for rules.
queryset = YourRuleMixinSubclass.objects.filter(xxxxx)
If you subclass BaseRuleMixin, then this method will be best
However if you choose to use Preset Rule model, then categories is best.


For further customization, this app ships with a signal report_hander
>> from django_violations.signals import report_handler

Feel comportable to look at the source code for more customization.