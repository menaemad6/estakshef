from django.shortcuts import get_object_or_404, redirect, render 
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from .models import Site , Login
from django.core.paginator import Paginator


# Create your views here.






def about(request):
    return render(request, 'main/about.html' , {'site':Site.objects.all()})

# def sites(request):
#     sites = Site.objects.get(all)
#     context = {'site' : sites}
#     return render(request, 'main/sites.html' , context)

def main(request):
    return render(request, 'main/index.html' , {'site':Site.objects.all()})

def site_list(request):
    site_list = Site.objects.all()
    context = {'site' : site_list}
    return render(request , 'main/sites.html' , context)


def site_detail(request , slug):
    # prodcut_detail = Product.objects.get(PRDSLug=slug)
    site_detail = get_object_or_404(Site ,slug=slug )
    context = {'site' : site_detail}
    return render(request , 'main/site.html' , context)


# def site(request):
#     return render(request, 'main/site.html' , {'site':Site.objects.all()})

# def sites(self, request, *args, **kwargs):
#     return render(request, 'main/sites.html' , {'site':Site})






def addsite(request):
    if request.method == 'POST':
        
        names = request.POST.get('name')
        places = request.POST.get('place')
        descriptions = request.POST.get('description')
        rates = request.POST.get('rate')
        map_links = request.POST.get('map_link')
        lower_prices = request.POST.get('lower_price')
        higher_prices = request.POST.get('higher_price')
        contact_urls = request.POST.get('contact_url')
        contact_names = request.POST.get('contact_name')
        if len(request.FILES) != 0:
            first_images = request.FILES['first_image']
            second_images = request.FILES['second_image']
            third_images = request.FILES['third_image']
            fourth_images = request.FILES['fourth_image']

        
        durations = request.POST.get('duration')
        hourss = request.POST.get('hours')
        open_hourss = request.POST.get('open_hours')
        close_hourss = request.POST.get('close_hours')
        data = Site(name=names , contact_url=contact_urls , open_hours=open_hourss , close_hours=close_hourss ,  fourth_image=fourth_images , duration=durations , contact_name=contact_names , first_image=first_images , third_image=third_images ,  second_image=second_images ,    place=places , description=descriptions , rate=rates , map_link=map_links , lower_price=lower_prices , higher_price=higher_prices)
        
        data.save()
        return redirect(reverse('main-page:main'))
        
    return render(request, 'main/add-site.html')




def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    data = Login(email=email, password=password)
    data.save()

    
    return render(request, 'main/login.html' , {'site':Site.objects.all()})
