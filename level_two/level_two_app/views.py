from django.shortcuts import render
from django.http import HttpResponse
from level_two_app.models import Topic, WebPage, AccessRecord


# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    my_dict = {'insert_content': "HELLO! I AM FROM LEVEL TWO"}
    return render(request, 'level_two_app/index.html', context=date_dict)
