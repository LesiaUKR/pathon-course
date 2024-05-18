from __future__ import annotations

import yaml
# перезаписуємо значення в файлі config.yaml
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

config["postgres"]["db_user"] = "admin"
config["postgres"]["db_password"] = "333333"

with open("config.yaml", "w", encoding="utf-8") as f:
    yaml.dump(config, f)

print(config)
print(config["postgres"]["db_user"])
