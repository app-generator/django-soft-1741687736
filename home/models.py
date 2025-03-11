# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    address = models.TextField(max_length=255, null=True, blank=True)
    phone = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Clb(models.Model):

    #__Clb_FIELDS__
    clb_name = models.TextField(max_length=255, null=True, blank=True)
    clb_address = models.TextField(max_length=255, null=True, blank=True)

    #__Clb_FIELDS__END

    class Meta:
        verbose_name        = _("Clb")
        verbose_name_plural = _("Clb")



#__MODELS__END
