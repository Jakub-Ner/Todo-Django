import requests


class TimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = requests.get("http://127.0.0.1:5000/time")
            request.time = response.json()['time']
        except:
            request.time = "NaN"
            print("Could not connect to TimeApi server")

        return self.get_response(request)
