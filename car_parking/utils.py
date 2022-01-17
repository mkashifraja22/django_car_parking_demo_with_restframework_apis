def operation_success(data=None,msg="operation successful!"):
    return {
        "Success":True,
        "message":msg,
        "data":data
    }


def operation_failure(data=None,msg="operation failed!"):
    return {
        "Success":False,
        "message":msg,
        "data":data
    }