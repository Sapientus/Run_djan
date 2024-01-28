from django.forms import ModelForm, CharField, DateField, TextInput, DateInput, ModelChoiceField, ModelMultipleChoiceField
from .models import Tag, Quote, Author


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']

class QuoteForm(ModelForm):

    name = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=300, required=True, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all())
    class Meta:
        model = Quote
        fields = ['name', 'description', 'tags', 'author']
        #exclude = ['tags', 'author']

class AuthorForm(ModelForm):

    name = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    borndate=DateField(widget=DateInput())
    bio = CharField(min_length=10, max_length=150, widget=TextInput())

    class Meta:
        model = Author
        fields = ['name', 'borndate', 'bio']