from django.shortcuts import render

# Create your views here.

from django.views.decorators.http import require_GET
from django.http import HttpResponse

@require_GET
def favicon(request):
    print(request)
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")