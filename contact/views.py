from django.shortcuts import render

# Create your views here.


def contacts(request):
    """ A view for the contact page """

    return render(request, 'contact/contacts.html')
