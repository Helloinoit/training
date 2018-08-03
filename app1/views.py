from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.urls import reverse


from .models import Photo, Profile
from .forms import DecsriptionForm, DocumentForm



def get_description(request, pk):
    
    photo=get_object_or_404(PhotoInstance, pk = pk)
    print("you are here")

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DescriptionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(photo)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            photo.photo_text = form.cleaned_data[description]
            photo.save()
            return HttpResponseRedirect('app1/home/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DescriptionForm()


    photo.photo_text = form.cleaned_data[description]
    
    return render(request, 'detail.html', {'form': form, 'photo':photo})





def index(request):
    
    photo_list = Photo.objects.all()
    paginator = Paginator(photo_list, 20)
    
    page = request.GET.get('page')
    photo = paginator.get_page(page)
   
    return render(request, 'app1/index.html', {'photos':photo})

def user(request, user_id):

    photo_list = Photo.objects.all()
    print(photo_list)
    paginator = Paginator(photo_list, 20)
    
    page = request.GET.get('page')
    photo = paginator.get_page(page)
      
    return render(request, 'app1/photos.html', {'photos':photo})
    

def detail(request, photo_id):

    photo = get_object_or_404(Photo, pk=photo_id)

      
    return render(request, 'app1/detail.html', {'photo':photo})


def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.profile = self.request.user
            form.save()
            return HttpResponseRedirect((reverse('home')))
    else:
        form = DocumentForm()
    return render(request, 'app1/model_form_upload.html', {'form': form})








