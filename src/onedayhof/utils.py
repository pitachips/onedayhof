import os
from django.utils import timezone
from uuid import uuid4


def random_name_upload_to(instance, filename):
    app_label = instance.__class__._meta.app_label
    cls_name = instance.__class__.__name__.lower()
    ymd_path = timezone.now().strftime('%Y/%m/%d')
    name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return os.path.join(app_label, cls_name, ymd_path, name + extension)
