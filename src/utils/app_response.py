from flask import Response, json
class AppResponse(Response):
    default_mimetype = "application/json"
    def __init__(self, body:dict={}, message:str=None, status="success", status_code=200, **kwargs):
        response_body = {
            "status": status,
            **body
        }
        if message != None and message.strip() != "":
            response_body.update({"message": message})
        response_json = json.dumps(response_body)
        super().__init__(response_json, status=status_code, mimetype=self.default_mimetype, **kwargs)