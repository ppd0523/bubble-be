from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import validate_slug, validate_unicode_slug
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, nickname, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            nickname=nickname,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nickname, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            nickname=nickname,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField('user ID', max_length=20, unique=True, validators=[validate_slug])
    email = models.EmailField(
        verbose_name='email address',
        max_length=100,
        blank=True,
        null=True,
    )
    nickname = models.CharField('nickname', max_length=24, unique=True, validators=[validate_unicode_slug])
    joined_date = models.DateField(default=timezone.localdate, editable=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nickname']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class ToFollow(models.Model):
    followee = models.ForeignKey(User, to_field='username', related_name='followee', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, to_field='username', related_name='follower', on_delete=models.CASCADE)
    create_date = models.DateField(default=timezone.localdate, null=False, blank=False, editable=False)
    delete_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.follower} -> {self.followee}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['followee', 'follower'], name='unique_following')
        ]