from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Request

def home(request):
    all_requests = Request.objects.all()
    list_requests = list()

    for item in all_requests:
        list_requests.append(item)

    return render(request, 'board/home.html', {'list_requests': list_requests})

def preview(request, pk):
    page = Request.objects.get(pk=pk)
    return render(request, 'board/preview.html', {'page': page})

def new_request(request):
    if request.method == 'POST':

        title = request.POST['title']
        description = request.POST['description']
        user = User.objects.get(id=1)
        event_date = request.POST['eventdate']
        event_address = request.POST['eventaddress']
        city = request.POST['eventcity']
        contact = request.POST['email']
        type = request.POST['type']

        new = Request.objects.create(

            title=title,
            description=description,
            event_date=event_date,
            event_address=event_address,
            city=city,
            contact=contact,
            coordinator=user,
            requester=user,
            type=type
        )

        return redirect('home')


    return render(request, 'board/new_request.html')

#
# def new_topic(request):
#     user = User.objects.get(id=1)
#     if request.method == 'POST':
#         form = NewRequestForm(request.POST)
#         if form.is_valid():
#             new_object = Request(
#                 title=form.cleaned_data.get['title'],
#                 description=form.cleaned_data.get['description'],
#                 event_date=form.cleaned_data.get['event_date'],
#                 event_address=form.cleaned_data.get['event_address'],
#                 city=form.cleaned_data.get['city'],
#                 contact=form.cleaned_data.get['contact'],
#                 type=form.cleaned_data.get['type'],
#                 coordinator=user,
#                 requester=user
#             )
#
#             new_object.save()
#
#         return redirect('home')
#     else:
#         form = NewRequestForm()
#     return render(request, 'board/form_request.html', {'form' : form})

