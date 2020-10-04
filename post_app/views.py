from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView,FormView
# Create your views here.
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import * 
from django.http import JsonResponse, Http404
from django.contrib.auth.forms import AuthenticationForm


class PostLists(ListView):
    
    template_name = 'index.html'
    paginate_by = 100
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status = 1)


class PostDetails(DetailView):
    template_name = 'post_detail.html'
    model = Post
    slug_field = 'slug'

# class LoginView(View): 
    
#     def get(self,request):        
#         form = LoginForm()
#         return render(request,'new_login.html',{'form':form})

#     def post(self,request):

#         form = LoginForm(request.POST)

#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')       

#             user = authenticate(email=email, password=password)       
#             print(user,'##')

#             if user is not None:
#                 print( login(request,user),'$$')
#                 login(request,user)
#                 return redirect('/')        
#         else:        
#             print(form.errors,'#')
#         return render(request,'new_login.html',{'form':form})

# class RegisterUser(View):
# Use SignUpform as form insted of model form to use this view.
#     template_name = 'new_register.html'        

#     def get(self,request):
#         return render(request,self.template_name,{'form':SignUpForm})

#     def post(self,request):
#         form = SignUpForm(request.POST)
#         if form.is_valid():            
#             username = form.cleaned_data.get('username')                  
#             first_name = form.cleaned_data.get('first_name')
#             last_name = form.cleaned_data.get('last_name')
#             password = form.cleaned_data.get('password')
#             email = form.cleaned_data.get('email')
#             user = User.objects.create(username = username,first_name=first_name,last_name=last_name,email=email)       
        
#         return render(request,self.template_name,{'form':form})

class RegisterUser(CreateView):
    template_name = 'new_register.html'
    form_class =  SignUpForm    
    success_url = '/' 

    def form_valid(self,form):
        user = form.save()       
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return super().form_valid(form)

    def form_invalid(self,form):
        # import pdb;pdb.set_trace()
        print(self,'$')
        if 'abc' not in form.data.get('username'):
            raise ValidationError('User name not found')
        return super().form_invalid(form)


class CreatePost(CreateView):
    form_class = CreatPostForm    
    template_name = 'create_post.html'
    success_url = '/'


class LoginView(View): 
    
    def get(self,request):        
        form = LoginForm()
        return render(request,'new_login.html',{'form':form})

    def post(self,request):

        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')       

            user = authenticate(email=email, password=password)       
            print(user,'##')

            if user is not None:
                print( login(request,user),'$$')
                login(request,user)
                return redirect('/')        
        else:        
            print(form.errors,'#')
        return render(request,'new_login.html',{'form':form})