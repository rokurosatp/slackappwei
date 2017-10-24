import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

def index(request):
    return HttpResponse("Hello World, You're at the tutors index")

def on_slash(request: HttpRequest):
    if request.method == "POST":
        print(request.POST)
        req_body = request.POST
        if not request.POST:
            req_body = json.JSONDecoder().decode(request.body.decode())
        response_url = req_body["response_url"]
        if req_body["token"] != 'uwLea061GWEvwy6KQTlSnQKA':
            response = HttpResponse("Access Forbidden", content_type="text/plain")
            response.status_code = 403
            return response
        else:
            message = {
                "text": "This is your first interactive message",
                "attachments": [
                    {
                        "text": "Building buttons is easy right?",
                        "fallback": "Shame... buttons aren't supported in this land",
                        "callback_id": "button_tutorial",
                        "color": "#3AA3E3",
                        "attachment_type": "default",
                        "actions": [
                            {
                                "name": "yes",
                                "text": "yes",
                                "type": "button",
                                "value": "yes"
                            },
                            {
                                "name": "no",
                                "text": "no",
                                "type": "button",
                                "value": "no"
                            },
                            {
                                "name": "maybe",
                                "text": "maybe",
                                "type": "button",
                                "value": "maybe",
                                "style": "danger"
                            }
                        ]
                    }
                ]
            }
            result = requests.post(response_url, json=message)
            result_text = b''
            #for line in result.iter_lines():
            #    print(line.decode())
            #    result_text += line
            response = HttpResponse(result_text)
            response.status_code = 200
            return response
    else:
        return HttpResponse("Access Forbidden (Use POST Method!)", content_type="text/plain", status_code=403)

def on_clicked(request: HttpRequest):
    req_body = request.POST
    if not request.POST:
        req_body = json.JSONDecoder().decode(request.body.decode())
    actionJSONPayload = json.JSONDecoder().decode(req_body["payload"])
    message = {
        "text": actionJSONPayload["user"]["name"]+" clicked: "+actionJSONPayload["actions"][0]["name"],
        "replace_original": False
    }
    result = requests.post(actionJSONPayload["response_url"], json=message)
    result_text = b''
    #for line in result.iter_lines():
    #    print(line.decode())
    #    result_text += line
    response = HttpResponse(result_text)
    response.status_code = 200
    return response

def on_debug(request: HttpRequest):
    print("request posted")
    print(request.POST)
    return HttpResponse("Hello World, Request Succeeded")




