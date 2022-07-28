from django.conf import settings


EXCLUDE_PATH = settings.SPECTACULAR_SETTINGS["EXCLUDE_PATH"]
ignores = ['apps.views.Application', ]


def preprocessing_filter_spec(endpoints):
    filtered = []
    for (path, path_regex, method, callback) in endpoints:
        a = ".".join([callback.cls.__module__, callback.cls.__name__])
        if a not in ignores and path not in EXCLUDE_PATH:
            filtered.append((path, path_regex, method, callback))
    return filtered
