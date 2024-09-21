from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import WikiPage, WikiImage

def wiki_index(request):
    pages = WikiPage.objects.all()
    return render(request, 'entries/index.html', {'pages': pages})

def wiki_page(request, slug):
    page = get_object_or_404(WikiPage, slug=slug)
    html_content = page.get_html_content()
    return render(request, 'entries/wiki_page.html', {'page': page, 'html_content': html_content})

def upload(request):
    if request.method == "POST":
        title = request.POST.get('title')
        markdown = request.FILES.get('markdown')
        wiki_page = WikiPage.objects.create(title=title, markdown_file=markdown)
        images = request.FILES.getlist('images')
        
        for image in images:
            WikiImage.objects.create(wiki_page=wiki_page, image=image)
        
        return redirect(wiki_page.get_absolute_url())
    
    return render(request, "entries/upload.html")




