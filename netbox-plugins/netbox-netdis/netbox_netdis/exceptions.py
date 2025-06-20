class NaaSServiceException(Exception):
    def __init__(self, result: dict, exc_info: bool = False):
        self.result = result
        self.status = result.get("status", "error")
        self.exc_info = exc_info

    def __str__(self):
        return self.result.get("message", "Unknown error occurred in the NaaS service.")
