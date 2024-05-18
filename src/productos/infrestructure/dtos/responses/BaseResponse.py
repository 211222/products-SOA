class BaseResponse:
    def __init__(self, data, message, status, httpstatuscode):
        self.data = data
        self.message = message
        self.status = status
        self.httpstatuscode = httpstatuscode

    def response(self):
        return {
            "data": self.data,
            "message": self.message,
            "status": self.status
        }, self.httpstatuscode
