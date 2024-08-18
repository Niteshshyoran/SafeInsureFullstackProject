from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    USER_ROLES =(
        ('admin','admin'),
        ('customer','customer')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10,choices=USER_ROLES)

    def __str__(self):
        return f'{self.user}-{self.user_type}'


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField()
    description = models.TextField()
    established_date = models.DateField()

    def __str__(self):
        return self.name


class Policy(models.Model):
    policy_number = models.CharField(max_length=20, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_amount = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return self.policy_number


class Claim(models.Model):
    claim_number = models.CharField(max_length=20, unique=True)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    date_of_incident = models.DateField()
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self):
        return self.claim_number


class Payment(models.Model):
    payment_id = models.CharField(max_length=20, unique=True)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.payment_id
