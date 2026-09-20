# -*- coding: utf-8 -*-
"""
Script nâng cấp Bảng Vàng (bang-vang.html):
1. Lịch 35 tuần năm học 2026 - 2027 (14:00 Thứ Sáu, nghỉ Tết 2 tuần).
2. Chế độ lọc Đua Top Tuần: 14:00 Thứ Sáu tuần này -> 13:59:59 Thứ Sáu tuần sau.
3. Chế độ xem: 🏆 Đua Top Tuần (Chính thức) vs 🌟 Tất cả lượt thi (Luyện tập).
4. Đồng bộ 5 thư mục.
"""
import os
import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = os.path.dirname(os.path.abspath(__file__))
from schedule_data import SCHEDULE_CONFIG

with open(os.path.join(ROOT, "bang-vang.html"), "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update filter bar HTML
old_filter_bar = '''    <!-- BỘ LỌC HỌC KỲ -->
    <div class="filter-bar">
        <button class="btn-filter-bv active" id="btn-bv-all" onclick="filterBv('all')">🌟 TOÀN BỘ (35 TUẦN)</button>
        <button class="btn-filter-bv" id="btn-bv-hk1" onclick="filterBv('hk1')">📘 HỌC KỲ 1 (TUẦN 1 - 18)</button>
        <button class="btn-filter-bv" id="btn-bv-hk2" onclick="filterBv('hk2')">📙 HỌC KỲ 2 (TUẦN 19 - 35)</button>
    </div>'''

new_filter_bar = '''    <!-- BỘ LỌC CHẾ ĐỘ & HỌC KỲ -->
    <div class="filter-bar" style="flex-direction:column; gap:8px;">
        <div style="display:flex; gap:8px; justify-content:center; flex-wrap:wrap; width:100%;">
            <button class="btn-filter-bv active" id="btn-mode-official" onclick="setModeFilter('official')" style="background:#4CAF50; color:#fff; border-color:#4CAF50;">🏆 ĐUA TOP TUẦN (14H T6 - 13H59 T6 SAU)</button>
            <button class="btn-filter-bv" id="btn-mode-all" onclick="setModeFilter('all')" style="background:#fff; color:#333; border-color:#ccc;">🌟 TẤT CẢ LƯỢT THI (TỰ LUYỆN)</button>
        </div>
        <div style="display:flex; gap:8px; justify-content:center; flex-wrap:wrap; width:100%;">
            <button class="btn-filter-bv active" id="btn-bv-all" onclick="filterBv('all')">🌟 TOÀN BỘ (35 TUẦN)</button>
            <button class="btn-filter-bv" id="btn-bv-hk1" onclick="filterBv('hk1')">📘 HỌC KỲ 1 (TUẦN 1 - 18)</button>
            <button class="btn-filter-bv" id="btn-bv-hk2" onclick="filterBv('hk2')">📙 HỌC KỲ 2 (TUẦN 19 - 35)</button>
        </div>
    </div>'''

if old_filter_bar in html:
    html = html.replace(old_filter_bar, new_filter_bar, 1)

# 2. Inject SCHEDULE & Window Time in script
sched_str = json.dumps(SCHEDULE_CONFIG, ensure_ascii=False, indent=12)

old_script_start = '''    <script>
        const firebaseConfig = {
            databaseURL: "https://gamhoctap-default-rtdb.asia-southeast1.firebasedatabase.app"
        };
        firebase.initializeApp(firebaseConfig);
        const db = firebase.database();

        const charts = {};'''

new_script_start = f'''    <script>
        const firebaseConfig = {{
            databaseURL: "https://gamhoctap-default-rtdb.asia-southeast1.firebasedatabase.app"
        }};
        firebase.initializeApp(firebaseConfig);
        const db = firebase.database();

        const SCHEDULE = {sched_str};
        let currentModeFilter = 'official'; // 'official' (14h T6 -> 13h59 T6 sau) | 'all'
        let currentSemesterFilter = 'all'; // 'all' | 'hk1' | 'hk2'
        let cachedAllScores = {{}};
        const charts = {{}};'''

if old_script_start in html:
    html = html.replace(old_script_start, new_script_start, 1)

# 3. Update initAccordion to show weekly window & time info
old_init = '''                html += `
                <div class="week-accordion" id="accordion-week-${i}">
                    <div class="week-header" onclick="toggleWeek(${i})">
                        <div class="week-title"><span>📂 Tuần ${i}: ${landmark}</span> <span class="week-badge" id="count-${i}">0 bạn</span></div>
                        <span id="icon-${i}">▼</span>
                    </div>'''

new_init = '''                const sched = SCHEDULE[i];
                const timeInfo = sched ? `<span style="font-size:0.75rem; color:#e0f2fe; font-weight:normal; margin-left:8px; display:inline-block;">(⏱ Mở: ${sched.open_str} -> Chốt: ${sched.close_str})</span>` : '';
                html += `
                <div class="week-accordion" id="accordion-week-${i}">
                    <div class="week-header" onclick="toggleWeek(${i})">
                        <div class="week-title">
                            <div>
                                <span>📂 Tuần ${i}: ${landmark}</span>
                                ${timeInfo}
                            </div>
                            <span class="week-badge" id="count-${i}">0 bạn</span>
                        </div>
                        <span id="icon-${i}">▼</span>
                    </div>'''

if old_init in html:
    html = html.replace(old_init, new_init, 1)

# 4. Update data processing to support time window filtering
old_listener_start = '''        db.ref('scores').on('value', (snap) => {
            const allData = snap.val() || {};'''

new_listener_start = '''        function setModeFilter(mode) {
            currentModeFilter = mode;
            document.getElementById('btn-mode-official').classList.toggle('active', mode === 'official');
            document.getElementById('btn-mode-all').classList.toggle('active', mode === 'all');
            if (mode === 'official') {
                document.getElementById('btn-mode-official').style.background = '#4CAF50';
                document.getElementById('btn-mode-official').style.color = '#fff';
                document.getElementById('btn-mode-all').style.background = '#fff';
                document.getElementById('btn-mode-all').style.color = '#333';
            } else {
                document.getElementById('btn-mode-all').style.background = '#4CAF50';
                document.getElementById('btn-mode-all').style.color = '#fff';
                document.getElementById('btn-mode-official').style.background = '#fff';
                document.getElementById('btn-mode-official').style.color = '#333';
            }
            renderAllWeeks();
        }

        function parseDateToMs(str) {
            if (!str) return 0;
            try {
                const parts = str.split(' ');
                const timeParts = parts[0].split(':');
                const dateParts = parts[1].split('/');
                const d = new Date(dateParts[2], dateParts[1] - 1, dateParts[0], timeParts[0], timeParts[1], timeParts[2] || 0);
                return d.getTime();
            } catch(e) {
                return 0;
            }
        }

        db.ref('scores').on('value', (snap) => {
            cachedAllScores = snap.val() || {};
            renderAllWeeks();
        });

        function renderAllWeeks() {
            const allData = cachedAllScores;'''

if old_listener_start in html:
    html = html.replace(old_listener_start, new_listener_start, 1)

# 5. Inside week loop: filter by schedule window if currentModeFilter === 'official'
old_sort_logic = '''                let sorted = Array.from(filteredMap.values())
                    .filter(s => {
                        let nameValue = (s.fullName || s.name || "").trim();
                        let nameLower = nameValue.toLowerCase();

                        const draftKeywords = ['test', 'abc', 'nhap', 'nháp', '123', 'demo', 'đemo', 'xxx', '...', '---', 'utc', 'bts', 'admin'];
                        if (draftKeywords.some(k => nameLower.includes(k))) return false;
                        if (/^\\d+$/.test(nameLower)) return false;

                        const words = nameValue.split(/\\s+/).filter(w => w.length > 0);
                        if (words.length < 2) return false;
                        if (words.some(w => w.length > 15)) return false;

                        return (s.score || 0) >= 50;
                    })'''

new_sort_logic = '''                const sched = SCHEDULE[i];
                let sorted = Array.from(filteredMap.values())
                    .filter(s => {
                        let nameValue = (s.fullName || s.name || "").trim();
                        let nameLower = nameValue.toLowerCase();

                        const draftKeywords = ['test', 'abc', 'nhap', 'nháp', '123', 'demo', 'đemo', 'xxx', '...', '---', 'utc', 'bts', 'admin'];
                        if (draftKeywords.some(k => nameLower.includes(k))) return false;
                        if (/^\\d+$/.test(nameLower)) return false;

                        const words = nameValue.split(/\\s+/).filter(w => w.length > 0);
                        if (words.length < 2) return false;
                        if (words.some(w => w.length > 15)) return false;

                        // Lọc theo khung giờ đua Top tuần chính thức
                        if (currentModeFilter === 'official' && sched) {
                            const openMs = new Date(sched.open).getTime();
                            const closeMs = new Date(sched.close).getTime();
                            const submitTime = s.timestamp || parseDateToMs(s.date);
                            if (submitTime > 0) {
                                if (submitTime < openMs || submitTime > closeMs) return false;
                            }
                        }

                        return (s.score || 0) >= 50;
                    })'''

if old_sort_logic in html:
    html = html.replace(old_sort_logic, new_sort_logic, 1)

# Write to all 5 locations
targets = [
    os.path.join(ROOT, "bang-vang.html"),
    os.path.join(ROOT, "edubot-zmp", "src", "bang-vang.html"),
    os.path.join(ROOT, "edubot-zmp", "src", "public", "bang-vang.html"),
    os.path.join(ROOT, "edubot-zmp", "src", "www", "bang-vang.html"),
    os.path.join(ROOT, "edubot-zmp", "www", "bang-vang.html"),
]

for p in targets:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ Đã cập nhật bang-vang.html tại {os.path.relpath(p, ROOT)}")

print("HOÀN TẤT NÂNG CẤP BẢNG VÀNG CHÍNH THỨC!")
