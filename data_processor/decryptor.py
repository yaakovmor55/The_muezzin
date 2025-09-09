import base64


def decode_string(encrypted_text):
    encrypted_text = encrypted_text.encode('ascii')
    decoded_bytes = base64.b64decode(encrypted_text)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string



