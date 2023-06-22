import json
import openai

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


openai.api_key = "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" #dumsterdev


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

        error_message = {'error': 'Invalid JSON data'}
        return JsonResponse(error_message, status=400)


def funcgpt(user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "ты асистент помпошник плотформы ModMe Online"},
            {"role": "assistant", "content": f""},
            {"role": "assistant", "content": f""},
            {"role": "user", "content": user_prompt},

        ]
    )

    return response['choices'][0]['message']['content']



# import json
# import openai
#
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.http import require_POST
# from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
#
#
# openai.api_key = "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"
# arry = []
#
# @ensure_csrf_cookie
# def index(request):
#     return render(request, 'index.html')
#
#
# @csrf_exempt
# @require_POST
# def process_json(request):
#     try:
#         json_data = json.loads(request.body.decode('utf-8'))
#         user_input = json_data.get('text')
#         response = funcgpt(user_input)
#         prompt_response = func_prompt(response)
#         result = {'json_answer': response, 'prompt_answer': prompt_response}
#         return JsonResponse(result)
#
#     except json.JSONDecodeError as e:
#         error_message = {'error': 'Invalid JSON data'}
#         return JsonResponse(error_message, status=400)
#
#
#
# def funcgpt(user_prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "Здравствуйте! готов помочь по платформе ModeMe Online"},
#             {"role": "assistant", "content": f""},
#             {"role": "assistant", "content": f""},
#             {"role": "user", "content": user_prompt},
#
#         ]
#     )
#
#     json_answer = response['choices'][0]['message']['content']
#     print("json_answer work", json_answer)
#     return json_answer
#
#
# def func_prompt(user_response):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system",
#              "content": "сгенерируй 2 варианта вопроса,"
#                         " которые могут заинтересовать пользователя отталкиваясь от его запроса,"
#                         " каждый промпт не больше 5 слов, только массив вариантов"
#                         " без лишних символов, только цифры"},
#             {"role": "user", "content": user_response},
#         ]
#     )
#
#     prompt_answer = response['choices'][0]['message']['content'].split("\n")
#
#     arry.extend(prompt_answer)
#     print('prompt_answer work')
#     return prompt_answer
