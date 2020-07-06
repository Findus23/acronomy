from django.http import HttpResponseRedirect


class NoTrailingSlashMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        old_url: str = request.path
        if (
                old_url.endswith('/')
                and not old_url.startswith("/admin")
                and not old_url.startswith("/__debug__")
                and not old_url.startswith("/account")
                and not old_url.startswith("/api")
                and not old_url == "/"
        ):
            new_url = old_url[:-1]
            return HttpResponseRedirect(new_url)

        return self.get_response(request)
