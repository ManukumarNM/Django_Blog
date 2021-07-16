from django.forms import fields
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from .forms import AuthorUpdateForm, UserUpdateForm, ContactForm


#About function for User/Author 
def about(request):
    return render(request, 'about.html')


#User Contact function
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            body = {
                'name' : form.cleaned_data['name'],
                'email' : form.cleaned_data['email'],
                'mobile' : form.cleaned_data['mobile'],
                'message' : form.cleaned_data['message'],
            }
            message_email = "\n".join(str(body.values())) #Combine and Format data using join method with "\n" or ","
        
            if request.user.is_authenticated:
                subject = str(request.user) + "Post/Blog Inquiry"
            else:
                subject = "Visitor's message"

            try:
                send_mail(subject, message_email, 'email', ['To_Email']) #Replace this with your mail ID's
            except BadHeaderError:   # BadHeaderError for security reasons
                return HttpResponse('Invalid Header Found.')
            messages.info(request, 'Mail sent Successfully')
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form':form})


#User Register function for Posting a Post
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Alreday Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, "User Created Successfully")
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

        return redirect('/')

    else:
        return render(request, 'register.html')

    
#Login function for Users
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('post_form')
        else:
            messages.info(request, 'Invalid Credentials Username or Password is incorrect')
            return redirect('login')

    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')

# class AuthorDetailView(generic.DetailView):
#     model = Author


#Update and Delete function for Author/User Posts
@login_required
def author_form(request, *args, **kwargs):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        author_image_form = AuthorUpdateForm(request.POST, request.FILES, instance=request.user.author)
        if  user_form.is_valid() and author_image_form.is_valid():
            user_form.save()
            author_image_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('author_form')

    else:
        user_form = UserUpdateForm(instance=request.user)
        author_image_form = AuthorUpdateForm(instance=request.user.author)

    context = {
        'user_form': user_form,
        'author_image_form': author_image_form,
    }

    return render(request, 'author_form.html', context)


