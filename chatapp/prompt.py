import json
import openai
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

openai.api_key = "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"  # scumesc


@csrf_exempt
@require_POST
def process_json2(request):
    try:
        json_data = json.loads(request.body.decode('utf-8'))
        user_input = json_data.get('text')
        response = funcgpt2(user_input)
        result = {'response': response}
        return JsonResponse(result)

    except json.JSONDecodeError as e:
        error_message = {'error': 'Invalid JSON data'}
        return JsonResponse(error_message, status=400)


def funcgpt2(user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "сгенерируй 2 варианта вопроса не большее двух и без только вариант вапроса"
                                          "которые могут заинтересовать пользователя оталкиваесь от его запрос,"
                                          "каждый вапрос не большее 6 слов,"
                                          "разделяй каждый вопрос с \n"},
            {"role": "user", "content": user_prompt},
        ]
    )

    return response['choices'][0]['message']['content'].split("\n")