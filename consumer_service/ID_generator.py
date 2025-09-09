import hashlib
import json

# Uses hash to generate a unique ID
class IDGenerator:

    @staticmethod
    def generate(doc, length=10):
        data_str = json.dumps(doc, sort_keys=True)
        hash_id = hashlib.sha256(data_str.encode()).hexdigest()[:length]
        doc["id"] = hash_id
        return doc
