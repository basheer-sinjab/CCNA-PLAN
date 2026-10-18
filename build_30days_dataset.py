import json
from datetime import datetime, timedelta

with open(r'D:\CCNA III-PLAN\plan_data.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

sections_def = [
    {
        "code": "1.0",
        "name": "1.0 Network Fundamentals",
        "ar_name": "أساسيات الشبكات",
        "desc": "المفاهيم التأسيسية، أنواع الشبكات، الكوابل، البروتوكولات، ونموذج OSI و TCP/IP وPacket Tracer",
        "color": "sky",
        "start": 1,
        "end": 68,
        "study_days": 8
    },
    {
        "code": "2.0",
        "name": "2.0 Network Access",
        "ar_name": "الوصول إلى الشبكة والبنية التحتية",
        "desc": "الـ VLANs، الـ Trunking، بروتوكولات EtherChannel و LACP، الـ STP/RSTP، وشبكات الـ Wireless",
        "color": "indigo",
        "start": 69,
        "end": 101,
        "study_days": 4
    },
    {
        "code": "3.0",
        "name": "3.0 IP Connectivity",
        "ar_name": "التوجيه والاتصال الشبكي",
        "desc": "توجيه البيانات Routing، الـ Static Route، بروتوكول OSPF بالتفصيل، EIGRP، وبروتوكولات الـ FHRP و HSRP",
        "color": "emerald",
        "start": 102,
        "end": 144,
        "study_days": 5
    },
    {
        "code": "4.0",
        "name": "4.0 IP Services",
        "ar_name": "خدمات بروتوكول الإنترنت",
        "desc": "الـ NAT و PAT، خدمات DHCP، DNS، NTP، أنظمة المراقبة SNMP و Syslog، وجودة الخدمة QoS، و SSH",
        "color": "amber",
        "start": 145,
        "end": 169,
        "study_days": 4
    },
    {
        "code": "5.0",
        "name": "5.0 Security Fundamentals",
        "ar_name": "أساسيات أمن الشبكات",
        "desc": "المفاهيم الأمنية، جدران الحماية، الـ AAA، قوائم التحكم بالوصول ACLs، أمن المنافذ Port Security، و Wi-Fi Security",
        "color": "rose",
        "start": 170,
        "end": 199,
        "study_days": 3
    },
    {
        "code": "6.0",
        "name": "6.0 Automation and Programmability",
        "ar_name": "الأتمتة والبرمجة الشبكية",
        "desc": "مفاهيم الـ SDN، الـ APIs، تنسيقات JSON و XML، أدوات إدارة الإعدادات Ansible و Terraform، والذكاء الاصطناعي",
        "color": "purple",
        "start": 200,
        "end": 221,
        "study_days": 2
    }
]

def chunk_list(lst, n):
    total = len(lst)
    base = total // n
    rem = total % n
    res = []
    curr = 0
    for i in range(n):
        s = base + (1 if i < rem else 0)
        res.append(lst[curr : curr + s])
        curr += s
    return res

study_days = []
for sec in sections_def:
    sec_videos = items[sec['start']-1 : sec['end']]
    chunks = chunk_list(sec_videos, sec['study_days'])
    for idx, chunk in enumerate(chunks):
        study_days.append({
            "section_code": sec['code'],
            "section_name": sec['name'],
            "section_ar": sec['ar_name'],
            "section_color": sec['color'],
            "sec_day_index": idx + 1,
            "sec_total_days": sec['study_days'],
            "videos": chunk
        })

print(f"Total study days generated: {len(study_days)}")

start_date = datetime(2026, 10, 18)
calendar_days = []
study_idx = 0

for cal_day in range(1, 31):
    curr_date = start_date + timedelta(days=cal_day - 1)
    date_str = curr_date.strftime("%b %d, %Y")
    
    # Rest day is on day 7, 14, 21, 28
    if cal_day in [7, 14, 21, 28]:
        week_num = cal_day // 7
        calendar_days.append({
            "calendar_day": cal_day,
            "day_label": f"Day {cal_day}",
            "date": date_str,
            "is_rest_day": True,
            "title": f"يوم راحة ومراجعة أسبوعي (Week {week_num} Rest & Review)",
            "videos": []
        })
    else:
        sdata = study_days[study_idx]
        study_idx += 1
        calendar_days.append({
            "calendar_day": cal_day,
            "day_label": f"Day {cal_day}",
            "date": date_str,
            "is_rest_day": False,
            "study_day_num": study_idx,
            "section_code": sdata['section_code'],
            "section_name": sdata['section_name'],
            "section_ar": sdata['section_ar'],
            "section_color": sdata['section_color'],
            "sec_day_index": sdata['sec_day_index'],
            "sec_total_days": sdata['sec_total_days'],
            "videos": sdata['videos']
        })

print(f"Total calendar days: {len(calendar_days)}")
with open(r'D:\CCNA III-PLAN\plan_30days_data.json', 'w', encoding='utf-8') as out:
    json.dump(calendar_days, out, ensure_ascii=False, indent=2)

print("Saved plan_30days_data.json successfully!")
