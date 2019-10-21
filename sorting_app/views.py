from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hey, Hi!")


def contact(request):
    input_value = request.POST['input_list']

    new_input_value = input_value[:4]

    return render(request, 'contact.html', {
        'phone': "+2348164702655",
        'name': "Yinka",
        'email': "olayinka@semicolon.africa",
        'input': new_input_value
    })


def summary(request):
    API_key = "14f0a0f22f57411d5b84b58c52446d73"
    input_link = request.POST['input_list']
    input_number = request.POST['input_number']

    API_response = requests.get('https://api.meaningcloud.com/summarization-1.0?'
                                + 'key=' + API_key + '&url=' + input_link
                                + '&sentences=' + input_number)

    summary = API_response.json()['summary']

    return render(request, 'summary.html', {
        'summary': summary
    })


