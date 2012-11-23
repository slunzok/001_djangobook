#from django.template.loader import get_template
#from django.template import Context
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def hello(request):
    return HttpResponse("Hello World!")
	
def homepage(request):
    return HttpResponse("Welcome to the page at %s" % request.path)
	
def ua_display_good1(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = unknown
    return HttpResponse("Your browser is %s" % ua)
	
def ua_display_good2(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" %ua)
	
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
	
#def current_time(request):
    #now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
    #previous version
	
def current_time(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})
	
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s</body></html>" % (offset, dt)
    return HttpResponse(html)
