import re
from django.conf import settings
from django.shortcuts import redirect
from django.urls import resolve
from django.contrib import messages
class LoginControlMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self,request):
        response=self.get_response(request)
        return response
        
    def process_view(self,request,view_func,view_args,view_kwargs):
        assert hasattr(request,'user')
        path=request.path_info
        view=resolve(path).url_name
        
        print(view)
        #if view==None:
        #    return redirect('login')
        # Login Required Middleware
        if request.user.is_authenticated and view in settings.LOGIN_NOT_REQUIRED_VIEWS:
            
            return redirect('dashboard')
        elif request.user.is_authenticated or view in settings.LOGIN_NOT_REQUIRED_VIEWS:

            # User logged in 

            return None
        else:
            #messages.error(request,'Error ! Login required ')
            return redirect ('login')

       
        
    
