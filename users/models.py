from django.db                  import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email    = self.normalize_email(email),
            nickname = nickname,
        )
        
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(
            email    = email,
            password = password,
            nickname = nickname,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email      = models.CharField(max_length=255, unique=True)
    nickname   = models.CharField(max_length=50, unique=True)
    is_admin   = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['nickname', ]
    
    def __str__(self):
        return f'{self.nickname} - {self.email}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    class Meta:
        db_table = 'users'