import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


def get_avatar_image_path(instance, filename):
    return 'images/users/{0}/avatar/{1}'.format(instance.id, filename)


#class Department(models.Model):
#    """
#      Department is
#      a major division
#      複数可能
#    """
#
#    name = models.CharField(_('major division'), max_length=300, blank=True)
#
#    def __str__(self):
#        return self.name

#    class Meta:
#        verbose_name = _('所属')
#        verbose_name_plural = _('所属')


class User(AbstractBaseUser, PermissionsMixin):
    """
    拡張ユーザーモデル
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username_validator = UnicodeUsernameValidator()

    # username override
    username = models.CharField(
        verbose_name="ユーザーネーム", # 'user name',
        max_length=150,
        unique=True,
        help_text="半角アルファベット、半角数字にしてください。",
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(max_length=50, blank=True, verbose_name="姓")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="名")
    email = models.EmailField(_('email'), blank=True)
    phone = models.CharField(max_length=20, blank=True, verbose_name="Phone")

    #departments = models.ManyToManyField(
    #    Department,
    #    verbose_name=_('所属'),
    #    blank=True,
    #    help_text=_('Specific Departments for this user.'),
    #    related_name="user_set",
    #    related_query_name="user",
    #)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __repr__(self):
        """show main key and name"""
        return "{}: {}".format(self.pk, self.email)

    __str__ = __repr__



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nick_name = models.CharField(max_length=50, blank=True, verbose_name="ニックネーム")
    comment = models.CharField(max_length=250, blank=True, verbose_name="コメント")
    avatar = models.ImageField(upload_to=get_avatar_image_path, blank=True, verbose_name="プロフィール画像")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        """show main key and name"""
        return "{}: {}".format(self.pk, self.user)

    __str__ = __repr__
