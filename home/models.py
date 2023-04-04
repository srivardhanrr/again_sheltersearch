from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    gender = models.CharField(max_length=10)
    room = models.CharField(max_length=10)
    college = models.CharField(max_length=100)
    # pay_id = models.CharField(max_length=50, default="Not Paid")
    # order_id = models.CharField(max_length=50, default="No")
    # paid = models.CharField(max_length=5, default="No")
    # signature = models.CharField(max_length=100, default="Empty")
    checked = models.CharField(max_length=5, blank=True, choices=(("Y", "Yes"), ("N", "No")))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Contacts(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class PayingGuest(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    college = models.ForeignKey(College, verbose_name="College", on_delete=models.CASCADE)
    distance = models.DecimalField(max_digits=3, decimal_places=3)
    gender_choice = (("Male", "Male"), ("Female", "Female"), ("Coed", "Coed"))
    gender = models.CharField(max_length=8, choices=gender_choice, default="Male")

    def __str__(self):
        return self.name


class ServiceInfo(models.Model):
    happy_clients = models.IntegerField()
    hard_worker = models.IntegerField()
    tie_ups = models.IntegerField()
    support = models.IntegerField()


class Testimonials(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    message = models.CharField(max_length=200)
    image = models.CharField(max_length=5000, null=True, blank=True)
    occupation = models.CharField(max_length=30, null=True, blank=True)


class Partners(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=5000, null=True, blank=True)





