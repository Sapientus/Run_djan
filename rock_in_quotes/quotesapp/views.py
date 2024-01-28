from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Quote, Author
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    authors=Author.objects.all()
    return render(request, 'quotesapp/index.html', {"quotes": quotes, 'authors':authors})

@login_required
def set_done(request, quote_id):
    Quote.objects.filter(pk=quote_id).update(done=True)
    return redirect(to='quotesapp:main')

@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id).delete()
    return redirect(to='quotesapp:main')

@login_required
def remove_author(request, author_id):
    Author.objects.get(pk=author_id).delete()
    return redirect(to='quotesapp:main')

@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/tag.html', {'form': form})

    return render(request, 'quotesapp/tag.html', {'form': TagForm()})

@login_required
def quote(request):
    tags = Tag.objects.all()
    author=Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form
            '''
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            
            choice_authors = author.filter(name__in=request.POST.getlist('author')).first()
            new_quote.author=choice_authors.id
            '''
            new_quote.save()

            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/quote.html', {"tags": tags, 'author':author, 'form': form})

    return render(request, 'quotesapp/quote.html', {"tags": tags, 'author':author, 'form': QuoteForm()})


def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quotesapp/detail.html', {"quote": quote})

def lookfor(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotesapp/lookfor.html', {"author": author})


@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author=form
            author.save()

            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/author.html', {'form': form})

    return render(request, 'quotesapp/author.html', {'form': AuthorForm()})
