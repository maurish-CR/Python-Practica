def encrypt_message(string):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for v in string:
        en = (alpha.index(v) + len(string)-1) % 26
        encrypted += alpha[en]
    return encrypted
print(encrypt_message('xyz'))