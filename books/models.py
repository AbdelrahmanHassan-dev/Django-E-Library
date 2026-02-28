from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from django.conf import settings


class Author(models.Model):
    name = models.CharField(max_length= 50)
    birth_date = models.DateField()
    nationallty = models.CharField(max_length=100)
    photo_profile= models.ImageField(upload_to='photos/%Y/%m/%d/',null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    title= models.CharField(max_length=50)
    discribtion = models.TextField()

    def __str__(self):
        return self.title

class Book(models.Model):
    title= models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/',null=True, blank=True)
    discribtion = models.TextField()
    spread_date = models.DateField()
    number_pages = models.IntegerField()
    ISBN = models.IntegerField()
    ratings = GenericRelation(Rating, related_query_name='books')
    language = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    autor = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    


    class Meta:
        permissions = [
            ("can_mark_featured","Can add a feature")
        ]
    

    READING_STATUS_CHOICES = [
        ('reading', 'reading'),
        ('completed', 'completed'),
        ('paused', 'paused'),
        ('abandoned', 'abandoned'),
    ]
    reading_status = models.CharField(
        max_length=20,
        choices=READING_STATUS_CHOICES,
        default='reading',
        help_text="حالة القراءة الحالية للكتاب"
    )
    def __str__(self):
        return self.title

class Messages(models.Model):
    sender_name= models.CharField(max_length=50)
    content = models.TextField()
    time = models.DateField()

    # books = models.ManyToManyField(Book)
    # def __str__(self):
    #     return self.

    def __str__(self):
        return self.sender_name

# class Favorite(models.Model):
    
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='users',on_delete=models.CASCADE)
#     favorite_books = models.ForeignKey(Book,on_delete=models.CASCADE)



class Favoritebooks(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    favorite_books = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True , blank=True)
    
    # def __str__(self):
    #     return f"the user {self.user} the book is {self.favorite_books.title}"
    class Meta:
        unique_together = ('user','favorite_books')