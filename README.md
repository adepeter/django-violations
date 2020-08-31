# django-violation

## Description

Description Django-violation is a very simple app which serves the purpose of violation. It can easily be plugged into any django app of your choice with just little line of code/customization but with robust function.

## Installation

```
>> pip install django-violation
```

## Features

django-violation is shipped with basic features that is needed for reporting / flagging an item, post, image, user, thread etc as invalid.

Among some of its basic features are:

- An item cannot be submitted for violation by same person.
- Built-in django admin panel.
- Ability to redisplay rules that have been submitted by various users.
- Can be plugged with any django app.
- Highly customizable.

**Future implementations**

- Adding a UI interface.

## Requirements

- Python >= 3.7
- Django >= 3.1

## Usage

1. Add package to list of your already available django apps in settings.py

   Code:

```
INSTALLED_APPS = [

...

'violation',

]
```
2. Run database migration to sync preset violation that the app ships with.
  Code: 

  ```
  >> python manage.py migrate
  ```

  

3. Login your project admin panel and you should see VIOLATION added menu.

4. Next is to write a view code to load object you will like report.

   ### CBV

   For Lovers of class views, who want to customize to the core,  import `BaseViolationViewMixin`

   i.e. `from violation.viewmixins.violation import BaseViolationMixin`

   Inherit the view class and supply other `CreateView` parameters other than form_class.

   Do something similar to this

   ```
   from violation.views.violation import BaseViolationView
   
   class ThreadViolationView(BaseViolationView):
       model = YourModelClass
    template_name = ''
   ```

   It's worth noting that `BaseViolationView` ancestors are `BaseViolationMixin` and `CreateView`

   ### FBV

   Function base view user can follow this code logic

   ```
   from django.shortcuts import render, get_object_or_404
   
   from violation.forms.violation import ViolationForm
   
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

> Most importantly, it is worth noting that request and object keywords must be passed to form in your view.

For further customization, see project source code in [github](http://github.com/adepeter/django-violations).

## Limitations

- Lack of links and UI.
- Limited info on how to fully use.

## Versioning

SemVer is the versioning style utilized for this app. For the versions available, see the tags on this repository [releases](https://github.com/adepeter/django-violations/releases).

## License

This work uses MIT license
