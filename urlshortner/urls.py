from django.urls import path
from . import views

# RESTFUL API PATTERNS AND ROUTE REQUESTS ARE SET UP HERE AND MANAGED BY VIEWS.PY. URL PATH HANDLING which setsup requsts and url path. VIEWS.PY MANAGES THE LOGIC OF EACH PATHs/URLPATTERN
urlpatterns = [
    path("", views.index, name="index"), #views.index is the function being imported from views, which is the logic to apply/manage on each request to a url path
    path("create", views.create, name="create"),
    path("<str:id>", views.redirecturl, name="redirecturl") #DYNAMIC URL -> <str:id> IS LIKE REQ.PARAMS. This path is looking for localhost:8000/XXXXX
    ]