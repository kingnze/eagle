from django.shortcuts import get_object_or_404, render,redirect
from .models import Room,Meeting,Spa,Gallery,Ourservice,Ourservice1,Whoweare,Blog,Contact,Dining,Ourinfo,Service,About,Comfort,Booking
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):   
    rooms = Room.objects.all()[:4]
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:3]
    gimg = Gallery.objects.all()[:6]
    dining = Dining.objects.all()[:1]
    spa = Spa.objects.all()[:1]
    meeting = Meeting.objects.all()[:1]
    ourservice = Ourservice.objects.all()[:3]
    ourinfo = Ourinfo.objects.all()[:1]
    whoweare = Whoweare.objects.all()[:1]
    ourservice_1 = Ourservice1.objects.all()[:1]
    comfort = Comfort.objects.all()
    
    context = { 
     'rooms': rooms,
     'ourinfo': ourinfo,
     'blog': blog,
     'gimg':gimg,
     'dining':dining,
     'spa':spa,
     'meeting':meeting,
     'ourservice':ourservice,
     'whoweare':whoweare,
     'ourservice_1':ourservice_1,
     'comfort':comfort
    }



    return render(request,'eagles/index.html',context)

def rooms(request):   
    rooms = Room.objects.all()

    paginator = Paginator(rooms, 9)
    page = request.GET.get('page')
    paged_rooms = paginator.get_page(page)
    
    context = {
        'rooms': paged_rooms,
    }

    return render(request,'eagles/rooms.html',context)

def room(request, room_id):   
    room = get_object_or_404(Room, pk=room_id)
    
    context = {
        'room': room,
    }

    return render(request,'eagles/room.html',context)

def service(request):   
    service = Service.objects.all()[:1]
    dining = Dining.objects.all()[:1]
    spa = Spa.objects.all()[:1]
    meeting = Meeting.objects.all()[:1]
    rooms = Room.objects.all()[:3]
    whoweare = Whoweare.objects.all()[:1]
    ourservice_1 = Ourservice1.objects.all()[:1]
    ourservice = Ourservice.objects.all()[:3]
    context = { 
     'service':service,
     'dining':dining,
     'spa':spa,
     'meeting':meeting,
     'rooms': rooms,
     'ourservice':ourservice,
     'whoweare':whoweare,
     'ourservice_1':ourservice_1,
     

    }

    return render(request,'eagles/service.html',context)

def about(request): 
    about = About.objects.all()[:1] 
    ourinfo = Ourinfo.objects.all()[:1] 
    whoweare = Whoweare.objects.all()[:1] 
    context = { 
        'about': about,
        'ourinfo': ourinfo,
        'whoweare':whoweare,
    }

    return render(request,'eagles/about.html',context)

def blog(request):   
    blog = Blog.objects.order_by('-date_posted').filter(published=True)

    paginator = Paginator(blog, 9)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    
    context = {
        'blog': paged_blog,
    }
    return render(request,'eagles/blog.html',context)

def blogdetail(request, slug_id):
    blogdetail = Blog.objects.filter(slug=slug_id).first()
    rooms = Room.objects.all()[:9]
    context = {
        'post': blogdetail,
        'rooms': rooms,
        
    }
    return render(request,'eagles/blogdetail.html',context)      

def gallery(request):   
    gimg = Gallery.objects.all()

    context = {
        'gimg':gimg
    }
    return render(request,'eagles/gallery.html',context)

def dining(request):   
    dining = Dining.objects.all()
    context = {
        'dining':dining
    }

    return render(request,'eagles/dining.html',context)

def spa(request):   
    spa = Spa.objects.all()
    context = {
        'spa':spa
    }
    return render(request,'eagles/spa.html',context)

def meeting(request):   
    meeting = Meeting.objects.all()
    context = {
        'meeting':meeting
    }

    return render(request,'eagles/meeting.html',context)

def ourservice(request):   
    ourservice = Ourservice.objects.all()

    context = {
        'ourservice':ourservice
    }
    return render(request,'eagles/ourservice.html',context)

def whoweare(request):   
    whoweare = Whoweare.objects.all()

    context = {
        'whoweare':whoweare
    }
    return render(request,'eagles/whoweare.html',context)

def whowearedetail(request,slug_id):   
    whowearedetail = Whoweare.objects.filter(slug=slug_id).first()
    rooms = Room.objects.all()[:9]

    context = {
        'post':whowearedetail,
        'rooms': rooms,
    }
    return render(request,'eagles/whowearedetail.html',context)

def ourservice_1(request):   
    ourservice_1 = Ourservice1.objects.all()

    context = {
        'ourservice_1':ourservice_1
    }

    return render(request,'eagles/ourservice_1.html',context)

def contact(request):   
    if request.method == 'POST':
    
      try:
          connect = Contact(fname=request.POST['fname'],lname=request.POST['lname'],phone=request.POST['phone'],email=request.POST['email'],message=request.POST['message'])
          messages.success(request,f"{request.POST['fname']} Sent Successfully!!")

          connect.save()
          return redirect('contact')

      except Exception as e:
          messages.error(request,f"Something went wrong...")

    return render(request,'eagles/contact.html')

@login_required   
def bookings(request):   
    if request.method == 'POST':
    
      try:
          bookings = Booking(room=request.POST['room'],
          check_in=request.POST['check_in'],
          check_out=request.POST['check_out'],
          gender=request.POST['gender'],
          address=request.POST['address'],
          adults=request.POST['adults'],
          children=request.POST['children'])
          messages.success(request,f"{request.POST['room']} Booked Successfully!!")

          bookings.save()
          return redirect('bookings')

      except Exception as e:
          messages.error(request,f"Something went wrong...")

    return render(request,'eagles/bookings.html')
