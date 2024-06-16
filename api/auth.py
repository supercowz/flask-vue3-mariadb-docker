import hashlib
import os
import hmac

def hash_password(password: str) -> bytes:
    salt = os.urandom(16)

    if isinstance(password, str):
      password = password.encode('utf-8')

    hashed_password = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    return salt + b'$' + hashed_password

def verify_password(password: str, salted_hashed_password: bytes) -> bool:
    parts = salted_hashed_password.split(b'$')
    if len(parts) != 2:
      return False
    
    salt = parts[0]
    hashed_password = parts[1]
    if isinstance(password, str):
      password = password.encode('utf-8')

    computed_hash = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)

    # Compare using compare_digest to prevent timing attacks
    return hmac.compare_digest(hashed_password, computed_hash)
