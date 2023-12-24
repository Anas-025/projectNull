from django.http import HttpResponse
from .forms import MyForm
from django.shortcuts import render
import requests 

def index(request):
    if request.method == 'GET':
        form = MyForm()
        return render(request, 'form.html', {'form': form})

    elif request.method == 'POST':
        form = MyForm(request.POST)
        csrf_token = request.POST['csrfmiddlewaretoken']
        headers = {'X-CSRFToken': csrf_token}
        cookies = {'csrftoken': csrf_token}
        if form.is_valid():
            response = requests.post(
                            'http://127.0.0.1:8000/app/api/util/v1/public/transform',
                            data={'text': form.cleaned_data['text']},
                            cookies=cookies,
                            headers=headers)
            if response.status_code == 200:
                transformed_text = response.text
                return render(request, 'result.html', {'text': transformed_text})
            else:
                error_message = f"Error: {response.status_code} - {response.text}"
                return HttpResponse(error_message)
        else:
            return HttpResponse("Invalid form")

    else:
        return HttpResponse("Invalid request")