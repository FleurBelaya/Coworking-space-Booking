from loguru import logger


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(
            "Incoming request",
            extra={
                "method": request.method,
                "path": request.path,
            },
        )

        response = self.get_response(request)

        logger.info(
            "Response",
            extra={
                "status_code": response.status_code,
            },
        )

        return response
