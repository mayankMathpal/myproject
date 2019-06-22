from django.db import models
from django.utils.safestring import mark_safe


class Address(models.Model):
    streetAddr      = models.CharField(max_length=62)
    city            = models.CharField(max_length=30)
    state           = models.CharField(max_length=20)
    country         = models.CharField(max_length=20)
    pincode         = models.IntegerField()

    def __str__(self):
        return self.streetAddr

class Profile(models.Model):

    gender          = (('m','male'),('f','female'),('o','other'))
    name            = models.CharField(max_length=20)
    genderField     = models.CharField(choices=gender, max_length=20, default='male')
    phoneNo         = models.IntegerField(unique=True)
    profilePic      = models.ImageField(upload_to='images/')
    dob             = models.DateField()
    perma_address   = models.OneToOneField(Address, related_name='addr', on_delete=models.CASCADE)
    company_address = models.OneToOneField(Address, related_name='cmpaddr', on_delete=models.CASCADE)
    friends         = models.ManyToManyField('self')


    def image_profile(self):
        return mark_safe('<img src="/media/%s" width ="80" height="90" />' % (self.profilePic))

    image_profile.short_description = 'Profile Pic'

    def __str__(self):
        return self.name