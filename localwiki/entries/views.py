from django.shortcuts import render, get_object_or_404
from .models import WikiPage

def wiki_index(request):
    pages = WikiPage.objects.all()
    return render(request, 'entries/index.html', {'pages': pages})

def wiki_page(request, slug):
    page = get_object_or_404(WikiPage, slug=slug)
    html_content = page.get_html_content()
    return render(request, 'entries/wiki_page.html', {'page': page, 'html_content': html_content})
