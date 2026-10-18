import json

with open(r'D:\CCNA III-PLAN\plan_data.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Define the 6 sections
sections = [
    {"id": 1, "name": "1.0 Network Fundamentals", "ar_name": "أساسيات الشبكات", "start": 1, "end": 68, "days_count": 8},
    {"id": 2, "name": "2.0 Network Access", "ar_name": "الوصول إلى الشبكة والبنية التحتية", "start": 69, "end": 101, "days_count": 4},
    {"id": 3, "name": "3.0 IP Connectivity", "ar_name": "التوجيه والاتصال الشبكي", "start": 102, "end": 144, "days_count": 5},
    {"id": 4, "name": "4.0 IP Services", "ar_name": "خدمات بروتوكول الإنترنت", "start": 145, "end": 169, "days_count": 4},
    {"id": 5, "name": "5.0 Security Fundamentals", "ar_name": "أساسيات أمن الشبكات", "start": 170, "end": 199, "days_count": 3},
    {"id": 6, "name": "6.0 Automation and Programmability", "ar_name": "الأتمتة والبرمجة الشبكية", "start": 200, "end": 221, "days_count": 2},
]

# Total study days: 8 + 4 + 5 + 4 + 3 + 2 = 26 study days
# Let's inspect distribution for each section
def distribute(items_list, n_days):
    total = len(items_list)
    base = total // n_days
    rem = total % n_days
    chunks = []
    idx = 0
    for i in range(n_days):
        size = base + (1 if i < rem else 0)
        chunks.append(items_list[idx : idx + size])
        idx += size
    return chunks

print("Proposed Day Distributions:")
study_day_num = 1
for s in sections:
    sec_items = items[s['start']-1 : s['end']]
    chunks = distribute(sec_items, s['days_count'])
    print(f"\n=== {s['name']} ({len(sec_items)} videos) ===")
    for c in chunks:
        mins = sum(v['durationMins'] for v in c)
        print(f"  Study Day {study_day_num:02d}: {len(c)} videos | {mins:3d} mins (~{mins/60:.1f}h) | #{c[0]['id']} -> #{c[-1]['id']}")
        study_day_num += 1
