d = {
    'name': 'zhangsan'
}
s = {
    'age': 11
}
s = dict(d, **s)
print(s)
