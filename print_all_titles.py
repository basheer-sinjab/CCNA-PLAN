import json

with open(r'D:\CCNA III-PLAN\plan_data.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for idx, item in enumerate(items):
    title = item['title']
    print(f"{idx+1:03d} | {item['day']} | {item['duration']} | {title}")
