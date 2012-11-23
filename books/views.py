#from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book

#def search_form(request):
    #return render_to_response('search_form.html')
    #removed
	
#def search(request):
    #if 'q' in request.GET:
        #message = 'You searched for: %r' % request.GET['q']
    #else:
        #message = 'You submitted an empty form'
    #return HttpResponse(message)
    #previous version of search (v1)
	
#def search(request):
    #if 'q' in request.GET and request.GET['q']:
        #q = request.GET['q']
        #books = Book.objects.filter(title__icontains=q)
        #return render_to_response('search_results.html', {'books': books, 'query': q})
    #else:
        #return HttpResponse('Please submit a search term.') (1)
        #return render_to_response('search_form.html', {'error': True}) (2)
    #previous version of search (v2)
		
#def search(request):
    #error = False
    #if 'q' in request.GET:
        #q = request.GET['q']
        #if not q:
            #error = True
        #else:
            #books = Book.objects.filter(title__icontains=q)
            #return render_to_response('search_results.html', {'books': books, 'query': q})
    #return render_to_response('search_form.html', {'error': error})
    #previous version of search (v3) - no validation
	
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books': books, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})
