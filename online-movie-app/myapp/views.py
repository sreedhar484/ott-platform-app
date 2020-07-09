from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . forms import ExtendedForm,ProfileForm,ExtendedUpdateForm,ProfileUpdateForm
from . models import Movies,Slide,App

# Create your views here.
def index(request):
    a = App.objects.all()
    return render(request,'index.html',{'a':a})

def signup(request):
    if request.method=='POST':
        form = ExtendedForm(request.POST)
        form1 = ProfileForm(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            profile = form1.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('/')
    else:
        form = ExtendedForm()
        user_profile = ProfileForm()
        return render(request,'register.html',{'form':form,'form1':user_profile})

def allmovie(movie,l):
    foryou = list(set([i for i in movie for j in  str(i.select_movie_types_liked).split(',') if j.casefold() in l]))
    telugu = list(set([i for i in movie if i.language.casefold() =='telugu']))
    tamil =list(set([i for i in movie if i.language.casefold()=='tamil']))
    hindi = list(set([i for i in movie if i.language.casefold()=='hindi']))
    english = list(set([i for i in movie if i.language.casefold()=='english']))
    return (foryou,telugu,tamil,hindi,english)
    

def home(request):
    a = App.objects.all()
    movie = Movies.objects.all()
    slide = Slide.objects.all()
    slide = [i for i in slide]
    l =[i.casefold() for i in str(request.user.profile.m_type).split(',')]
    movie = allmovie(movie,l)
    return render(request,'main.html',{'foryou':movie[0],'telugu':movie[1],'tamil':movie[2],'hindi':movie[3],'english':movie[4],'slide1':slide[:2],'slide2':slide[2:4],'slide3':slide[4:6],'slide4':slide[6:8],'slide5':slide[8:10],'a':a})

def h(request,id):
    a = App.objects.all()
    movie = Movies.objects.all()
    slide = Slide.objects.all()
    slide = [i for i in slide]
    l =[i.casefold() for i in str(request.user.profile.m_type).split(',')]
    movie = allmovie(movie,l)
    return render(request,'main.html',{'foryou':movie[0],'telugu':movie[1],'tamil':movie[2],'hindi':movie[3],'english':movie[4],'slide1':slide[:2],'slide2':slide[2:4],'slide3':slide[4:6],'slide4':slide[6:8],'slide5':slide[8:10],'a':a})

def movieview(request,id):
    movie = Movies.objects.get(id=id)
    all_movie = Movies.objects.all()
    l =[i.casefold() for i in str(movie.select_movie_types_liked).split(',')]
    all_movie = list(set([i for i in all_movie for j in  str(i.select_movie_types_liked).split(',') if j.casefold() in l and i.id!=movie.id]))
    return render(request,'main2.html',{'name':movie,'movie':all_movie})

def fullmovieview(request,id):
    movie = Movies.objects.get(id=id)
    return render(request,'play.html',{'name':movie})

def fulltrailerview(request,id):
    movie = Movies.objects.get(id=id)
    return render(request,'play_trailer.html',{'name':movie})

def profile(request):
    return render(request,'profile.html')

def pro(request,id):
    return render(request,'profile.html')

def search(request):
    all_movie = Movies.objects.all()
    return render(request,'search.html',{'movie':all_movie})

def searchres(request,id):
    all_movie = Movies.objects.all()
    return render(request,'search.html',{'movie':all_movie})

def srh(string):
    movie = Movies.objects.all()
    l=string.casefold()
    k = []
    k.extend([i for i in movie if i.name.casefold() in l])
    k.extend([i for i in movie if i.language.casefold() in l])
    k.extend([i for i in movie if i.hero_name.casefold() in l])
    k.extend([i for i in movie if i.heroin_name.casefold() in l])
    k.extend([i for i in movie if i.director_name.casefold() in l])
    k.extend([i for i in movie for j in  str(i.select_movie_types_liked).split(',') if j.casefold() in l])
    k = list(set(k))
    return k

def searchform(request):
    string = request.POST['string']
    result = srh(string)
    return render(request,'search.html',{'movie':result})

def searchform1(request,id):
    string = request.POST['string']
    result = srh(string)
    return render(request,'search.html',{'movie':result})

def editprofile(request):
    if request.method=='POST':
        form = ExtendedUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('profile')
        else:
            return redirect('editprofile')
    else:
        form = ExtendedUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        return render(request,'profile_update.html',{'form':form,'form1':profile_form})

def editpro(request,id):
    if request.method=='POST':
        form = ExtendedUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('profile')
        else:
            return redirect('editprofile')
    else:
        form = ExtendedUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        return render(request,'profile_update.html',{'form':form,'form1':profile_form})
