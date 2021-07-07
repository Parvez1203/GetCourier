from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User  
from customer.models import User_Info , client_requirement
from django.views import View
from django.contrib.auth.hashers import make_password, check_password


def index(request):
      print(request.session.get('username'))
      return render(request , 'index.html')

class login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User_Info.getCustomerByEmail(email)
        if user is not None:
            if check_password(password,user.password):
                request.session['email'] = user.email
                request.session['username'] = user.username
                return redirect('/')
            else:
                return render(request,'login.html',{'error':'incorrect email or password'})
        else:
                return render(request,'login.html',{'error':'incorrect email or password'})

   
def contact_us(request):
    if request.method=="POST":
        user = User_Info.getCustomerByEmail(request.session.get('email'))
        
        if user is None:
            return HttpResponse('you must our user,please login first')
        
        else:
            input_username =  user
            input_recipient_name= request.POST.get('recipient_name')
            input_recipient_email = request.POST.get('recipient_email')
            input_recipient_mobile = request.POST.get('recipient_mobile')
            input_item_type =request.POST.get('item_type')
            input_item_name =request.POST.get('item_name')
            input_item_weight=request.POST.get('item_weight')
            input_sender_pincode = request.POST.get('sender_pincode')
            input_receiver_pincode = request.POST.get('receiver_pincode')
            input_sender_address =request.POST.get('sender_address')
            input_receiver_address=request.POST.get('receiver_address')
            image = request.FILES.get('image')
            #input_to_neighbour =request.POST.get('neighbour','false')

            client_info = client_requirement(username=input_username,recipient_name=input_recipient_name,recipient_email=input_recipient_email,
            recipient_mobile=input_recipient_mobile,item_type=input_item_type,item_name=input_item_name,item_weight=input_item_weight,
            sender_pincode=input_sender_pincode,receiver_pincode=input_receiver_pincode,sender_address=input_sender_address,
            receiver_address= input_receiver_address,package_images=image)
            client_info.save()
            return HttpResponse('okay')
    
    return render(request,'contactus.html')
    
    
        
def about(request):
    return render(request , 'about.html')

def customer_support(request):
    return render(request,'customer_support.html')

def FAQs(request):
    return render(request,'FAQs.html')


def logoutUser(request):
    request.session.clear()
    return redirect('/login')  

def registration(request):
    if request.method == "POST":
                name = request.POST.get('Name')
                form_username = request.POST.get('username')
                email = request.POST.get('email')
                mobile = request.POST.get('Mobile')
                password = request.POST.get('password')
                confirm_password = request.POST.get('Confirm Password')
                
                # making an user object to validate(user)
                user = User_Info(name = name,
                                 username = form_username,
                                 email = email,
                                 mobile = mobile,
                                 password = password) 
                
               
                error_messages = validate(user,confirm_password)
                print(error_messages)

                if error_messages is None:
                    user.password = make_password(password)
                    User_Info.save(user)
                    return redirect('/')
               
                values = {
                  'name': name,
                  'username': form_username,
                  'email': email,
                  'mobile': mobile
                }

                data = {
                    'error': error_messages,
                    'value': values
                }

                return render(request, 'registration.html', data)
    
    return render(request, 'registration.html')

def validate(user,confirm_password):
    error_messages = None
   # checking validations
    if User_Info.emailIsExists(user.email):
        error_messages = 'this email is already registered'

    elif User_Info.usernameIsExists(user.username):
        error_messages = 'username is taken please another'

    elif user.name == '':
        error_messages = 'name is mandatory'

    elif user.email == '':
        error_messages = 'email is mandatory'

    elif user.mobile == '':
        error_messages = 'mobile number is mandatory'

    elif user.password == '':
        error_messages = 'password is mandatory'

    elif user.password != confirm_password:
        error_messages = 'password is not matching'

    return error_messages

def orders(request):
    try:
        customer = User_Info.getCustomerByUsername(request.session.get('username'))
        orders = client_requirement.get_orders_by_customer_id(customer)
        return render(request , 'orders.html' , {'orders' : orders})
    except:
        return HttpResponse('you are not logged in')