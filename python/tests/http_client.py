class Http_client:
    def __init__(self):
        self.base_url = ""
        self.request = ""

    def post(self, base_url, request):
        self.base_url = base_url
        self.request = request
