from django.shortcuts import render
import uuid
from .models import URL
from django.http import HttpResponse

# Create your views here. Logic handling/data handling of requests to the coresponsing url paths (index, create etc -> names denoted in urls.py)
def index(request):
    return render(request, "index.html")

def create(request):
    if request.method == "POST":
        url = request.POST['link'] #the data object has a key called link from from the AJAX REQUEST. links value is the long url. Request.POST is our ajax data object/dictionary. We are accessing the link key/dictionary with []
        short_link_id = str(uuid.uuid4())[:5] #expression that uses the uuid to generate a uuid/random id and take the first 5 char [:5]
        #NOW LETS SAVE THE ABOVE TO THE DB/URL MODEL
        new_url = URL(link=url, short_link_id=short_link_id) #create the new URL data using the URL model
        new_url.save() #save the new URL
        return HttpResponse(short_link_id) #send a response to the client of the short_url_id which ajax will take care of using its succes function
