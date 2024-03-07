from django.urls import path
from recipes.views import home


#(Cliente) HTTP Request <- HTTP Response (Servidor)

#HTTP Request - funçao que é mandada ao servidor.
#return HTTP response - resposta dada pelo servidor.



urlpatterns = [
    path('', home),
]
