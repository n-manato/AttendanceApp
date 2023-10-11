from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
import uuid as uuid_lib

class Department(models.Model):
    """所属 兼任可"""

    name = models.CharField(_('所属'), max_length=150, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('所属')
        verbose_name_plural = _('所属')

class Period(models.Model):
    period = models.CharField(max_length=50)#前期・後期
    def __str__(self):
        return self.period
    
class Hour(models.Model):
    hour = models.CharField(max_length=50, blank=True)#時限
    def __str__(self):
        return self.hour

class Date(models.Model):
    date = models.CharField(max_length=50, blank=True)#時限
    def __str__(self):
        return self.date
    
class Subject(models.Model):
    subject = models.CharField(max_length=50)#教科
    period = models.ForeignKey(Period, on_delete=models.SET_NULL, null=True, max_length=50, related_name='related_period')#時限
    hour = models.ForeignKey(Hour, on_delete=models.SET_NULL, null=True, max_length=50, related_name='related_hour')#前期後期
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='related_department')#CS・AD・EE・ME
    date = models.ForeignKey(Date, on_delete=models.SET_NULL, null=True, max_length=50, related_name='related_date')#曜日
    Number_of_classes =  models.IntegerField(null=True,blank=True,default=0)
    def __str__(self):
        return self.subject

class User(AbstractBaseUser, PermissionsMixin):
    """AbstractUser"""
    Subject = models.ManyToManyField(Subject, verbose_name=_('科目'), blank=True, related_name='related_Subject')

    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            primary_key=True, editable=False)
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    full_name = models.CharField(_('氏名'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    departments = models.ManyToManyField(
        Department,
        verbose_name=_('所属'),
        blank=True,
        help_text=_('Specific Departments for this user.'),
        related_name="user_set",
        related_query_name="user",
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    accidental_absence = models.IntegerField(null=True,blank=True,default=0)
    class_absence = models.IntegerField(null=True,blank=True,default=0)
    sick_absence = models.IntegerField(null=True,blank=True,default=0)
    leaving_early = models.IntegerField(null=True,blank=True,default=0)
    tardiness = models.IntegerField(null=True,blank=True,default=0)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name