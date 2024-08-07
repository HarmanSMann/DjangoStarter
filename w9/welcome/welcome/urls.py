"""
URL configuration for welcome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def hello_bob(request):
    return HttpResponse('<h1>HELLO FROM BOB</h1>')

# def hello_bob(request):
#     return HttpResponse('''
#                             <h1>Simple Form</h1>
#     <form method="post">
#         {% csrf_token %}
#         {{ form.as_p }}
#         <button type="submit">Submit</button>
#     </form>''')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bob/', "<h1>HELLO FROM BOB</h1"),
]
