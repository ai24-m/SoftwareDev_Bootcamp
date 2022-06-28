from django.db import models
import re



class UserManager(models.Manager):
    def validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        emails = Users.objects.filter(email=postData['email'])
    
        if len(emails)>0:
            errors['emailExist']="This Email is already in use!"
            return errors

        if not postData['fname']:
            errors['fname']="The First Name field is required !"

        elif len(postData['fname'])<2:
            errors['fname']= 'First Name must be at least 2 characters'

        if not postData['lname']:
            errors['lname']="The Last Name field is required !"

        elif  len(postData['lname'])<2:
            errors['lname']= 'Last Name must be at least 2 characters'

        if not EMAIL_REGEX.match(postData['email']):
            errors['email']="The email field is required !"

        elif not EMAIL_REGEX.match(postData['email']):
            errors['email']='Invalid email address!'

        if not postData['password']:
            errors['password']="The Password field is required !"

        elif len(postData['password'])<8:
            errors['password'] = 'Password must be at least 8 characters'

        if not postData['Cpassword']:
            errors['Cpassword']="The Password field is required !"

        elif not postData['Cpassword'] == postData['password']:
            errors['Cpassword'] = 'Password and Confirm Password must be the same!'
        return errors


class Users(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    createdAt =models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now= True)
    objects = UserManager()

class BookManager(models.Manager):

    def valdator(self,postData):
        errors = {}
        if len(postData['title'])<1:
            errors['title']="You must include the title."
        if len(postData['desc'])<5:
            errors['desc']="Your description must be at least 5 characters."
        return errors

class Books(models.Model):
    title=models.CharField(max_length=55)
    desc=models.TextField()
    uplodedBy =models.ForeignKey(Users, related_name="books_uploaded", on_delete = models.CASCADE)
    userLikes = models.ManyToManyField(Users, related_name="liked_books")
    createdAt =models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now= True)
    objects = BookManager()