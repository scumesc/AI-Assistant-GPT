import json
import openai

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


#Dumster Key
openai.api_key = "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"


@ensure_csrf_cookie
def index(request):
    return render(request, 'index.html')


@csrf_exempt
@require_POST
def process_json(request):
    try:
        json_data = json.loads(request.body.decode('utf-8'))
        user_input = json_data.get('text')
        response = funcgpt(user_input)
        result = {'response': response}
        return JsonResponse(result)

    except json.JSONDecodeError as e:

        error_message = {'error': 'Invalid JSON data  + ошибка на Frontend'}
        return JsonResponse(error_message, status=400)


@csrf_exempt
@require_POST
def companyinfo(request):
    try:
        json_data = json.loads(request.body.decode('utf-8'))
        user_input = json_data.get('text')
        response = funcgpt(user_input)
        result = {'response': response}
        return JsonResponse(result)

    except json.JSONDecodeError as e:

        error_message = {'error': 'Invalid JSON data  + ошибка на Frontend'}
        return JsonResponse(error_message, status=400)


def funcgpt(user_prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"ты асистент помпошник плотформы {companyinfo} если тут ModMe online"},
                {"role": "assistant", "content": f"генерируй ответы в трех языках"
                                                 f" смотря на каком языке написал ползователь в основом это "
                                                 f"русский, узбекский и инданезийский"},
                {"role": "user", "content": user_prompt},
            ]
        )

        return response['choices'][0]['message']['content']

    except Exception as e:
        # If there's an error, return it as a string to display on the frontend
        return "📌 Лимит превышен три" \
               "запроса в минуту!!!"





