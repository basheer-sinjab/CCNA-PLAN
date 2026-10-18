import json, os

with open(r'D:\CCNA III-PLAN\plan_30days_data.json', 'r', encoding='utf-8') as f:
    cal_days = json.load(f)

json_data_str = json.dumps(cal_days, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="ar" dir="rtl" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>خطة Cisco CCNA 200-301 v1.1 | خطة الـ 30 يوماً المقسمة على الأقسام الستة</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            cairo: ['Cairo', 'sans-serif'],
            inter: ['Inter', 'sans-serif']
          },
          colors: {
            cisco: {
              50: '#f0f9ff',
              100: '#e0f2fe',
              400: '#38bdf8',
              500: '#0ea5e9',
              600: '#0284c7',
              700: '#0369a1',
              900: '#0c4a6e',
            }
          }
        }
      }
    }
  </script>
  
  <!-- Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

  <style>
    body {
      font-family: 'Cairo', sans-serif;
      transition: background-color 0.3s ease, color 0.3s ease;
    }
    .font-num {
      font-family: 'Inter', sans-serif;
    }
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: rgba(15, 23, 42, 0.6);
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(56, 189, 248, 0.4);
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: rgba(56, 189, 248, 0.7);
    }
    .video-card-transition {
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .modal-enter {
      animation: modalFadeIn 0.2s ease-out forwards;
    }
    @keyframes modalFadeIn {
      from { opacity: 0; transform: scale(0.96); }
      to { opacity: 1; transform: scale(1); }
    }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen selection:bg-cisco-500 selection:text-white">

  <!-- Main Shell -->
  <div id="app" class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8 py-5 sm:py-8 space-y-6 sm:space-y-8">

    <!-- Version Switcher Bar -->
    <div class="flex items-center justify-between px-4 py-2.5 rounded-2xl bg-slate-900/60 border border-slate-800 text-xs">
      <div class="flex items-center gap-2">
        <span class="text-slate-400">أنت الآن في:</span>
        <span class="font-bold text-sky-400 bg-sky-500/10 px-2 py-0.5 rounded-md border border-sky-500/20">خطة الـ 30 يوماً (مقسمة بدقة على الأقسام الستة + أيام راحة أسبوعية)</span>
      </div>
      <a href="index.html" class="flex items-center gap-1.5 text-slate-400 hover:text-white font-bold transition">
        <span>الانتقال للنسخة الأصلية (25 يوماً)</span>
        <i class="fa-solid fa-arrow-left"></i>
      </a>
    </div>

    <!-- Header Banner -->
    <header class="flex flex-col md:flex-row items-center justify-between gap-5 p-5 sm:p-6 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-2xl backdrop-blur-xl">
      <div class="flex items-center gap-4 text-right">
        <div class="w-14 h-14 sm:w-16 sm:h-16 rounded-2xl bg-gradient-to-tr from-sky-600 via-indigo-600 to-emerald-400 flex items-center justify-center text-white shadow-xl shadow-sky-600/30 text-2xl sm:text-3xl font-black shrink-0">
          <i class="fa-solid fa-cubes-stacked"></i>
        </div>
        <div>
          <div class="flex flex-wrap items-center gap-2">
            <span class="px-3 py-0.5 rounded-full text-xs font-bold uppercase tracking-wider bg-cisco-500/20 text-cisco-300 border border-cisco-500/30 font-num">Cisco CCNA 200-301 v1.1</span>
            <span class="px-3 py-0.5 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">موزعة على الأقسام الـ 6</span>
            <span class="px-3 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">30 يوماً (مع أيام راحة)</span>
          </div>
          <h1 class="text-xl sm:text-3xl font-black text-white mt-1">خطة CCNA 200-301 المقسمة حسب المسارات الرسمية</h1>
          <p class="text-xs sm:text-sm text-slate-400 mt-0.5">كل قسم يبدأ وينتهي في أيامه الخاصة دون تداخل • 26 يوم دراسة + 4 أيام راحة واسترجاع أسبوعية</p>
        </div>
      </div>

      <!-- Quick Action Buttons -->
      <div class="flex flex-wrap items-center justify-center sm:justify-end gap-2.5 w-full md:w-auto">
        <button id="jumpNextBtn" onclick="jumpToNextPending()" class="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-cisco-600 hover:bg-cisco-500 text-white font-bold text-xs sm:text-sm shadow-lg shadow-cisco-600/30 transition active:scale-95">
          <i class="fa-solid fa-bolt text-yellow-300"></i>
          <span>الدرس التالي المطلوب</span>
        </button>

        <button onclick="exportUpdatedCSV()" title="تصدير ملف CSV محدث بحالة الإنجاز الحالية" class="flex items-center gap-2 px-3.5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700 text-xs sm:text-sm font-semibold transition active:scale-95">
          <i class="fa-solid fa-file-csv text-base"></i>
          <span>تصدير CSV محدث</span>
        </button>

        <button onclick="openBackupModal()" title="نسخ احتياطي أو استعادة" class="flex items-center gap-2 px-3 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs sm:text-sm font-medium transition active:scale-95">
          <i class="fa-solid fa-cloud-arrow-down text-cisco-400"></i>
          <span class="hidden sm:inline">نسخ / استعادة</span>
        </button>

        <button onclick="confirmReset()" title="إعادة تعيين التقدم بالكامل" class="p-2.5 rounded-xl bg-slate-800 hover:bg-rose-950/70 hover:text-rose-400 text-slate-400 border border-slate-700 transition active:scale-95">
          <i class="fa-solid fa-arrow-rotate-right"></i>
        </button>

        <button onclick="toggleTheme()" id="themeBtn" title="تبديل الوضع الليلي / الفاتح" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-400 border border-slate-700 transition active:scale-95">
          <i class="fa-solid fa-sun" id="themeIcon"></i>
        </button>
      </div>
    </header>

    <!-- General Stats Cards Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <div class="p-5 rounded-2xl bg-gradient-to-br from-slate-900 to-slate-900/90 border border-slate-800 shadow-xl flex flex-col justify-between">
        <div class="flex items-center justify-between mb-3">
          <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">نسبة الإنجاز الإجمالية</span>
          <span id="badgeMotivational" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cisco-500/20 text-cisco-400 border border-cisco-500/30">ابدأ الآن 🚀</span>
        </div>
        <div>
          <div class="flex items-baseline gap-2">
            <span id="statPercent" class="text-4xl sm:text-5xl font-black text-white font-num tracking-tight">0%</span>
            <span class="text-xs text-slate-400 font-num">من الكورس كاملاً</span>
          </div>
          <div class="w-full h-3 bg-slate-800 rounded-full mt-3 overflow-hidden p-0.5 border border-slate-700/60">
            <div id="statProgressBar" class="h-full bg-gradient-to-r from-sky-500 via-indigo-400 to-emerald-400 rounded-full transition-all duration-500" style="width: 0%"></div>
          </div>
        </div>
      </div>

      <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl flex items-center justify-between">
        <div>
          <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-1">المقاطع المنجزة</span>
          <div class="flex items-baseline gap-1.5 font-num">
            <span id="statCompletedCount" class="text-3xl sm:text-4xl font-black text-emerald-400">0</span>
            <span class="text-slate-500 text-lg">/</span>
            <span class="text-slate-400 font-bold text-lg font-num">221</span>
          </div>
          <span id="statPendingCount" class="text-xs text-amber-400/90 font-medium mt-1.5 block">المتبقي: 221 مقطع</span>
        </div>
        <div class="w-14 h-14 rounded-2xl bg-emerald-500/10 border border-emerald-500/25 flex items-center justify-center text-emerald-400 text-2xl shadow-inner">
          <i class="fa-solid fa-circle-check"></i>
        </div>
      </div>

      <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl flex items-center justify-between">
        <div>
          <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-1">الوقت المشاهد</span>
          <div class="flex items-baseline gap-1.5 font-num">
            <span id="statCompletedHours" class="text-3xl sm:text-4xl font-black text-cisco-400">0.0</span>
            <span class="text-slate-500 text-xs">من</span>
            <span class="text-slate-400 font-bold text-sm">33.5 ساعة</span>
          </div>
          <span id="statRemainingHours" class="text-xs text-slate-400 mt-1.5 block font-num">المتبقي: ~33.5 ساعة</span>
        </div>
        <div class="w-14 h-14 rounded-2xl bg-cisco-500/10 border border-cisco-500/25 flex items-center justify-center text-cisco-400 text-2xl shadow-inner">
          <i class="fa-solid fa-clock"></i>
        </div>
      </div>

      <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl flex items-center justify-between">
        <div>
          <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-1">الأقسام المكتملة</span>
          <div class="flex items-baseline gap-1.5 font-num">
            <span id="statCompletedSections" class="text-3xl sm:text-4xl font-black text-purple-400">0</span>
            <span class="text-slate-500 text-lg">/</span>
            <span class="text-slate-400 font-bold text-lg">6 أقسام</span>
          </div>
          <span id="statDaysCount" class="text-xs text-slate-400 mt-1.5 block font-num">26 يوم دراسة + 4 راحة</span>
        </div>
        <div class="w-14 h-14 rounded-2xl bg-purple-500/10 border border-purple-500/25 flex items-center justify-center text-purple-400 text-2xl shadow-inner">
          <i class="fa-solid fa-layer-group"></i>
        </div>
      </div>
    </div>

    <!-- The 6 Cisco Sections Executive Dashboard Grid -->
    <div class="p-5 sm:p-6 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
          <h2 class="text-base sm:text-lg font-black text-white flex items-center gap-2">
            <i class="fa-solid fa-shapes text-sky-400"></i>
            <span>لوحة تقدم الأقسام الستة (The 6 CCNA Modules Breakdown)</span>
          </h2>
          <p class="text-xs text-slate-400 mt-0.5">انقر على أي قسم لتصفيته مباشرة وعرض أيامه ودروسه فقط</p>
        </div>
        <button onclick="filterBySection(null)" class="text-xs text-sky-400 hover:underline font-bold self-start sm:self-center">
          عرض جميع الأقسام
        </button>
      </div>

      <!-- 6 Sections Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3.5" id="sectionsCardsGrid">
        <!-- Rendered by JS -->
      </div>
    </div>

    <!-- Celebration Banner -->
    <div id="congratsBanner" class="hidden p-6 rounded-3xl bg-gradient-to-r from-emerald-600 via-teal-600 to-cisco-600 text-white shadow-2xl relative overflow-hidden">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-4 text-center sm:text-right">
          <div class="text-5xl">🏆🎓</div>
          <div>
            <h2 class="text-2xl font-black">ألف مبروك! أتممت خطة كورس CCNA 200-301 بالكامل عبر الأقسام الستة!</h2>
            <p class="text-sm text-emerald-100 mt-1">أنت الآن جاهز للاختبار الدولي وحصد الشهادة بجدارة. بالتوفيق الدائم!</p>
          </div>
        </div>
        <button onclick="triggerConfetti(true)" class="px-5 py-2.5 rounded-xl bg-white text-slate-900 font-bold text-sm shadow hover:bg-emerald-50 transition active:scale-95 flex items-center gap-2 shrink-0">
          <i class="fa-solid fa-champagne-glasses text-emerald-600"></i>
          <span>إطلاق الاحتفال مجدداً</span>
        </button>
      </div>
    </div>

    <!-- Controls, Filter & Search Panel -->
    <div class="p-5 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
      
      <!-- Top Row: Search + Status Tabs + Expand/Collapse -->
      <div class="flex flex-col lg:flex-row items-stretch lg:items-center justify-between gap-4">
        
        <!-- Search Field -->
        <div class="relative flex-1">
          <i class="fa-solid fa-magnifying-glass absolute right-4 top-1/2 -translate-y-1/2 text-slate-400"></i>
          <input 
            type="text" 
            id="searchInput" 
            oninput="handleSearch(this.value)" 
            placeholder="ابحث في عناوين المقاطع، رقم اليوم، القسم (1.0, 2.0, 3.0...) أو المفاهيم..." 
            class="w-full pr-11 pl-10 py-3 rounded-2xl bg-slate-950/70 border border-slate-700/80 text-white placeholder-slate-400 text-sm focus:outline-none focus:border-cisco-500 focus:ring-1 focus:ring-cisco-500 transition"
          >
          <button id="clearSearchBtn" onclick="clearSearch()" class="hidden absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white p-1">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>

        <!-- Status Filter Tabs -->
        <div class="flex items-center gap-1.5 p-1 rounded-2xl bg-slate-950/80 border border-slate-800 text-xs sm:text-sm font-bold self-start lg:self-center">
          <button onclick="setStatusFilter('all')" id="filterAll" class="filter-tab px-3.5 py-2 rounded-xl bg-cisco-600 text-white transition">الكل (<span id="countAllTab" class="font-num">221</span>)</button>
          <button onclick="setStatusFilter('pending')" id="filterPending" class="filter-tab px-3.5 py-2 rounded-xl text-slate-400 hover:text-white transition">⏳ قيد الانتظار (<span id="countPendingTab" class="font-num">221</span>)</button>
          <button onclick="setStatusFilter('completed')" id="filterCompleted" class="filter-tab px-3.5 py-2 rounded-xl text-slate-400 hover:text-white transition">✅ المكتملة (<span id="countCompletedTab" class="font-num">0</span>)</button>
        </div>

        <!-- Accordions Toggle -->
        <div class="flex items-center gap-2 self-end lg:self-center">
          <button onclick="toggleAllAccordions(true)" title="توسيع كافة الأيام" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 flex items-center gap-1.5 transition">
            <i class="fa-solid fa-chevron-down"></i>
            <span>فتح الكل</span>
          </button>
          <button onclick="toggleAllAccordions(false)" title="طي كافة الأيام" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 flex items-center gap-1.5 transition">
            <i class="fa-solid fa-chevron-up"></i>
            <span>طي الكل</span>
          </button>
        </div>

      </div>

      <!-- 30 Days Timeline Pills -->
      <div class="border-t border-slate-800 pt-3">
        <div class="flex items-center justify-between text-xs text-slate-400 mb-2">
          <span class="flex items-center gap-1.5 font-bold">
            <i class="fa-solid fa-calendar-days text-sky-400"></i>
            <span>الجدول الزمني الكامل (Day 1 إلى Day 30):</span>
          </span>
          <span class="text-[11px] text-slate-500 hidden sm:inline">أيام الراحة الأسبوعية (7، 14، 21، 28) محددة برمز ☕</span>
        </div>
        <div id="dayPillsContainer" class="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none">
          <!-- Populated by JS -->
        </div>
      </div>

    </div>

    <!-- Active Filter Notification -->
    <div id="activeFilterAlert" class="hidden flex items-center justify-between px-5 py-3 rounded-2xl bg-cisco-900/40 border border-cisco-600/50 text-cisco-200 text-xs sm:text-sm">
      <div class="flex items-center gap-2">
        <i class="fa-solid fa-filter text-cisco-400"></i>
        <span id="activeFilterText">تصفية مفعّلة</span>
      </div>
      <button onclick="resetFilters()" class="text-xs text-cisco-300 hover:underline font-bold">إلغاء التصفية وعرض الكل</button>
    </div>

    <!-- Main Content Container: Grouped Days & Videos -->
    <main id="videosContainer" class="space-y-6">
      <!-- Injected by JavaScript -->
    </main>

    <!-- Empty State -->
    <div id="emptyState" class="hidden text-center py-16 px-4 bg-slate-900/40 rounded-3xl border border-slate-800">
      <div class="w-16 h-16 mx-auto mb-4 rounded-full bg-slate-800 flex items-center justify-center text-slate-400 text-2xl">
        <i class="fa-solid fa-magnifying-glass"></i>
      </div>
      <h3 class="text-lg font-bold text-slate-200">لم يتم العثور على مقاطع مطابقة لبحثك</h3>
      <p class="text-sm text-slate-400 mt-1">جرّب البحث بكلمة أخرى أو قم بإلغاء الفلاتر المحددة</p>
      <button onclick="resetFilters()" class="mt-4 px-5 py-2.5 rounded-xl bg-cisco-600 text-white text-xs font-bold hover:bg-cisco-500 transition">
        إعادة تعيين الفلاتر
      </button>
    </div>

    <!-- Footer -->
    <footer class="pt-8 pb-12 text-center text-xs text-slate-500 border-t border-slate-800/80 space-y-2">
      <div class="flex items-center justify-center gap-2">
        <span>خطة دراسة وتتبع Cisco CCNA 200-301 (v1.1) - خطة الـ 30 يوماً المقسمة على الأقسام الستة</span>
        <span>•</span>
        <span>حفظ تلقائي لتقدمك وملاحظاتك في المتصفح</span>
      </div>
      <p>كل قسم دراسي ينتهي قبل البدء في القسم التالي بدون أي تداخل</p>
    </footer>

  </div>

  <!-- Video Modal (YouTube Embedded Player) -->
  <div id="videoModal" class="fixed inset-0 z-50 hidden bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-3 sm:p-4">
    <div class="bg-slate-900 border border-slate-800 rounded-3xl w-full max-w-4xl overflow-hidden shadow-2xl modal-enter flex flex-col">
      <div class="flex items-center justify-between p-4 sm:p-5 border-b border-slate-800 bg-slate-950/60">
        <div class="flex items-center gap-3 overflow-hidden">
          <div class="w-10 h-10 rounded-xl bg-red-600/20 text-red-500 flex items-center justify-center shrink-0">
            <i class="fa-brands fa-youtube text-xl"></i>
          </div>
          <div class="truncate">
            <h3 id="modalVideoTitle" class="text-sm sm:text-base font-bold text-white truncate">عنوان الفيديو</h3>
            <span id="modalVideoMeta" class="text-xs text-slate-400 font-num">Day 1 • Oct 18, 2026 • 14m</span>
          </div>
        </div>
        <button onclick="closeVideoModal()" class="text-slate-400 hover:text-white p-2 rounded-xl hover:bg-slate-800 transition">
          <i class="fa-solid fa-xmark text-lg"></i>
        </button>
      </div>

      <div class="relative w-full aspect-video bg-black">
        <iframe 
          id="videoIframe" 
          class="w-full h-full" 
          src="" 
          title="YouTube video player" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
          allowfullscreen
        ></iframe>
      </div>

      <div class="flex flex-wrap items-center justify-between gap-3 p-4 border-t border-slate-800 bg-slate-950/50">
        <button id="modalToggleCompleteBtn" onclick="toggleCurrentModalVideo()" class="px-4 py-2.5 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition active:scale-95">
          <i class="fa-solid fa-check"></i>
          <span>تحديد كمكتمل</span>
        </button>

        <div class="flex items-center gap-2">
          <button id="modalPrevBtn" onclick="navigateModalVideo(-1)" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold transition flex items-center gap-1.5">
            <i class="fa-solid fa-arrow-right"></i>
            <span>السابق</span>
          </button>
          <button id="modalNextBtn" onclick="navigateModalVideo(1)" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold transition flex items-center gap-1.5">
            <span>التالي</span>
            <i class="fa-solid fa-arrow-left"></i>
          </button>
          <a id="modalExternalLink" href="#" target="_blank" rel="noopener noreferrer" class="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-cisco-400 text-xs font-bold transition flex items-center gap-1.5">
            <i class="fa-solid fa-arrow-up-right-from-square"></i>
            <span>يوتيوب</span>
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- Notes Modal -->
  <div id="notesModal" class="fixed inset-0 z-50 hidden bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-800 rounded-3xl w-full max-w-lg overflow-hidden shadow-2xl modal-enter">
      <div class="p-4 sm:p-5 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
        <div class="flex items-center gap-2 text-white font-bold text-sm sm:text-base">
          <i class="fa-solid fa-pen-to-square text-cisco-400"></i>
          <span>ملاحظات الدرس الشخصية</span>
        </div>
        <button onclick="closeNotesModal()" class="text-slate-400 hover:text-white p-1.5 rounded-xl hover:bg-slate-800">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <div class="p-5 space-y-3">
        <div class="text-xs text-slate-300 font-semibold" id="notesVideoTitle">عنوان الدرس</div>
        <textarea 
          id="noteTextArea" 
          rows="6" 
          placeholder="سجّل هنا أهم الأوامر، المفاهيم، أو الملاحظات التي تحتاج مراجعتها..." 
          class="w-full p-3.5 rounded-2xl bg-slate-950 border border-slate-700 text-white placeholder-slate-500 text-sm focus:outline-none focus:border-cisco-500 focus:ring-1 focus:ring-cisco-500"
        ></textarea>
        <div class="text-[11px] text-slate-400">يتم حفظ الملاحظات محلياً في متصفحك وتبقى دائماً.</div>
      </div>
      <div class="p-4 border-t border-slate-800 flex justify-end gap-2 bg-slate-950/50">
        <button onclick="closeNotesModal()" class="px-4 py-2 rounded-xl text-slate-400 hover:text-white text-xs font-semibold">إلغاء</button>
        <button onclick="saveNote()" class="px-5 py-2 rounded-xl bg-cisco-600 hover:bg-cisco-500 text-white text-xs font-bold shadow">حفظ الملاحظة</button>
      </div>
    </div>
  </div>

  <!-- Backup & Restore Modal -->
  <div id="backupModal" class="fixed inset-0 z-50 hidden bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-800 rounded-3xl w-full max-w-md overflow-hidden shadow-2xl modal-enter">
      <div class="p-4 sm:p-5 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
        <div class="flex items-center gap-2 text-white font-bold text-sm sm:text-base">
          <i class="fa-solid fa-database text-cisco-400"></i>
          <span>النسخ الاحتياطي والاستعادة</span>
        </div>
        <button onclick="closeBackupModal()" class="text-slate-400 hover:text-white p-1.5 rounded-xl hover:bg-slate-800">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <div class="p-5 space-y-5">
        <div>
          <h4 class="text-xs font-bold text-slate-300 uppercase mb-1">تصدير نسخة احتياطية (JSON)</h4>
          <p class="text-xs text-slate-400 mb-2.5">تحميل ملف JSON يشمل كافة المقاطع التي قمت بإنجازها مع ملاحظاتك الخاصة.</p>
          <button onclick="downloadBackupJSON()" class="w-full py-2.5 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 text-cisco-400 border border-slate-700 text-xs font-bold flex items-center justify-center gap-2 transition">
            <i class="fa-solid fa-download"></i>
            <span>تحميل ملف النسخة الاحتياطية</span>
          </button>
        </div>

        <div class="border-t border-slate-800 pt-4">
          <h4 class="text-xs font-bold text-slate-300 uppercase mb-1">استعادة نسخة سابقة</h4>
          <p class="text-xs text-slate-400 mb-2.5">اختر ملف JSON محفوظ سابقاً لاستعادة تقدمك فوراً.</p>
          <input type="file" id="restoreFileInput" accept=".json" class="hidden" onchange="handleRestoreFile(event)">
          <button onclick="document.getElementById('restoreFileInput').click()" class="w-full py-2.5 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700 text-xs font-bold flex items-center justify-center gap-2 transition">
            <i class="fa-solid fa-upload"></i>
            <span>اختيار ملف JSON للاستعادة</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- JavaScript Logic -->
  <script>
    const CALENDAR_DATA = """ + json_data_str + """;

    // Flatten all videos for quick lookup
    const ALL_VIDEOS = [];
    CALENDAR_DATA.forEach(d => {
      if (!d.is_rest_day && d.videos) {
        d.videos.forEach(v => {
          ALL_VIDEOS.push({
            ...v,
            calendar_day: d.calendar_day,
            day_label: d.day_label,
            date: d.date,
            section_code: d.section_code,
            section_name: d.section_name,
            section_ar: d.section_ar,
            section_color: d.section_color
          });
        });
      }
    });

    // 6 Sections Definition
    const SECTIONS_META = [
      { code: "1.0", name: "1.0 Network Fundamentals", ar: "أساسيات الشبكات", color: "sky", days: "Day 1 - Day 8 (8 أيام)", total_videos: 68 },
      { code: "2.0", name: "2.0 Network Access", ar: "الوصول إلى الشبكة والبنية", color: "indigo", days: "Day 9 - Day 12 (4 أيام)", total_videos: 33 },
      { code: "3.0", name: "3.0 IP Connectivity", ar: "التوجيه والاتصال الشبكي", color: "emerald", days: "Day 13 - Day 18 (5 أيام)", total_videos: 43 },
      { code: "4.0", name: "4.0 IP Services", ar: "خدمات بروتوكول الإنترنت", color: "amber", days: "Day 19 - Day 22 (4 أيام)", total_videos: 25 },
      { code: "5.0", name: "5.0 Security Fundamentals", ar: "أساسيات أمن الشبكات", color: "rose", days: "Day 23 - Day 26 (3 أيام)", total_videos: 30 },
      { code: "6.0", name: "6.0 Automation and Programmability", ar: "الأتمتة والبرمجة الشبكية", color: "purple", days: "Day 27 - Day 30 (2 أيام)", total_videos: 22 }
    ];

    let completedSet = new Set();
    let notesMap = {};
    let collapsedDays = new Set();
    let currentFilter = 'all'; // 'all', 'pending', 'completed'
    let selectedDayFilter = null; // null or calendar_day number
    let selectedSectionFilter = null; // null or "1.0", "2.0"...
    let searchQuery = '';
    let activeModalVideoId = null;

    const STORAGE_KEY_COMPLETED = 'ccna_30days_completed_ids_v1';
    const STORAGE_KEY_NOTES = 'ccna_30days_notes_v1';
    const STORAGE_KEY_THEME = 'ccna_30days_theme_v1';

    function initApp() {
      loadState();
      applyTheme();
      renderSectionCards();
      renderDayPills();
      render();
      updateStats();
    }

    function loadState() {
      try {
        const saved = localStorage.getItem(STORAGE_KEY_COMPLETED);
        if (saved) {
          completedSet = new Set(JSON.parse(saved));
        }
        const savedNotes = localStorage.getItem(STORAGE_KEY_NOTES);
        if (savedNotes) {
          notesMap = JSON.parse(savedNotes);
        }
      } catch (e) {
        console.error('Error loading state:', e);
      }
    }

    function saveState() {
      try {
        localStorage.setItem(STORAGE_KEY_COMPLETED, JSON.stringify(Array.from(completedSet)));
        localStorage.setItem(STORAGE_KEY_NOTES, JSON.stringify(notesMap));
      } catch (e) {
        console.error('Error saving state:', e);
      }
    }

    function toggleVideo(id, event) {
      if (event) event.stopPropagation();
      const wasCompleted = completedSet.has(id);
      
      if (wasCompleted) {
        completedSet.delete(id);
      } else {
        completedSet.add(id);
      }
      
      saveState();
      updateStats();
      render();

      const video = ALL_VIDEOS.find(v => v.id === id);
      if (!wasCompleted && video) {
        checkDayAndSectionCompletion(video);
      }
    }

    function checkDayAndSectionCompletion(video) {
      // Check day completion
      const dayData = CALENDAR_DATA.find(d => d.calendar_day === video.calendar_day);
      if (dayData && !dayData.is_rest_day) {
        const allDayDone = dayData.videos.every(v => completedSet.has(v.id));
        if (allDayDone) triggerConfetti(false);
      }

      // Check section completion
      const secVideos = ALL_VIDEOS.filter(v => v.section_code === video.section_code);
      const allSecDone = secVideos.every(v => completedSet.has(v.id));
      if (allSecDone && secVideos.length > 0) {
        triggerConfetti(false);
      }

      if (completedSet.size === ALL_VIDEOS.length) {
        triggerConfetti(true);
      }
    }

    function toggleDayAll(calDayNum, event) {
      if (event) event.stopPropagation();
      const dayData = CALENDAR_DATA.find(d => d.calendar_day === calDayNum);
      if (!dayData || dayData.is_rest_day) return;

      const allDone = dayData.videos.every(v => completedSet.has(v.id));

      if (allDone) {
        dayData.videos.forEach(v => completedSet.delete(v.id));
      } else {
        dayData.videos.forEach(v => completedSet.add(v.id));
        triggerConfetti(false);
      }

      saveState();
      updateStats();
      render();
    }

    function toggleSectionAll(secCode, event) {
      if (event) event.stopPropagation();
      const secVideos = ALL_VIDEOS.filter(v => v.section_code === secCode);
      const allDone = secVideos.every(v => completedSet.has(v.id));

      if (allDone) {
        secVideos.forEach(v => completedSet.delete(v.id));
      } else {
        secVideos.forEach(v => completedSet.add(v.id));
        triggerConfetti(false);
      }

      saveState();
      updateStats();
      render();
    }

    function triggerConfetti(massive = false) {
      if (typeof confetti === 'function') {
        if (massive) {
          const end = Date.now() + 3 * 1000;
          const colors = ['#0ea5e9', '#6366f1', '#10b981', '#f59e0b', '#ec4899'];
          (function frame() {
            confetti({ particleCount: 5, angle: 60, spread: 55, origin: { x: 0 }, colors: colors });
            confetti({ particleCount: 5, angle: 120, spread: 55, origin: { x: 1 }, colors: colors });
            if (Date.now() < end) requestAnimationFrame(frame);
          }());
        } else {
          confetti({ particleCount: 75, spread: 65, origin: { y: 0.7 } });
        }
      }
    }

    function renderSectionCards() {
      const container = document.getElementById('sectionsCardsGrid');
      let html = '';

      SECTIONS_META.forEach(sec => {
        const secVideos = ALL_VIDEOS.filter(v => v.section_code === sec.code);
        const done = secVideos.filter(v => completedSet.has(v.id)).length;
        const total = secVideos.length;
        const pct = Math.round((done / total) * 100);
        const isComplete = done === total && total > 0;
        const isSelected = selectedSectionFilter === sec.code;

        let colorBorder = 'border-slate-800';
        let colorBg = 'bg-slate-950/70 hover:border-sky-500/50';
        if (isSelected) {
          colorBg = 'bg-slate-900 border-sky-400 ring-2 ring-sky-400/50 shadow-lg';
        } else if (isComplete) {
          colorBg = 'bg-emerald-950/40 border-emerald-500/40';
        }

        html += `
          <div onclick="filterBySection('${sec.code}')" class="p-4 rounded-2xl border ${colorBg} cursor-pointer transition flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-1.5">
                <span class="px-2.5 py-0.5 rounded-full text-[11px] font-bold uppercase tracking-wider bg-slate-800 text-sky-400 font-num">${sec.code}</span>
                <span class="text-[11px] text-slate-400 font-num">${sec.days}</span>
              </div>
              <h3 class="text-sm font-bold text-white">${sec.name}</h3>
              <p class="text-xs text-slate-400 mt-0.5">${sec.ar}</p>
            </div>

            <div class="mt-4 pt-3 border-t border-slate-800/80">
              <div class="flex items-center justify-between text-xs font-num mb-1.5">
                <span class="text-slate-400">${done}/${total} مقطع</span>
                <span class="font-bold ${isComplete ? 'text-emerald-400' : 'text-sky-400'}">${pct}%</span>
              </div>
              <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                <div class="h-full bg-gradient-to-r from-sky-500 to-emerald-400 transition-all duration-300" style="width: ${pct}%"></div>
              </div>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function renderDayPills() {
      const container = document.getElementById('dayPillsContainer');
      let html = `
        <button onclick="filterByDay(null)" class="day-pill px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 transition ${selectedDayFilter === null ? 'bg-cisco-600 text-white shadow' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'}">
          جميع الأيام (30)
        </button>
      `;

      CALENDAR_DATA.forEach(d => {
        const isSelected = selectedDayFilter === d.calendar_day;
        if (d.is_rest_day) {
          html += `
            <button onclick="filterByDay(${d.calendar_day})" class="day-pill px-3 py-1.5 rounded-xl text-xs font-semibold shrink-0 transition flex items-center gap-1.5 ${isSelected ? 'bg-amber-600 text-white ring-2 ring-amber-400' : 'bg-amber-950/60 border border-amber-600/30 text-amber-300 hover:bg-amber-900/60'}">
              <span>☕ ${d.day_label}</span>
              <span class="text-[10px] opacity-75">راحة</span>
            </button>
          `;
        } else {
          const dayDone = d.videos.filter(v => completedSet.has(v.id)).length;
          const isComplete = dayDone === d.videos.length && d.videos.length > 0;
          let badgeClass = 'bg-slate-800 text-slate-300 hover:bg-slate-700';
          if (isSelected) {
            badgeClass = 'bg-cisco-600 text-white shadow ring-2 ring-cisco-400';
          } else if (isComplete) {
            badgeClass = 'bg-emerald-950/80 border border-emerald-600/50 text-emerald-400';
          }

          html += `
            <button onclick="filterByDay(${d.calendar_day})" class="day-pill px-3 py-1.5 rounded-xl text-xs font-semibold shrink-0 transition flex items-center gap-1.5 ${badgeClass}">
              <span class="font-num">${d.day_label}</span>
              ${isComplete ? '<i class="fa-solid fa-check text-[10px]"></i>' : `<span class="text-[10px] opacity-75 font-num">${dayDone}/${d.videos.length}</span>`}
            </button>
          `;
        }
      });

      container.innerHTML = html;
    }

    function filterBySection(secCode) {
      if (selectedSectionFilter === secCode) {
        selectedSectionFilter = null;
      } else {
        selectedSectionFilter = secCode;
        selectedDayFilter = null;
      }
      renderSectionCards();
      renderDayPills();
      updateFilterAlert();
      render();
    }

    function filterByDay(calDay) {
      selectedDayFilter = calDay;
      if (calDay !== null) selectedSectionFilter = null;
      renderSectionCards();
      renderDayPills();
      updateFilterAlert();
      render();
      if (calDay) {
        const el = document.getElementById(`cal-day-section-${calDay}`);
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    function setStatusFilter(status) {
      currentFilter = status;
      document.querySelectorAll('.filter-tab').forEach(btn => {
        btn.classList.remove('bg-cisco-600', 'text-white');
        btn.classList.add('text-slate-400');
      });
      const activeBtn = document.getElementById(`filter${status.charAt(0).toUpperCase() + status.slice(1)}`);
      if (activeBtn) {
        activeBtn.classList.add('bg-cisco-600', 'text-white');
        activeBtn.classList.remove('text-slate-400');
      }
      updateFilterAlert();
      render();
    }

    function handleSearch(val) {
      searchQuery = val.trim().toLowerCase();
      const clearBtn = document.getElementById('clearSearchBtn');
      if (searchQuery) {
        clearBtn.classList.remove('hidden');
      } else {
        clearBtn.classList.add('hidden');
      }
      updateFilterAlert();
      render();
    }

    function clearSearch() {
      document.getElementById('searchInput').value = '';
      searchQuery = '';
      document.getElementById('clearSearchBtn').classList.add('hidden');
      updateFilterAlert();
      render();
    }

    function resetFilters() {
      searchQuery = '';
      document.getElementById('searchInput').value = '';
      document.getElementById('clearSearchBtn').classList.add('hidden');
      currentFilter = 'all';
      selectedDayFilter = null;
      selectedSectionFilter = null;
      setStatusFilter('all');
      renderSectionCards();
      renderDayPills();
      updateFilterAlert();
      render();
    }

    function updateFilterAlert() {
      const alert = document.getElementById('activeFilterAlert');
      const text = document.getElementById('activeFilterText');
      const isFiltered = searchQuery !== '' || currentFilter !== 'all' || selectedDayFilter !== null || selectedSectionFilter !== null;
      if (isFiltered) {
        alert.classList.remove('hidden');
        let parts = [];
        if (searchQuery) parts.push(`بحث: "${searchQuery}"`);
        if (currentFilter === 'pending') parts.push('الحالة: قيد الانتظار');
        if (currentFilter === 'completed') parts.push('الحالة: المكتملة');
        if (selectedSectionFilter) parts.push(`القسم: ${selectedSectionFilter}`);
        if (selectedDayFilter) parts.push(`اليوم: Day ${selectedDayFilter}`);
        text.textContent = 'تصفية نشطة: ' + parts.join(' • ');
      } else {
        alert.classList.add('hidden');
      }
    }

    function toggleDayAccordion(calDayNum) {
      if (collapsedDays.has(calDayNum)) {
        collapsedDays.delete(calDayNum);
      } else {
        collapsedDays.add(calDayNum);
      }
      render();
    }

    function toggleAllAccordions(expand) {
      if (expand) {
        collapsedDays.clear();
      } else {
        CALENDAR_DATA.forEach(d => collapsedDays.add(d.calendar_day));
      }
      render();
    }

    function jumpToNextPending() {
      const nextPending = ALL_VIDEOS.find(v => !completedSet.has(v.id));
      if (!nextPending) {
        alert('تهانينا! لقد أتممت جميع الدروس بنجاح.');
        return;
      }
      if (currentFilter === 'completed') setStatusFilter('all');
      if (selectedSectionFilter && selectedSectionFilter !== nextPending.section_code) {
        selectedSectionFilter = null;
      }
      if (selectedDayFilter && selectedDayFilter !== nextPending.calendar_day) {
        selectedDayFilter = null;
      }
      collapsedDays.delete(nextPending.calendar_day);
      renderSectionCards();
      renderDayPills();
      render();

      setTimeout(() => {
        const row = document.getElementById(`video-row-${nextPending.id}`);
        if (row) {
          row.scrollIntoView({ behavior: 'smooth', block: 'center' });
          row.classList.add('ring-4', 'ring-cisco-400', 'bg-cisco-900/40');
          setTimeout(() => {
            row.classList.remove('ring-4', 'ring-cisco-400', 'bg-cisco-900/40');
          }, 2500);
        }
      }, 100);
    }

    function updateStats() {
      const total = ALL_VIDEOS.length;
      const completed = completedSet.size;
      const pending = total - completed;
      const pct = Math.round((completed / total) * 100);

      let completedMins = 0;
      ALL_VIDEOS.forEach(v => {
        if (completedSet.has(v.id)) completedMins += v.durationMins;
      });
      const totalMins = 2011;
      const remainingMins = totalMins - completedMins;

      // Section completion check
      let completedSecCount = 0;
      SECTIONS_META.forEach(s => {
        const secVids = ALL_VIDEOS.filter(v => v.section_code === s.code);
        if (secVids.length > 0 && secVids.every(v => completedSet.has(v.id))) {
          completedSecCount++;
        }
      });

      document.getElementById('statPercent').textContent = `${pct}%`;
      document.getElementById('statProgressBar').style.width = `${pct}%`;
      document.getElementById('statCompletedCount').textContent = completed;
      document.getElementById('statPendingCount').textContent = `المتبقي: ${pending} مقطع`;
      
      document.getElementById('statCompletedHours').textContent = (completedMins / 60).toFixed(1);
      document.getElementById('statRemainingHours').textContent = `المتبقي: ~${(remainingMins / 60).toFixed(1)} ساعة`;

      document.getElementById('statCompletedSections').textContent = completedSecCount;

      document.getElementById('countAllTab').textContent = total;
      document.getElementById('countPendingTab').textContent = pending;
      document.getElementById('countCompletedTab').textContent = completed;

      const badge = document.getElementById('badgeMotivational');
      if (pct === 0) badge.textContent = 'ابدأ الآن 🚀';
      else if (pct <= 25) badge.textContent = 'بداية قوية 💪';
      else if (pct <= 50) badge.textContent = 'تقدم رائع 🎯';
      else if (pct <= 75) badge.textContent = 'أكثر من النصف 🌟';
      else if (pct < 100) badge.textContent = 'اللمسات الأخيرة 🏆';
      else badge.textContent = 'تم الإنجاز بالكامل! 🎓';

      const banner = document.getElementById('congratsBanner');
      if (pct === 100) {
        banner.classList.remove('hidden');
      } else {
        banner.classList.add('hidden');
      }

      renderSectionCards();
      renderDayPills();
    }

    function render() {
      const container = document.getElementById('videosContainer');
      const emptyState = document.getElementById('emptyState');

      let visibleDays = CALENDAR_DATA.filter(d => {
        if (selectedDayFilter && d.calendar_day !== selectedDayFilter) return false;
        if (selectedSectionFilter && !d.is_rest_day && d.section_code !== selectedSectionFilter) return false;
        if (selectedSectionFilter && d.is_rest_day) return false;

        if (d.is_rest_day) {
          if (currentFilter !== 'all') return false;
          if (searchQuery && !d.title.toLowerCase().includes(searchQuery) && !d.day_label.toLowerCase().includes(searchQuery)) {
            return false;
          }
          return true;
        }

        // For study days, check if any videos pass the status & search filters
        const matchingVideos = d.videos.filter(v => {
          const isDone = completedSet.has(v.id);
          if (currentFilter === 'pending' && isDone) return false;
          if (currentFilter === 'completed' && !isDone) return false;

          if (searchQuery) {
            const matchTitle = v.title.toLowerCase().includes(searchQuery);
            const matchDay = d.day_label.toLowerCase().includes(searchQuery);
            const matchSec = d.section_name.toLowerCase().includes(searchQuery);
            if (!matchTitle && !matchDay && !matchSec) return false;
          }
          return true;
        });

        return matchingVideos.length > 0;
      });

      if (visibleDays.length === 0) {
        container.innerHTML = '';
        emptyState.classList.remove('hidden');
        return;
      }
      emptyState.classList.add('hidden');

      let html = '';

      visibleDays.forEach(day => {
        if (day.is_rest_day) {
          html += `
            <div id="cal-day-section-${day.calendar_day}" class="rounded-3xl bg-gradient-to-r from-amber-950/40 via-slate-900/90 to-purple-950/40 border border-amber-600/30 p-5 sm:p-6 shadow-xl flex flex-col sm:flex-row items-center justify-between gap-4">
              <div class="flex items-center gap-4 text-center sm:text-right">
                <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-2xl shrink-0">
                  <i class="fa-solid fa-mug-hot"></i>
                </div>
                <div>
                  <div class="flex items-center gap-2">
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 font-num">${day.day_label}</span>
                    <span class="text-xs text-slate-400 font-num">${day.date}</span>
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-purple-500/20 text-purple-300">يوم راحة أسبوعي</span>
                  </div>
                  <h3 class="text-base sm:text-lg font-bold text-white mt-1">${day.title}</h3>
                  <p class="text-xs text-slate-400 mt-0.5">خصص هذا اليوم للراحة التامة من الدروس الجديدة، أو مراجعة سريعة للملاحظات التي دونتها وتثبيت المفاهيم.</p>
                </div>
              </div>
              <div class="px-4 py-2 rounded-xl bg-slate-800/80 border border-slate-700 text-xs font-semibold text-amber-300 shrink-0">
                <span>استعد بقوة للأسبوع القادم 🚀</span>
              </div>
            </div>
          `;
          return;
        }

        // Study Day Card
        const dayVideos = day.videos;
        const matchingVideos = dayVideos.filter(v => {
          const isDone = completedSet.has(v.id);
          if (currentFilter === 'pending' && isDone) return false;
          if (currentFilter === 'completed' && !isDone) return false;
          if (searchQuery) {
            const matchTitle = v.title.toLowerCase().includes(searchQuery);
            const matchDay = day.day_label.toLowerCase().includes(searchQuery);
            const matchSec = day.section_name.toLowerCase().includes(searchQuery);
            if (!matchTitle && !matchDay && !matchSec) return false;
          }
          return true;
        });

        const dayDoneCount = dayVideos.filter(v => completedSet.has(v.id)).length;
        const dayTotalCount = dayVideos.length;
        const dayPct = Math.round((dayDoneCount / dayTotalCount) * 100);
        const isDayAllDone = dayDoneCount === dayTotalCount && dayTotalCount > 0;
        const isCollapsed = collapsedDays.has(day.calendar_day) && !searchQuery;
        const dayTotalMins = dayVideos.reduce((acc, curr) => acc + curr.durationMins, 0);

        html += `
          <div id="cal-day-section-${day.calendar_day}" class="rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl overflow-hidden transition">
            
            <div onclick="toggleDayAccordion(${day.calendar_day})" class="p-4 sm:p-5 flex flex-col md:flex-row md:items-center justify-between gap-3 cursor-pointer hover:bg-slate-800/40 select-none border-b border-slate-800/60">
              
              <div class="flex items-center gap-3">
                <button class="w-8 h-8 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 flex items-center justify-center transition">
                  <i class="fa-solid fa-chevron-${isCollapsed ? 'down' : 'up'} text-xs"></i>
                </button>
                <div>
                  <div class="flex flex-wrap items-center gap-2">
                    <h3 class="text-lg sm:text-xl font-black text-white font-num">${day.day_label}</h3>
                    <span class="text-xs text-slate-400 font-num bg-slate-800 px-2.5 py-0.5 rounded-full border border-slate-700/60">${day.date}</span>
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30 font-num">القسم ${day.section_code}</span>
                    <span class="text-xs text-slate-400 font-num">(${day.sec_day_index}/${day.sec_total_days})</span>
                    ${isDayAllDone ? '<span class="px-2 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">مكتمل بالكامل 🎉</span>' : ''}
                  </div>
                  <div class="text-xs text-slate-400 mt-1 flex items-center gap-2">
                    <span class="font-semibold text-slate-300">${day.section_name}</span>
                    <span>•</span>
                    <span class="font-num">${dayTotalCount} مقاطع</span>
                    <span>•</span>
                    <span class="font-num">⏱️ ${dayTotalMins} دقيقة</span>
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-4 self-stretch md:self-auto justify-between md:justify-end" onclick="event.stopPropagation()">
                <div class="flex items-center gap-2">
                  <div class="w-24 sm:w-32 h-2.5 bg-slate-800 rounded-full overflow-hidden border border-slate-700/50">
                    <div class="h-full bg-gradient-to-r from-cisco-500 to-emerald-400 transition-all duration-300" style="width: ${dayPct}%"></div>
                  </div>
                  <span class="text-xs font-semibold text-slate-300 font-num min-w-[50px]">${dayDoneCount}/${dayTotalCount} (${dayPct}%)</span>
                </div>

                <button 
                  onclick="toggleDayAll(${day.calendar_day}, event)" 
                  class="px-3.5 py-2 rounded-xl text-xs font-bold transition flex items-center gap-1.5 ${isDayAllDone ? 'bg-emerald-600 text-white hover:bg-emerald-500' : 'bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700'}"
                >
                  <i class="fa-solid fa-${isDayAllDone ? 'check-double' : 'check'}"></i>
                  <span>${isDayAllDone ? 'إلغاء تحديد اليوم' : 'تحديد اليوم كاملاً'}</span>
                </button>
              </div>

            </div>

            <div class="${isCollapsed ? 'hidden' : 'block'} divide-y divide-slate-800/50">
        `;

        matchingVideos.forEach(video => {
          const isDone = completedSet.has(video.id);
          const hasNote = notesMap[video.id] && notesMap[video.id].trim().length > 0;

          html += `
            <div 
              id="video-row-${video.id}" 
              class="p-4 sm:px-5 sm:py-3.5 flex flex-col sm:flex-row sm:items-center justify-between gap-3 video-card-transition ${isDone ? 'bg-slate-950/40 text-slate-400' : 'hover:bg-slate-800/30'}"
            >
              
              <div class="flex items-start sm:items-center gap-3.5 flex-1 min-w-0">
                <button 
                  type="button"
                  onclick="toggleVideo(${video.id}, event)"
                  title="${isDone ? 'اضغط لتغيير الحالة إلى قيد الانتظار' : 'اضغط لتحديد الدرس كمكتمل'}"
                  class="w-7 h-7 mt-0.5 sm:mt-0 rounded-lg flex items-center justify-center shrink-0 border-2 transition active:scale-90 ${isDone ? 'bg-emerald-500 border-emerald-500 text-white shadow-lg shadow-emerald-500/20' : 'bg-slate-950 border-slate-700 hover:border-cisco-400 text-transparent'}"
                >
                  <i class="fa-solid fa-check text-xs font-black"></i>
                </button>

                <span class="text-xs font-mono px-2 py-0.5 rounded bg-slate-800/80 text-slate-400 font-num shrink-0">#${video.id}</span>

                <div class="min-w-0 flex-1">
                  <div class="text-sm font-semibold text-slate-100 flex items-center flex-wrap gap-1.5 ${isDone ? 'line-through text-slate-500' : ''}">
                    <span>${escapeHtml(video.title)}</span>
                  </div>
                  
                  <div class="flex items-center gap-3 text-xs text-slate-400 mt-1">
                    <span class="flex items-center gap-1 font-num text-slate-400">
                      <i class="fa-regular fa-clock text-[11px] text-cisco-400"></i>
                      <span>${video.duration}</span>
                    </span>
                    
                    ${isDone ? `
                      <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/15 text-emerald-400 border border-emerald-500/20 font-num">
                        [✓] Completed • مكتمل
                      </span>
                    ` : `
                      <span class="px-2 py-0.5 rounded text-[10px] font-medium bg-amber-500/10 text-amber-400/90 border border-amber-500/20 font-num">
                        [ ] Pending • قيد الانتظار
                      </span>
                    `}

                    ${hasNote ? `
                      <span class="text-xs text-cisco-400 flex items-center gap-1" title="يوجد ملاحظة مسجلة">
                        <i class="fa-solid fa-note-sticky text-yellow-400"></i>
                        <span>ملاحظة</span>
                      </span>
                    ` : ''}
                  </div>
                </div>

              </div>

              <div class="flex items-center gap-2 shrink-0 self-end sm:self-center">
                <button 
                  onclick="openVideoModal(${video.id})"
                  title="مشاهدة الفيديو داخل الصفحة"
                  class="px-3.5 py-1.5 rounded-xl bg-cisco-600/20 hover:bg-cisco-600 text-cisco-300 hover:text-white border border-cisco-500/30 text-xs font-bold flex items-center gap-1.5 transition active:scale-95"
                >
                  <i class="fa-solid fa-play text-[11px]"></i>
                  <span>مشاهدة</span>
                </button>

                <a 
                  href="${video.url}" 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  title="فتح في يوتيوب"
                  class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-red-400 text-xs transition active:scale-95"
                >
                  <i class="fa-brands fa-youtube text-sm"></i>
                </a>

                <button 
                  onclick="openNotesModal(${video.id})"
                  title="ملاحظات الدرس"
                  class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-yellow-400 text-xs transition active:scale-95"
                >
                  <i class="fa-solid fa-pen-to-square"></i>
                </button>
              </div>

            </div>
          `;
        });

        html += `
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function openVideoModal(id) {
      activeModalVideoId = id;
      const video = ALL_VIDEOS.find(v => v.id === id);
      if (!video) return;

      document.getElementById('modalVideoTitle').textContent = video.title;
      document.getElementById('modalVideoMeta').textContent = `${video.day_label} (${video.section_name}) • ${video.date} • المدة: ${video.duration}`;
      document.getElementById('modalExternalLink').href = video.url;

      updateModalToggleBtn();

      const iframe = document.getElementById('videoIframe');
      iframe.src = `https://www.youtube-nocookie.com/embed/${video.ytId}?autoplay=1&rel=0`;

      document.getElementById('videoModal').classList.remove('hidden');
    }

    function closeVideoModal() {
      const iframe = document.getElementById('videoIframe');
      iframe.src = '';
      document.getElementById('videoModal').classList.add('hidden');
      activeModalVideoId = null;
    }

    function updateModalToggleBtn() {
      const btn = document.getElementById('modalToggleCompleteBtn');
      if (!activeModalVideoId) return;
      const isDone = completedSet.has(activeModalVideoId);

      if (isDone) {
        btn.className = 'px-4 py-2 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition bg-emerald-600 text-white hover:bg-emerald-500';
        btn.innerHTML = '<i class="fa-solid fa-check-double"></i><span>مكتمل ✓ (اضغط للإلغاء)</span>';
      } else {
        btn.className = 'px-4 py-2 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition bg-slate-800 text-slate-200 hover:bg-emerald-600 hover:text-white border border-slate-700';
        btn.innerHTML = '<i class="fa-solid fa-check"></i><span>تحديد كمكتمل الآن</span>';
      }
    }

    function toggleCurrentModalVideo() {
      if (!activeModalVideoId) return;
      toggleVideo(activeModalVideoId);
      updateModalToggleBtn();
    }

    function navigateModalVideo(direction) {
      if (!activeModalVideoId) return;
      const nextId = activeModalVideoId + direction;
      if (nextId >= 1 && nextId <= ALL_VIDEOS.length) {
        openVideoModal(nextId);
      }
    }

    let activeNotesVideoId = null;
    function openNotesModal(id) {
      activeNotesVideoId = id;
      const video = ALL_VIDEOS.find(v => v.id === id);
      document.getElementById('notesVideoTitle').textContent = `#${video.id} - ${video.title}`;
      document.getElementById('noteTextArea').value = notesMap[id] || '';
      document.getElementById('notesModal').classList.remove('hidden');
    }

    function closeNotesModal() {
      document.getElementById('notesModal').classList.add('hidden');
      activeNotesVideoId = null;
    }

    function saveNote() {
      if (!activeNotesVideoId) return;
      const text = document.getElementById('noteTextArea').value.trim();
      if (text) {
        notesMap[activeNotesVideoId] = text;
      } else {
        delete notesMap[activeNotesVideoId];
      }
      saveState();
      closeNotesModal();
      render();
    }

    function exportUpdatedCSV() {
      let csvContent = '"Calendar Day","Date","Section","Video Title","Video URL","Duration","Status"\\n';
      
      CALENDAR_DATA.forEach(d => {
        if (d.is_rest_day) {
          csvContent += `"${d.day_label}","${d.date}","يوم راحة أسبوعي","${d.title}","-","-","[✓] Rest Day"\\n`;
        } else {
          d.videos.forEach(v => {
            const isDone = completedSet.has(v.id);
            const statusStr = isDone ? '[x] Completed' : '[ ] Pending';
            const escapedTitle = v.title.replace(/"/g, '""');
            csvContent += `"${d.day_label}","${d.date}","${d.section_name}","${escapedTitle}","${v.url}","${v.duration}","${statusStr}"\\n`;
          });
        }
      });

      const blob = new Blob(["\\ufeff" + csvContent], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', 'Plan_2026_Cisco_CCNA_30Days_6Sections_Updated.csv');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function openBackupModal() {
      document.getElementById('backupModal').classList.remove('hidden');
    }

    function closeBackupModal() {
      document.getElementById('backupModal').classList.add('hidden');
    }

    function downloadBackupJSON() {
      const backupData = {
        timestamp: new Date().toISOString(),
        plan: "30_days_6_sections",
        completedIds: Array.from(completedSet),
        notes: notesMap
      };

      const blob = new Blob([JSON.stringify(backupData, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', `CCNA_30Days_Progress_Backup_${new Date().toISOString().slice(0, 10)}.json`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function handleRestoreFile(event) {
      const file = event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const data = JSON.parse(e.target.result);
          if (data && Array.isArray(data.completedIds)) {
            completedSet = new Set(data.completedIds);
            if (data.notes) notesMap = data.notes;
            saveState();
            updateStats();
            render();
            closeBackupModal();
            alert('تم استعادة التقدم بنجاح!');
          } else {
            alert('صيغة الملف غير صالحة.');
          }
        } catch (err) {
          alert('حدث خطأ أثناء قراءة ملف النسخة الاحتياطية.');
        }
      };
      reader.readAsText(file);
    }

    function confirmReset() {
      if (confirm('هل أنت متأكد من رغبتك في تصفير كافة مقاطع الخطة وإعادتها إلى قيد الانتظار؟')) {
        completedSet.clear();
        saveState();
        updateStats();
        render();
      }
    }

    function toggleTheme() {
      const html = document.documentElement;
      if (html.classList.contains('dark')) {
        html.classList.remove('dark');
        localStorage.setItem(STORAGE_KEY_THEME, 'light');
        document.getElementById('themeIcon').className = 'fa-solid fa-moon';
      } else {
        html.classList.add('dark');
        localStorage.setItem(STORAGE_KEY_THEME, 'dark');
        document.getElementById('themeIcon').className = 'fa-solid fa-sun';
      }
    }

    function applyTheme() {
      const savedTheme = localStorage.getItem(STORAGE_KEY_THEME) || 'dark';
      if (savedTheme === 'light') {
        document.documentElement.classList.remove('dark');
        document.getElementById('themeIcon').className = 'fa-solid fa-moon';
      } else {
        document.documentElement.classList.add('dark');
        document.getElementById('themeIcon').className = 'fa-solid fa-sun';
      }
    }

    function escapeHtml(str) {
      return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeVideoModal();
        closeNotesModal();
        closeBackupModal();
      }
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'f') {
        document.getElementById('searchInput').focus();
      }
    });

    window.addEventListener('DOMContentLoaded', initApp);
  </script>
</body>
</html>
"""

target_path_1 = os.path.join(r'D:\CCNA III-PLAN', 'CCNA_2026_30Days_Plan.html')
target_path_2 = os.path.join(r'D:\CCNA III-PLAN', 'index_30days.html')

with open(target_path_1, 'w', encoding='utf-8') as f:
    f.write(html_template)

with open(target_path_2, 'w', encoding='utf-8') as f:
    f.write(html_template)

print('Success! Generated CCNA_2026_30Days_Plan.html and index_30days.html')
