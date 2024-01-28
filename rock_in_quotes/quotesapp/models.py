from django.db import models


class Tag(models.Model):
    name=models.CharField(max_length=50, null=False)
    def __str__(self):
        return f'{self.name}'


    
class Author(models.Model):
    name=models.CharField(max_length=50, null=False)
    borndate=models.DateField()
    bio=models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'
    
class Quote(models.Model):
    name=models.CharField(max_length=50, null=False)
    tags=models.ManyToManyField(Tag)
    description=models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f'{self.name}'