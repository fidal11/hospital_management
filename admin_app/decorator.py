from django.shortcuts import redirect



def auth_admin(func):
    def wrapper(request, *args, **kwargs):
        if 'admin' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('myhospital_app:home')
    return wrapper