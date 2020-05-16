import datetime
from django.conf import settings

def send_context(request):
    current_datetime=datetime.date.today()
    day=current_datetime.strftime("%A")
    sidebar_url=''
    cart_type=request.session.get(settings.CART_TYPE_SESSION_ID)
    if cart_type==None or cart_type=='':
        cart_type='Sale'
    
    if request.user.is_authenticated:
        sidebar_url=f'sidebar/{request.user.profile.account_type}.html'
    output = f'{current_datetime} - {day}'
    return { 'date':output,
            'sidebar_url':sidebar_url,'cart_type':cart_type,
        }