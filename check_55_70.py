import json

with open(r'D:\CCNA III-PLAN\plan_data.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for idx in range(54, 71):
    title = items[idx]['title']
    print(f"{idx+1:03d} | {items[idx]['day']} | {items[idx]['duration']} | {title}")
