import secrets
from django.db import models
from datetime import datetime
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from .validators import Banner_v
from . paystack import PayStack


class Banner(models.Model):
    title = models.CharField(max_length=500,null=True,blank=True)
    body = RichTextField(null=True,blank=True)
    video = models.FileField(validators=[Banner_v],null=True,blank=True)
    button = models.CharField(max_length=100,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null =True,blank=True)
    registered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name

class Room(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    price = models.PositiveIntegerField(null=True,blank=True)
    discount_price = models.PositiveIntegerField(null=True,blank=True)
    guests = models.CharField(max_length=50,blank=True)
    bed = models.CharField(max_length=50,blank=True)
    car_rent = models.CharField(max_length=50,blank=True,null=True)
    roomimg = models.ImageField()
    roomimg1 = models.ImageField(blank=True)
    roomtmg2 = models.ImageField(blank=True)
    roomtmg3 = models.ImageField(blank=True)
    view_count = models.PositiveIntegerField(default=0,blank=True,null=True)
    description = models.TextField(blank=True)
    isbooked = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'room'
        managed = True
        verbose_name = 'rooms'
        verbose_name_plural = 'rooms' 

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'cart ::: {str(self.id)}'

class CartRoom(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True,blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'cart ::: {str(self.cart.id)} - cartroom ::: {str(self.id)}'

OREDER_STATUS = (
	('Booking Received','Booking Received'),
	('Booking Processing','Booking Processing'),
	('Booking Completed','Booking Completed'),
	('Booking Canceled','Booking Canceled'),
	)

METHOD = (
    ('Paystack','Paystack'),
    ('Payment Transfer','Payment Transfer'),
    ('Cash On Arrival','Cash On Arrival'),
)

class Bookings(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    booked_by =models.CharField(max_length=200)
    check_in  = models.DateField()
    check_out = models.DateField()
    gender = models.CharField(max_length=50,null=True, blank=True)
    address = models.CharField(max_length=500,null=True, blank=True)
    adults = models.IntegerField()
    children = models.IntegerField()
    mobile = models.CharField(max_length=11)
    email = models.EmailField(null=True,blank=True)
    discount = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    booking_status = models.CharField(max_length=200, choices=OREDER_STATUS)
    booking_date = models.DateTimeField(auto_now_add=True)	
    payment_method = models.CharField(max_length=20, choices=METHOD,default='Paystack')
    payment_completed = models.BooleanField(default=False,null=True,blank=True)
    ref = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return f'{self.booking_status} ::: {str(self.id)}'

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            obj_with_sm_ref = Bookings.objects.filter(ref=ref)
            if not obj_with_sm_ref:
                self.ref= ref
        super().save(*args, **kwargs)
    
    def amount_value(self) -> int:
        return self.amount * 100

    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.payment_completed=True
            self.save()
        if self.order_status == 'Order Completed':
            self.save()
            self.cart.delete()
        if self.payment_completed:
            return True
        return False

    class Meta:
            db_table = 'Bookings'
            managed = True
            verbose_name = 'Bookings'
            verbose_name_plural = 'Bookings' 

class Gallery(models.Model):
    imggallery = models.ImageField()
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'gallery'
        managed = True
        verbose_name = 'Gallerys'
        verbose_name_plural = 'Gallerys'

class Dining(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100,null=True,blank=True)
    diningimg = models.ImageField()
    text_1 = models.CharField(max_length=500,null=True,blank=True)
    text_2 = models.CharField(max_length=500,null=True,blank=True)
    text_3 = models.CharField(max_length=500,null=True,blank=True)
    text_4 = models.CharField(max_length=500,null=True,blank=True)
    text_5 = models.CharField(max_length=500,null=True,blank=True)
    body = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Dining'
        managed = True
        verbose_name = 'Dining'
        verbose_name_plural = 'Dining'  
 
class Spa(models.Model):
    title = models.CharField(max_length=100)
    spaimg = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'spa'
        managed = True
        verbose_name = 'Spa'
        verbose_name_plural = 'Spa'  

class Meeting(models.Model):
    title = models.CharField(max_length=100)
    meetimg = models.ImageField()
    

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'meeting'
        managed = True
        verbose_name = 'Meetings'
        verbose_name_plural = 'Meetings' 

class Ourservice(models.Model):
    subtitle = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

        return self.title

class Whoweare(models.Model):
    subtitle = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    text_1 = models.CharField(max_length=500)
    text_2 = models.CharField(max_length=500)
    text_3 = models.CharField(max_length=500)
    text_4 = models.CharField(max_length=500)
    text_5 = models.CharField(max_length=500)
    text_6 = models.CharField(max_length=500)
    leadimg = models.ImageField(default='myleadimg.jpg',null=True,blank=True)
    body = RichTextField()
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

        return self.title

    class Meta:
        db_table = 'Whoweare'
        managed = True
        verbose_name = 'Whoweare'
        verbose_name_plural = 'Whoweare' 

class Comfort(models.Model):
    subtitle = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    body = models.TextField(null=True,blank=True)
    def __str__(self):

        return self.title

class Ourinfo(models.Model):
    subtitle = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    years = models.CharField(max_length=500)
    number = models.CharField(max_length=500)
    subtitle_1 = models.CharField(max_length=500)
    subtitle_2 = models.CharField(max_length=500)
    text_1 = models.TextField(blank=True)
    text_2 = models.TextField(blank=True)
    leadimg = models.ImageField(default='myleadimg.jpg',null=True,blank=True)
    body = RichTextField()
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Ourinfo, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Ourinfo'
        managed = True
        verbose_name = 'Ourinfo'
        verbose_name_plural = 'Ourinfo' 

class Ourservice1(models.Model):
    subtitle = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    subtitle_1 = models.CharField(max_length=500)
    subtitle_2 = models.CharField(max_length=500)
    text_1 = models.TextField(blank=True)
    text_2 = models.TextField(blank=True)
    leadimg = models.ImageField(default='myleadimg.jpg',null=True,blank=True)
    body = RichTextField()
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

        return self.title

class Service(models.Model):
    title_1 = models.CharField(max_length=500)
    title_2 = models.CharField(max_length=500)
    title_3 = models.CharField(max_length=500)
    title_4 = models.CharField(max_length=500)
    title_5 = models.CharField(max_length=500)
    title_6 = models.CharField(max_length=500)
    subtitle_1 = models.CharField(max_length=500)
    subtitle_2 = models.CharField(max_length=500)
    subtitle_3 = models.CharField(max_length=500)
    subtitle_4 = models.CharField(max_length=500)
    subtitle_5 = models.CharField(max_length=500)
    text_1 = models.TextField(blank=True)
    text_2 = models.TextField(blank=True)
    text_3 = models.TextField(blank=True)
    text_4 = models.TextField(blank=True)
    text_5 = models.TextField(blank=True)
    text_6 = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    def __str__(self):

        return self.title_1

class About(models.Model):
    title_1 = models.CharField(max_length=500)
    title_2 = models.CharField(max_length=500)
    title_3 = models.CharField(max_length=500)
    title_4 = models.CharField(max_length=500)
    text_1 = models.TextField(blank=True)
    text_2 = models.TextField(blank=True)
    text_3 = models.TextField(blank=True)
    text_4 = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    def __str__(self):

        return self.title_1

class Blog(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Blog'
        managed = True
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

class BlogComment(models.Model):
    body = models.TextField()
    Blogusercomment = models.ForeignKey(User,on_delete=models.DO_NOTHING)  
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'BlogComments'
        managed = True
        verbose_name = 'BlogComment'
        verbose_name_plural = 'BlogComments'

class Contact(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.fname} {self.lname}'

    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts'         

