from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
from django.http import HttpResponse





def display_topics(request):
    LTO=Topic.objects.all()
    LTO=Topic.objects.filter(topic_name='cricket')
    #LTO=Topic.objects.get(topic_name='cricket')

    d={'LTO':LTO}
    return render(request,'display_topics.html',d)
    

def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(topic_name='cricket')
    LWO=Webpage.objects.filter(topic_name='volley ball')
    LWO=Webpage.objects.exclude(topic_name='volley ball')
    LWO=Webpage.objects.all()[3::]
    LWO=Webpage.objects.all()[::-1]
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.all().order_by('-name')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    LWO=Webpage.objects.all()

    LWO=Webpage.objects.filter(name__in=['kutty','pooja'])
    
    LWO=Webpage.objects.filter(name__regex='R\w+')

    LWO=Webpage.objects.filter(Q(name='poorna') | Q(url__startswith='https'))
    LWO=Webpage.objects.filter(Q(name='kutty') & Q(url__startswith='https'))

    LWO=Webpage.objects.all()
  
    
   
    

    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)


def display_accessrecods(request):
    LAO=AccessRecords.objects.all()
    LAO=AccessRecords.objects.filter(date='2002-03-27')
    LAO=AccessRecords.objects.filter(date__gt='2002-03-27')
    LAO=AccessRecords.objects.filter(date__lt='2002-03-27')
    LAO=AccessRecords.objects.filter(date__lte='2002-03-27')
    LAO=AccessRecords.objects.filter(date__year='2023')
    LAO=AccessRecords.objects.filter(date__month='03')
    LAO=AccessRecords.objects.filter(date__day='20')
    LAO=AccessRecords.objects.filter(date__year__gte='2002')
    LAO=AccessRecords.objects.filter(date__year__lte='2002')
    LAO=AccessRecords.objects.filter(date__day__gt='20')


    d={'LAO':LAO}
    return render(request,'display_accessrecods.html',d)



def update_webpage(request):

   
    Webpage.objects.filter(name='lucky').update(url='https://LK.com')
    Webpage.objects.filter(name='poorna').update(url='https://pp.com')
    Webpage.objects.filter(topic_name='cricket').update(url='https://IndianTeam.in')
    Webpage.objects.filter(name='Dhoni MSD').update(url='https://MSD.in')

    #error Webpage.objects.filter(name='vicky').update(topic_name='BCCI Cricket')
    Webpage.objects.filter(name='vicky').update(topic_name='cricket')
    Webpage.objects.update_or_create(name='kutty',defaults={'url':'http://ABCDE.com'})
    
    Webpage.objects.update_or_create(topic_name='volley ball',defaults={'url':'http://VB.com'})
    Webpage.objects.update_or_create(name='prathap',defaults={'url':'http://ABCDE.com'})
    CTO=Topic.objects.get(topic_name='cricket')
    
    
    Webpage.objects.update_or_create(name='vicky',defaults={'topic_name':CTO})
    Webpage.objects.update_or_create(name='mouni',defaults={'topic_name':CTO,'url':'http://MN.com'})

    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)

def delete_webpage(request):

    Webpage.objects.filter(name='prathap').delete()

    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)





















