import json

json_string='{"key": "value", "id": 8, "nombre": "Juan"}'

stuff= json.loads(json_string)
print(stuff)
stuff['key']