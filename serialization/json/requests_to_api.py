from __future__ import annotations

import json

# curl https://jsonplaceholder.typicode.com/posts/
# wget -O-  https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11
# json - java script object notation - текстовий формат обміну даними, що базується на синтаксисі мови JavaScript
# deserialization = load(для файлу), loads (для строки)
# serialization = dump(для файлу), dumps(для строки)

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

data = json.loads(json_string)
print(data)
print(data["researcher"]["name"])
