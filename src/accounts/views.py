from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login as auth_login
from .models import Profile
from .forms import UserForm , ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# This Is Function About User Register (SignUp)
def signup(request):

    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()

            username =  form.cleaned_data.get('username')
            password =  form.cleaned_data.get('password1')

            user = authenticate(username=username,password=password)
            auth_login(request,user)
            
            return redirect('products:product_list')
    else :
            form = UserCreationForm()

    context = {'form':form}
    return render(request,'registration/signup.html',context)

# This Function About User Profile By Slug
@login_required(login_url='login')
def profile(request,slug):
    profile = get_object_or_404(Profile,slug=slug)
    context = {'profile':profile}
    return render(request,'accounts/profile.html',context)


# This Is Function About User Can Edit Profile
@login_required(login_url='login')
def edit_profile(request,slug):
    
    my_profile   = Profile.objects.get(user=request.user)
    user_form    =  UserForm(instance=request.user)
    profile_form =  ProfileForm(instance=my_profile)

    if request.method == 'POST':

           user_form     =  UserForm(request.POST,instance=request.user)
           profile_form  =  ProfileForm(request.POST,request.FILES,instance=my_profile)

           if user_form.is_valid() and profile_form.is_valid():
               user_form.save()
               new_profile_form = profile_form.save(commit=False)
               new_profile_form.user = request.user
               new_profile_form.save()
               return redirect('accounts:profile',slug=slug)
    
           else :
                user_form    =  UserForm(request.POST,instance=request.user)
                profile_form =   ProfileForm(request.POST,request.FILES,instance=my_profile)

    context = {'user_form':user_form,'profile_form':profile_form}
    return render(request,'accounts/edit_profile.html',context)