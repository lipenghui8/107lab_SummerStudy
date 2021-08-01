import functools

sorted_ignore_case = functools.partial(sorted, key=lambda item: item.lower())
sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])