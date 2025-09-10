import base64
from logger import Logger
logger = Logger.get_logger()

def decode_string(encrypted_text):
    try:
        encrypted_text = encrypted_text.encode('ascii')
        decoded_bytes = base64.b64decode(encrypted_text)
        decoded_string = decoded_bytes.decode('utf-8')
        logger.info("info: text decoding successfully")
        return decoded_string.split(",")
    except Exception as e:
        logger.error(e)



