from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from app.forms import *
from app.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

def base(request):
    return render(request, 'base.html')

def home(request):
    if request.method == 'POST':
        entered_mail = request.POST.get('uem')
        SFO = Signup_Form()
        home_dic = {'entered_mail': entered_mail, 'SFO': SFO}
        return render(request, 'signup_page.html', home_dic)
    return render(request, 'home.html')

@login_required
def profile(request):
    username = request.session.get('username')
    UO = User.objects.get(username=username)
    d = {'UO':UO}
    return render(request, 'profile.html',d)


def main_page(request):
    if request.session.get('username'):
        username=request.session.get('username')
        # MSO = Movies_Series.objects.values_list('flyer')
        MSO = Movies_Series.objects.all()
        trending = MSO[:10]
        blockbuster = MSO[10:20]
        popular = MSO[20:len(MSO)]
        # print(trending)
        # print(MSO)
        d={'username':username,
            'MSO':MSO,
            'trending':trending,
            'blockbuster':blockbuster,
            'popular':popular,
        }
        return render(request,'main_page.html',d)
    return render(request, 'signin_page.html')

def tvshows(request):
    if request.session.get('username'):
        SO = Movies_Series.objects.filter(ms_type='seasonal')
        award = SO[len(SO)-10:]
        trending = SO[len(SO)-20:]
        tvdrama = SO[len(SO)-30:]
        d = {
            'SO':SO,
            'award':award,
            'trending':trending,
            'tvdrama':tvdrama
        }
        return render(request,'tvshows_page.html',d)
    return render(request, 'signin_page.html')
    

def movies(request):
    if request.session.get('username'):
        SO = Movies_Series.objects.filter(ms_type='single')
        popular = SO[len(SO)-30:]
        trending = SO[len(SO)-20:]
        romantic = SO[len(SO)-10:]
        d = {
            'SO':SO,
            'popular':popular,
            'trending':trending,
            'romantic':romantic
        }
        return render(request,'movies_page.html',d)
    return render(request, 'signin_page.html')
    

def new_popular(request):
    if request.session.get('username'):
        MSO = Movies_Series.objects.all()
        trending = MSO[:10]
        blockbuster = MSO[10:20]
        popular = MSO[20:len(MSO)]
        
        M_SO = Movies_Series.objects.filter(ms_type='single')
        mpopular = M_SO[len(M_SO)-30:]
        mtrending = M_SO[len(M_SO)-20:]
        mromantic = M_SO[len(M_SO)-10:]
        
        SO = Movies_Series.objects.filter(ms_type='seasonal')
        award = SO[len(SO)-10:]
        strending = SO[len(SO)-20:]
        tvdrama = SO[len(SO)-30:]
        d={
            'MSO':MSO,
            'trending':trending,
            'blockbuster':blockbuster,
            'popular':popular,
            'mpopular':mpopular,
            'mtrending':mtrending,
            'mromantic':mromantic,
            'award':award,
            'strending':strending,
            'tvdrama':tvdrama,
            
            }
        return render(request,'new_popular_page.html',d)
    return render(request, 'signin_page.html')
    

def children(request):
    CO = Movies_Series.objects.filter(age_limit='kids')
    popular = CO[:10]
    CO1 = Movies_Series.objects.filter(age_limit='kids', ms_type='seasonal')
    everyone = CO1[len(CO1)-10:]
    CO2 = Movies_Series.objects.filter(age_limit='kids', ms_type='single')
    funny = CO2[len(CO2)-10:]
    d = {
        'popular':popular,
        'everyone':everyone,
        'funny':funny,
    }
    return render(request,'children.html',d)

def signup(request):
    SFO = Signup_Form()
    sd = {'SFO': SFO}
    if request.method == 'POST':
        SFD = Signup_Form(request.POST)
        
        if SFD.is_valid():

            # un = SFD.cleaned_data.get('username')
            # if len(un)>10:
            #     messages.error(request,'Length should be less than 10 characters')
            #     return redirect('signup')
            
            NSSFD = SFD.save(commit=False)
            saved_password = SFD.cleaned_data['password']
            NSSFD.set_password(saved_password)
            NSSFD.save()
            # return HttpResponse('Successfull')
            # d = {'SFD': SFD}
            return render(request, 'signin_page.html')
        else:
            return HttpResponse('<script>alert("Invalid Details")</script>')

    return render(request, 'signup_page.html',sd)
    
def signin(request):
    if request.method == 'POST':
        
        siun = request.POST.get('siun')
        sipw = request.POST.get('sipw')
        
        #authentication
        AUO = authenticate(username = siun, password = sipw)
        if AUO:
            #active user checking and login request
            if AUO.is_active:
                login(request, AUO)
                request.session['username'] = siun
                return HttpResponseRedirect(reverse('main_page'))
            else:
                return HttpResponse('<script>alert("Not a Active User")</script>')
        else:
            return HttpResponse('<script>alert("Invalid Details")</script>')
        
        # return HttpResponse('Further Process')
    return render(request,'signin_page.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def change_password(request):
    if request.method == 'POST':
        pw = request.POST.get('pw')
        un = request.session.get('username')
        UO = User.objects.get(username=un)
        UO.set_password(pw)
        UO.save()
        return render(request, 'signin_page.html')
        # return HttpResponse('<script>alert("Password change Successful")</script>')
    return render(request, 'change_password_page.html')

def reset_password(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        rpw = request.POST.get('rpw')
        LUO = User.objects.filter(username=un)
        if LUO:
            if pw==rpw:
                UO = LUO[0]
                UO.set_password(pw)
                UO.save()
                return render(request, 'signin_page.html')
            else:
                return HttpResponse('<script>alert("Password Mis-Match")</script>')
        else:
            return HttpResponse('<script>alert("Invalid username")</script>')
            
    return render(request, 'reset_password_page.html')