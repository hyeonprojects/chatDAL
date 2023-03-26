import os, json

from fastapi import HTTPException

secret_json_file = os.path.join('./', 'env.json')


with open(secret_json_file, 'r') as secret_json:
    secret = json.load(secret_json)


def get_secret(setting, secret=secret):
    """
    비밀 변수를 가져오거나 명시적 예외를 반환함
    """
    try:
        return secret[setting]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(setting)
        raise HTTPException(status_code=404, message=error_msg)


def get_os_secrets(setting):
    """
    환경 변수 가져오는 기능
    """
    try:
        return os.environ[setting]
    except KeyError:
        raise HTTPException(status_code=404, message='Not found setting')
