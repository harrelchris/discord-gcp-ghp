import functions_framework
import requests

HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "POST",
    "Access-Control-Allow-Headers": "Content-Type",
}

WEBHOOK_URL = "https://discord.com/api/webhooks/1343848262255251546/kYlb3klJl5-eQ-xUL3-qTxcmpaTGsNN51uEll7scSDiP7RcfUqgjygP01RBf3xDuoV7h"


@functions_framework.http
def discord(request):
    if request.method == "OPTIONS":
        return "", 204, HEADERS

    data = request.get_json(silent=True)

    try:
        handle_data(data)
    except Exception as e:
        print(data)
        print(e)
        return {
            "status": "error",
            "message": str(e),
            "data": data,
        }, 500, HEADERS
    else:
        return {
            "status": "success",
            "data": data,
        }, 200, HEADERS


def handle_data(form_data):
    content = {
        "content": "@here New Submission",
        "embeds": [
            {
                "title": f"Submission from {form_data['name']}",
            }
        ]
    }
    response = requests.post(WEBHOOK_URL, json=content, headers={"Content-Type": "application/json"})
    response.raise_for_status()
