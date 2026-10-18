import json

with open(r'D:\CCNA III-PLAN\plan_data.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for idx in range(0, 105):
    title = items[idx]['title']
    if any(k in title.lower() for k in ['module', 'review', 'vlan', 'switching', 'access', 'fundamentals']):
        print(f"{idx+1:03d} | {items[idx]['day']} | {title}")
