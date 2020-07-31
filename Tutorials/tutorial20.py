# _args and _kwargs
# In list or tuple value are added then retrieve by using *args and **kwargs
# Sequence of argument are (normal_var, *args, **kwargs)
# *args and **kwargs are optional
# We can define any keyword of *args or **kwargs
# *args and **kwargs used for retrieve list or dictionary or tuple
def fuargs(normal, *args, **kwargs):
    """any list retrieve in *args or **kwargs it will convert to Tuple format"""
    print(normal)
    for item in args:
        print(item)
    print('\nNow I would like to introduce some of our skills')
    for key, value in kwargs.items():
        print(key, value)

har = ['Harry', 'Rohan', 'Sandip','Tom']
normal = 'I am a normal argument and the students are : '
kws = {'1': 'Python', '2': 'Javascript', '3': 'Flask'}
fuargs(normal, *har, **kws)
