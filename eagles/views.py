from django.shortcuts import get_object_or_404, render,redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.conf import settings
from . models import *
from .form import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    rooms = Room.objects.all()[:4]
    banner = Banner.objects.all()
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
     'banner': banner,  
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

def addtocart(request,id):
    # get the
    cart_room = Room.objects.get(id=id)
    # check if cart exists
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart_item = Cart.objects.get(id=cart_id)
        this_room_in_cart = cart_item.cartroom_set.filter(room=cart_room)
        # # assign cart to user
        if request.user.is_authenticated and request.user.customer:
                cart_item.customer = request.user.customer
                cart_item.save()
        # # end
        # checking if item exist in cart
        if this_room_in_cart.exists():
            cartroom = this_room_in_cart.last()
            cartroom.quantity += 1
            cartroom.subtotal += cart_room.price
            cartroom.save()
            cart_item.total += cart_room.price
            cart_item.save()
            messages.success(request, 'Item increase in cart')
        # new item in cart
        else:
            cartroom = CartRoom.objects.create(
            cart=cart_item, room=cart_room, rate=cart_room.price, quantity=1, subtotal=cart_room.price)
            cart_item.total += cart_room.price
            cart_item.save()
            messages.success(request, 'New room added to cart')

    else:
        cart_item = Cart.objects.create(total=0)
        request.session['cart_id'] = cart_item.id
        cartroom = CartRoom.objects.create(cart=cart_item, room =cart_room, rate = cart_room.price, quantity=1, subtotal=cart_room.price)
        cart_item.total += cart_room.price
        cart_item.save()
        messages.success(request, 'New Item to cart')
    return redirect('bookings')

def myCart(request):
    rooms = Room.objects.all()
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
        # assign to cart
        if request.user.is_authenticated and request.user.customer:
            cart.customer = request.user.customer
            cart.save()
        # end
    else:
        cart = None
    context = {
        'cart':cart,
        'rooms':rooms
    }
    return render(request, 'eagles/mycart.html',context)

def manageCart(request,id):
    action = request.GET.get('action')
    cart_obj = CartRoom.objects.get(id=id)
    cart = cart_obj.cart

    if action == 'inc':
        cart_obj.quantity += 1
        cart_obj.subtotal += cart_obj.rate
        cart_obj.save()
        cart.total += cart_obj.rate
        cart.save()
        messages.success(request, 'Item quantity increase in cart')

    elif action == 'dcr':
        cart_obj.quantity -= 1
        cart_obj.subtotal -= cart_obj.rate
        cart_obj.save()
        cart.total -= cart_obj.rate
        cart.save()
        messages.success(request, 'Item quantity decrease in cart')

        if cart_obj.quantity == 0:
            cart_obj.delete()
    elif action == 'rmv':
        cart.total -= cart_obj.subtotal
        cart.save()
        cart_obj.delete()
        messages.success(request, 'Item remove in cart')

    else:
        pass
    return redirect('bookings')

def emptyCart(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
        # assign to cart
        if request.user.is_authenticated and request.user.customer:
            cart.customer = request.user.customer
            cart.save()
        # end
        cart.cartroom_set.all().delete()
        cart.total = 0
        cart.save()
        messages.success(request, 'All Item in cart deleted')

    return redirect('myCart')

def bookings(request):
    rooms = Room.objects.all()
    cart_id = request.session.get('cart_id', None)
    cart_obj = Cart.objects.get(id=cart_id)
    form = BookingForm()

    # checkout authentication
    if request.user.is_authenticated and request.user.customer:
        pass
    else:
        return redirect('/login/?next=/bookings/')
    # getting cart
    if cart_id:
        cart_obj = Cart.objects.get(id=cart_id)
        # assign to cart
        if request.user.is_authenticated and request.user.customer:
            cart_obj.customer = request.user.customer
            cart_obj.save()
        # end
    else:
        cart_obj = None
    
    # form
    if request.method == 'POST':
        form = BookingForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.cart = cart_obj
            form.discount = 0
            form.subtotal = cart_obj.total
            form.amount = cart_obj.total
            form.booking_status = 'Booking Received'
            pay_mth = form.payment_method
            del request.session['cart_id']
            pay_mth = form.payment_method
            form.save()
            booking = form.id
            if pay_mth == 'Paystack':
                return redirect('payment', id = booking)
            elif pay_mth == 'Payment Transfer':
                return redirect('transfer')

            messages.success(request, 'Booking have been placed successfully')
            return redirect('index')
        else:
            messages.error(request, 'No booking have been placed')
            return redirect('index')

    context = {
        'cart':cart_obj,
        'form':form,
        'rooms':rooms

    }
    return render(request, 'eagles/bookings.html',context)

def transferPage(request):
    return render(request, 'eagles/transfer.html')

def paymentPage(request,id):
   
    booking = Bookings.objects.get(id=id)

    context = {
        'booking':booking,
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY 
    }
    return render(request, 'eagles/payment.html',context)

def verify_payment(request: HttpRequest, ref:str ) -> HttpResponse:
    payment = get_object_or_404(Bookings, ref = ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'Verification Successfully')
    else:
        messages.error(request, 'Verification Failed')
    return redirect('profile')

def room(request, room_id):   
    room = get_object_or_404(Room, pk=room_id)
    room.view_count +=1
    room.save()
    
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

@login_required(login_url='/login/')
def profile(request):
    if request.user.is_authenticated and request.user.customer:
        pass
    else:
        return redirect('/loginuser/?next=/profile/')

    customer = request.user.customer
    bookings = Bookings.objects.filter(cart__customer = customer).order_by('-id')
    context = {
        'customer':customer,
        'bookings':bookings,
    }
    
    return render(request, 'eagles/userprofile.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = CustomerRegister()
    if request.method == 'POST':
        form = CustomerRegister(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if User.objects.filter(username= username).exists():
                messages.warning(request,'User already exist')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.warning(request,'Email already exist')
                return redirect('register')
            if password != password2:
                messages.warning(request,'Password not match')
                return redirect('register')
            user = User.objects.create_user(username,email,password)
            form = form.save(commit=False)
            form.user = user
            form.save()
            messages.success(request, 'User registered successfully !')
            if "next" in request.GET:
                next_url=request.GET.get("next")
                return redirect(next_url)
            else:
                return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'eagles/register.html',context)

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        users = authenticate(request, username =username,password=password)
        if users is not None:
            login(request,users)
            messages.success(request,'User login successfully!')
            return redirect('rooms')

            
        else:
            messages.error(request,'Username/Password not correct!')

    return render(request, 'eagles/login.html')

def logoutuser(request):
    logout(request)
    messages.success(request,'User logged out successfully !')
    return redirect ('index')




