from .models import Code2FA
from random import randint


def create_code(user):
    code_2fa, created = Code2FA.objects.get_or_create(user=user)
    code_2fa.new_code()
    print(code_2fa.code)
    return 'code_saved'


def find_code(user):
    code_2fa = Code2FA.objects.filter(user=user).first()
    return code_2fa


def delete_code(user):
    code_2fa = find_code(user)
    code_2fa.delete()
    return 'code_deleted'


def send_code(user):
    code_2fa = find_code(user)
    return 'code_sended'
