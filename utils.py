import uuid


def get_uuid():
    uuid1 = str(uuid.uuid1())
    return uuid1.replace('-', '')
