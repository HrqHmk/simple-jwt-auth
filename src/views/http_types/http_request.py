class HttpRequest():
    def __init__(
            self,
            body: dict = None,
            headers: dict = None,
            params: dict = None,
            tokens_infos: dict = None
        )-> None:
        self.body = body
        self.headers = headers
        self.params = params
        self.tokens_infos = tokens_infos
