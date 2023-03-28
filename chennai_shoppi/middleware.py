from django.shortcuts import redirect, resolve_url

class ChennaiShoppiMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(request.path_info, request.user.is_authenticated)
        if request.user.is_authenticated:
            if request.path_info in ["/login/", '/register/']:
                return redirect('/')
        else:
            if request.path_info in ["/login/", "/register/"]:
                return
            return redirect(resolve_url('login'))
