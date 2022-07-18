ignores = ['apps.views.Application', ]


def preprocessing_filter_spec(endpoints):
    filtered = []
    for (path, path_regex, method, callback) in endpoints:
        a = ".".join([callback.cls.__module__, callback.cls.__name__])
        if a not in ignores:
            filtered.append((path, path_regex, method, callback))
    return filtered
