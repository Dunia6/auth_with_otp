import random
import time

def generate_otp(length=6, expire_time=30):
    """Génération d'un otp aléatoire de 6 caractères avec un temps d'expiration"""
    otp = ''.join(str(random.randint(0,9)) for i in range(length))
    otp_time = int(time.time())
    return otp, otp_time, expire_time


def is_valid_otp(otp, otp_time, expire_time):
    """Vérification de la validité de l'otp"""
    current_time = int(time.time())
    return (current_time - otp_time) <= expire_time and otp == otp