from django.dispatch import Signal

report_handler = Signal(providing_args=['violation', 'violator'])