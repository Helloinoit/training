from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from .models import Photo



def index(request):
    
    photo_list = Photo.objects.all()
    paginator = Paginator(photo_list, 20)
    
    page = request.GET.get('page')
    photo = paginator.get_page(page)
   
    return render(request, 'app1/index.html', {'photos':photo})
    

def detail(request, photo_id):

    photo = get_object_or_404(Photo, pk=photo_id)

      
    return render(request, 'app1/detail.html', {'photo':photo})
#    response = "You're looking at the results of photo %s."
#    return HttpResponse(response % photo_id)




