from django.db import models
import datetime

class User_Info(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    @staticmethod
    def emailIsExists(sample_email):
        if User_Info.objects.filter(email=sample_email):
            return True
        else:
            return False

    @staticmethod
    def usernameIsExists(sample_username):
        if User_Info.objects.filter(username=sample_username):
            return True
        else:
            return False

    @staticmethod
    def getCustomerByEmail(sample_email):
        try:
            return User_Info.objects.get(email=sample_email)

        except:
            return None

    @staticmethod
    def getCustomerByUsername(sample_username):
        try:
            return User_Info.objects.get(username=sample_username)

        except:
            return None

    def __str__(self):
        return self.email + ', id= '+str(self.id)


class client_requirement(models.Model):
    to_neighbour_choice = ((True, 'true'),
                           (False, 'false'))
    username = models.ForeignKey(User_Info, null=True, on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=20, null=True, default='blank')
    recipient_email = models.EmailField(null=True)
    recipient_mobile = models.CharField(max_length=12, null=True, default='blank')
    item_type = models.CharField(max_length=50, null=True, default='blank')
    item_name = models.CharField(max_length=50, null=True, default='blank')
    item_weight = models.IntegerField(null=True, blank=True)
    sender_pincode = models.CharField(max_length=12)
    receiver_pincode = models.CharField( max_length=50, null=True, default='blank')
    sender_address = models.TextField(max_length=300, null=True, default='blank')
    receiver_address = models.TextField(max_length=300, null=True, default='blank')
    package_images = models.ImageField(null=True, default='not_provided',upload_to="upload/orders")
    #to_neighbour = models.CharField(max_length=10,default='false',null=True,choices=to_neighbour_choice)
    date = models.DateField(default = datetime.datetime.today())

    @staticmethod
    def get_orders_by_customer_id(customer):
          return client_requirement.objects.filter(username = customer.id)

    def __str__(self):
        return str(self.username)
