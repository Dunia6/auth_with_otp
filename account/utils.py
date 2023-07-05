# import random
# import time

# def generate_otp(length=6, expire_time=30):
#     """Génération d'un otp aléatoire de 6 caractères avec un temps d'expiration"""
#     otp = ''.join(str(random.randint(0,9)) for i in range(length))
#     otp_time = int(time.time())
#     return otp, otp_time, expire_time


# def is_valid_otp(otp, otp_time, expire_time):
#     """Vérification de la validité de l'otp"""
#     current_time = int(time.time())
#     return (current_time - otp_time) <= expire_time and otp == otp

import random
import time

def generate_otp(length=6, expiry_time=5):
    """Génération d'un otp aléatoire de 6 caractères avec un temps d'expiration"""
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    expiry_timestamp = int(time.time()) + expiry_time
    print(expiry_timestamp)
    return otp, expiry_timestamp

def is_valid_otp(user_otp, otp, expiry_timestamp):
    """Vérification de la validité de l'otp"""
    current_timestamp = int(time.time())
    print(current_timestamp)
    if current_timestamp > expiry_timestamp:
        return False
    return user_otp == otp