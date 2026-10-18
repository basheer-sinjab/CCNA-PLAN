import json

with open(r'D:\CCNA III-PLAN\plan_data.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

sections = [
    {"name": "1.0 Network Fundamentals", "start": 1, "end": 68},
    {"name": "2.0 Network Access", "start": 69, "end": 101},
    {"name": "3.0 IP Connectivity", "start": 102, "end": 144},
    {"name": "4.0 IP Services", "start": 145, "end": 169},
    {"name": "5.0 Security Fundamentals", "start": 170, "end": 199},
    {"name": "6.0 Automation and Programmability", "start": 200, "end": 221},
]

for s in sections:
    sec_items = items[s['start']-1 : s['end']]
    total_mins = sum(i['durationMins'] for i in sec_items)
    print(f"{s['name']}: {len(sec_items)} videos | {total_mins} mins (~{total_mins/60:.1f} hrs) | avg {total_mins/len(sec_items):.1f} min/vid")
