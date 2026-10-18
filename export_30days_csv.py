import json, csv

with open(r'D:\CCNA III-PLAN\plan_30days_data.json', 'r', encoding='utf-8') as f:
    cal_days = json.load(f)

csv_path = r'D:\CCNA III-PLAN\Plan_2026_Cisco_CCNA_v1_1_30Days_6Sections.csv'

with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Calendar Day", "Date", "Section", "Video Title", "Video URL", "Duration", "Status"])
    
    for cday in cal_days:
        if cday['is_rest_day']:
            writer.writerow([
                cday['day_label'],
                cday['date'],
                "☕ يوم راحة واسترجاع أسبوعي",
                cday['title'],
                "-",
                "-",
                "[✓] Rest Day"
            ])
        else:
            sec_label = f"{cday['section_name']} ({cday['sec_day_index']}/{cday['sec_total_days']})"
            for v in cday['videos']:
                writer.writerow([
                    cday['day_label'],
                    cday['date'],
                    sec_label,
                    v['title'],
                    v['url'],
                    v['duration'],
                    "[ ] Pending"
                ])

print(f"Generated {csv_path} successfully!")
