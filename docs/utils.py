import os.path

from django.conf import settings


def get_md_docs(name):

    path = os.path.join(settings.BASE_DIR.parent, "docs", "md", name)
    with open(path, "r") as f:
        data = f.read()
    return data

