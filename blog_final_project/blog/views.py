from django.http import HttpResponse


def index(request):
    return HttpResponse("Thoughts from the Peanut Gallery")
    