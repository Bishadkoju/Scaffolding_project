import datetime

def send_context(request):
    current_datetime=datetime.date.today()
    day=current_datetime.strftime("%A")
    sidebar_url=''
    if request.user.is_authenticated:
        sidebar_url=f'sidebar/{request.user.profile.account_type}.html'
    output = f'{current_datetime} - {day}'
    return { 'date':output,
            'sidebar_url':sidebar_url,
        }