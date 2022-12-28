from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import login , authenticate
from .models import Profile
from .forms import UserForm , ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.



def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username , password=password)
            login(request,user)

            print(request.user)
            return redirect('accounts:profile')
    else:
        form = UserCreationForm

    context = {
        'form' : form ,
    }

    return render(request , 'registration/signup.html' , context)


@login_required(login_url='/accounts/login/')
def profile(request , slug):
    profile = get_object_or_404(Profile , slug=slug)
    context = {'profile' : profile}
    return render(request , 'profile.html' , context)

@login_required(login_url='/accounts/login/')
def profiles(request):
    return render(request , 'my-profile.html')






def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect('accounts:profile')

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request,'edit-profile.html',{'userform':userform , 'profileform':profileform})



def change_password(request , slug):
    profile = get_object_or_404(Profile , slug=slug)

    if request.method =='POST' :
        password_form = PasswordChangeForm(request.user ,request.POST)
        if password_form.is_valid():
            password_form.save()
            return redirect('/')

    else:
        password_form = PasswordChangeForm(request.user)


    context = {
        'password_form' : password_form ,
        'profile' : profile ,
    }

    return render(request,'change_password.html' , context)




# @login_required
# def editprofile(request):
#     if request.method == 'POST':
    
#         names = request.POST.get('name')
#         emails = request.POST.get('email')
#         phones = request.POST.get('phone')
#         countrys = request.POST.get('country')

#         data = Profile(name=names , email=emails, phone=phones, country=countrys )
#         data.save()
#         return redirect(reverse('accounts:profile'))
        
#     return render(request, 'edit-profile.html')
