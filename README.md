# DJANGO-VIOLATION v1.0.0

## Description

Description Django-violations is a very simple app which serves the purpose of violation. It can easily be plugged into any django app of your choice with just little line of code/customization but with robust function.

## Installation

pip install django-violation

## Features

django-violation is shipped with basic features that is needed for reporting / flagging an item, post, image, user, thread etc as invalid.

Among some of its basic features are:

- An item cannot be submitted for violation by same person.
- Built-in django admin panel.
- Ability to redisplay rules that have been submitted by various users.
- Can be plugged with any django app.
- Highly customizable 100%

**Future implementations**

- Adding a UI interface.

## Requirements

- Python >= 3.5
- Django >= 2.2

## Usage

1. Add package to list of your already available django apps in settings.py

Code:

```
INSTALLED_APPS = [

...

'django_violations',

]
```

2. Next is to write a view code to load object you will like report.

   For Lovers of class views, just import `BaseViolationViewMixin`

   `from django_violation.viewmixins import BaseViolationMixin`

   Inherit the view class and supply other `CreateView` parameters other than form_class.

   Do something similar to this

   ```
   from django_violation.views.violation import BaseViolationView
   
   class ThreadViolationView(BaseViolationView):
       template_name = ''
   ```

   

Function base view user can follow this code logic

```
from django.shortcuts import render, get_object_or_404

from django_violation.forms.violation import ViolationForm

from .models import Thread # where this a an imaginary thread you want to report

TEMPLATE_URL = 'apps/threads'

def report_thread(request, pk):
    template_name = f'{TEMPLATE_URL}/report_thread.html'
    thread = get_object_or_404(Thread, pk=pk)
    form_kwargs = {
        'request': request,
        'object': thread,
    }
    if request.method == 'POST':
        form = ViolationForm(data=request.POST, **form_kwargs)
        if form.is_valid():
            form.save()
    else:
        form = ViolationForm(**form_kwargs)
    context = {
        'form': form,
        'thread': thread
    }
    return render(request, template_name, context=context)
```

> Most importantly, it is worth noting that request and object keywords must be passed to form in your view

For further customization, see project source code in github.

Limitations

Lack of links and UI.

## Versioning

SemVer is for versioning. For the versions available, see the tags on this repository.

## License

This work uses MIT license

## Acknowledgement

- A big heart to Sammy Bala.
- Thanks to Stephen Efe.