import random
import time

def generate_otp(length=6, expiry_time=5):
    """Génération d'un otp aléatoire de 6 caractères avec un temps d'expiration"""
    
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    expiry_timestamp = int(time.time()) + expiry_time

    return otp, expiry_timestamp



def is_valid_otp(user_otp, otp, expiry_timestamp):
    """Vérification de la validité de l'otp"""
    
    current_timestamp = int(time.time())

    if current_timestamp > expiry_timestamp:
        return False
    return user_otp == otp