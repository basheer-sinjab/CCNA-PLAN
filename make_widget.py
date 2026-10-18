import json, os

with open(r'D:\CCNA III-PLAN\plan_data.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Group by day summary
days_summary = {}
for item in items:
    d = item['day']
    if d not in days_summary:
        days_summary[d] = {
            'day': d,
            'date': item['date'],
            'count': 0,
            'duration': 0,
            'first_video': item['title'],
            'sample_url': item['url'],
            'sample_yt': item['ytId']
        }
    days_summary[d]['count'] += 1
    days_summary[d]['duration'] += item['durationMins']

days_list = list(days_summary.values())

html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {{
      font-family: 'Cairo', sans-serif;
      background: transparent;
      margin: 0;
      padding: 0;
    }}
    .font-num {{ font-family: 'Inter', sans-serif; }}
    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-track {{ background: rgba(15, 23, 42, 0.4); }}
    ::-webkit-scrollbar-thumb {{ background: rgba(56, 189, 248, 0.3); border-radius: 3px; }}
  </style>
</head>
<body class="text-slate-100 p-2 sm:p-4">
  <div class="max-w-4xl mx-auto space-y-5">
    
    <!-- Top Hero Card -->
    <div class="p-5 rounded-2xl bg-gradient-to-br from-slate-900/95 via-slate-900/80 to-slate-950 border border-slate-800 shadow-xl backdrop-blur-xl">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="flex items-center gap-3.5">
          <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-sky-600 to-emerald-500 flex items-center justify-center text-white text-xl font-black shadow-lg shadow-sky-600/30 shrink-0">
            <i class="fa-solid fa-network-wired"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded-full text-[11px] font-bold bg-sky-500/20 text-sky-400 border border-sky-500/30 font-num">CCNA 200-301 v1.1</span>
              <span class="px-2 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">2026 Plan</span>
            </div>
            <h2 class="text-xl sm:text-2xl font-black text-white mt-0.5">لوحة متابعة وإنجاز كورس سيسكو CCNA</h2>
          </div>
        </div>

        <div class="flex items-center gap-2 self-start sm:self-center">
          <a href="index.html" target="_blank" class="px-4 py-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs flex items-center gap-2 shadow-lg shadow-sky-600/30 transition">
            <i class="fa-solid fa-arrow-up-right-from-square"></i>
            <span>فتح التطبيق التفاعلي بالكامل</span>
          </a>
        </div>
      </div>

      <!-- Stats Grid -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-5 pt-4 border-t border-slate-800/80 text-center">
        <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
          <span class="text-[11px] text-slate-400 block mb-0.5 font-bold">إجمالي المقاطع</span>
          <span class="text-xl font-black text-white font-num">221</span>
          <span class="text-[10px] text-slate-500 block">فيديو تدريبي</span>
        </div>
        <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
          <span class="text-[11px] text-slate-400 block mb-0.5 font-bold">إجمالي الأيام</span>
          <span class="text-xl font-black text-emerald-400 font-num">25</span>
          <span class="text-[10px] text-slate-500 block">يوماً دراسياً</span>
        </div>
        <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
          <span class="text-[11px] text-slate-400 block mb-0.5 font-bold">المدة الكلية</span>
          <span class="text-xl font-black text-sky-400 font-num">~33.5</span>
          <span class="text-[10px] text-slate-500 block">ساعة تدريبية</span>
        </div>
        <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
          <span class="text-[11px] text-slate-400 block mb-0.5 font-bold">الحفظ والمزامنة</span>
          <span class="text-xl font-black text-purple-400 font-num">100%</span>
          <span class="text-[10px] text-slate-500 block">تخزين محلي فوري</span>
        </div>
      </div>
    </div>

    <!-- Live Preview Checklist for First 10 Videos -->
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 space-y-3">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2">
          <i class="fa-solid fa-list-check text-emerald-400"></i>
          <h3 class="text-sm font-bold text-white">معاينة تفاعلية سريعة (انقر لتجربة التحديد):</h3>
        </div>
        <span id="previewCounter" class="text-xs font-bold text-slate-400 font-num">0 / 8 مكتمل</span>
      </div>

      <div id="previewList" class="space-y-2 text-xs">
        <!-- Javascript renders sample items here -->
      </div>
    </div>

    <!-- 25-Day Roadmap Timeline -->
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 space-y-3">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2">
          <i class="fa-solid fa-calendar-days text-sky-400"></i>
          <h3 class="text-sm font-bold text-white">خريطة الأيام التدريبية الـ 25 (Roadmap):</h3>
        </div>
        <span class="text-[11px] text-slate-500">من 18 أكتوبر إلى 11 نوفمبر 2026</span>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-2 max-h-64 overflow-y-auto pr-1">
"""

for d in days_list:
    html_content += f"""
        <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800 hover:border-sky-500/50 transition">
          <div class="flex items-center justify-between">
            <span class="font-bold text-white font-num text-xs">{d['day']}</span>
            <span class="text-[10px] text-sky-400 font-num">{d['count']} دروس</span>
          </div>
          <span class="text-[10px] text-slate-500 block font-num mt-0.5">{d['date']}</span>
          <span class="text-[10px] text-slate-400 block font-num mt-1">⏱️ {d['duration']} دقيقة</span>
        </div>
    """

html_content += f"""
      </div>
    </div>

  </div>

  <script>
    const sampleVideos = {json.dumps(items[:8], ensure_ascii=False)};
    let checkedIds = new Set();

    function renderPreview() {{
      const list = document.getElementById('previewList');
      let html = '';
      sampleVideos.forEach(v => {{
        const isDone = checkedIds.has(v.id);
        html += `
          <div onclick="togglePreviewItem(${{v.id}})" class="p-2.5 rounded-xl border flex items-center justify-between gap-3 cursor-pointer transition ${{isDone ? 'bg-emerald-950/30 border-emerald-500/40 text-emerald-200' : 'bg-slate-950/60 border-slate-800 hover:border-slate-700 text-slate-300'}}">
            <div class="flex items-center gap-2.5 min-w-0">
              <div class="w-5 h-5 rounded-md flex items-center justify-center shrink-0 border ${{isDone ? 'bg-emerald-500 border-emerald-500 text-white' : 'border-slate-600 bg-slate-900'}}">
                ${{isDone ? '<i class="fa-solid fa-check text-[10px]"></i>' : ''}}
              </div>
              <span class="font-mono text-[10px] text-slate-400 font-num shrink-0">#${{v.id}}</span>
              <span class="truncate font-medium ${{isDone ? 'line-through text-slate-400' : ''}}">${{v.title}}</span>
            </div>
            <div class="flex items-center gap-2 shrink-0">
              <span class="text-[10px] font-num text-slate-400">⏱️ ${{v.duration}}</span>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold ${{isDone ? 'bg-emerald-500/20 text-emerald-300' : 'bg-amber-500/10 text-amber-400 font-num'}}">
                ${{isDone ? 'مكتمل' : 'Pending'}}
              </span>
            </div>
          </div>
        `;
      }});
      list.innerHTML = html;
      document.getElementById('previewCounter').textContent = `${{checkedIds.size}} / ${{sampleVideos.length}} مكتمل`;
    }}

    function togglePreviewItem(id) {{
      if (checkedIds.has(id)) checkedIds.delete(id);
      else checkedIds.add(id);
      renderPreview();
    }}

    renderPreview();
  </script>
</body>
</html>
"""

with open(r'D:\CCNA III-PLAN\widget.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Successfully created D:\\CCNA III-PLAN\\widget.html')
