from django.shortcuts import render, get_object_or_404

from .forms import ThreadReportForm

from .models import Thread

TEMPLATE_URL = 'apps/threads'


def read_thread(request, pk):
    template_name = f'{TEMPLATE_URL}/read_thread.html'
    thread = get_object_or_404(Thread, pk=pk)
    context = {
        'thread': thread
    }
    return render(request, template_name, context=context)


def report_thread(request, pk):
    template_name = f'{TEMPLATE_URL}/report_thread.html'
    thread = get_object_or_404(Thread, pk=pk)
    form_kwargs = {
        'request': request,
        'object': thread,
    }
    if request.method == 'POST':
        form = ThreadReportForm(data=request.POST, **form_kwargs)
        if form.is_valid():
            form.save()
    else:
        form = ThreadReportForm(**form_kwargs)
    context = {
        'form': form,
        'thread': thread
    }
    return render(request, template_name, context=context)
