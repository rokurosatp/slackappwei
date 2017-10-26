"""
仮想乱数を利用したSECRET_KEYの発行
長さ50のキーが発行される
https://gist.github.com/mattseymour/9205591を参照
"""
import string
import random

def generate_key():
    # Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
    chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace("\\", '')
    return ''.join([random.SystemRandom().choice(chars) for i in range(50)])

with open("secret-key.tok", 'w') as f:
    SECRET_KEY = generate_key()
    f.write(SECRET_KEY)


    

