r"""
Script nâng cấp Bảng Vàng (bang-vang.html) hỗ trợ trọn bộ 35 Tuần với bộ lọc học kỳ và tên danh thắng
Đồng bộ sang:
1. c:/Users/Admin/Desktop/EduBot-BTCT5/bang-vang.html
2. edubot-zmp/src/bang-vang.html
3. edubot-zmp/src/www/bang-vang.html
"""

import os
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

html_content = '''<!DOCTYPE html>
<html lang="vi">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Bảng Vàng Thành Tích (Trọn Bộ 35 Tuần) - EduRobot.id.vn</title>
    <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;600;700&family=Bungee&display=swap" rel="stylesheet">
    <script src="https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/8.10.1/firebase-database.js"></script>
    <script src="https://cdn.sheetjs.com/xlsx-0.19.2/package/dist/xlsx.full.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        :root {
            --primary: #4CAF50;
            --secondary: #2196F3;
            --bg: #f4f7f6;
            --dark: #2c3e50;
            --gold: #FFD700;
        }

        body {
            font-family: 'Lexend', sans-serif;
            background: var(--bg);
            margin: 0;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }

        header {
            background: white;
            padding: 0.8rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .logo {
            font-size: 1.2rem;
            font-weight: bold;
            color: var(--primary);
            text-decoration: none;
            white-space: nowrap;
        }

        .hero {
            text-align: center;
            padding: 18px 10px;
            background: linear-gradient(135deg, #1e3a8a, #0284c7);
            color: white;
        }

        .hero h1 {
            font-size: 1.5rem;
            margin: 0 0 4px;
            font-family: 'Bungee', cursive;
            color: var(--gold);
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.4);
        }

        .hero p {
            font-size: 0.85rem;
            margin: 0;
            opacity: 0.9;
        }

        /* FILTER BAR */
        .filter-bar {
            display: flex;
            justify-content: center;
            gap: 8px;
            margin: 15px auto;
            max-width: 900px;
            padding: 0 10px;
            flex-wrap: wrap;
        }

        .btn-filter-bv {
            background: white;
            border: 1.5px solid #cbd5e1;
            color: #475569;
            padding: 7px 15px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: 0.2s;
        }

        .btn-filter-bv:hover, .btn-filter-bv.active {
            background: #2563eb;
            color: white;
            border-color: #2563eb;
            box-shadow: 0 2px 8px rgba(37, 99, 235, 0.35);
        }

        .admin-container {
            max-width: 1100px;
            margin: 5px auto 50px;
            padding: 0 10px;
            width: 100%;
            box-sizing: border-box;
        }

        .week-accordion {
            background: white;
            border-radius: 12px;
            margin-bottom: 12px;
            overflow: hidden;
            border: 1px solid #ddd;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
            transition: 0.2s;
        }

        .week-header {
            padding: 12px 15px;
            background: #fff;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            transition: 0.3s;
            user-select: none;
        }

        .week-header.active {
            background: #e0f2fe;
            border-bottom: 2px solid #0284c7;
        }

        .week-title {
            font-weight: bold;
            font-size: 0.92rem;
            color: var(--dark);
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }

        .week-badge {
            background: #0284c7;
            color: white;
            padding: 2px 8px;
            border-radius: 20px;
            font-size: 0.72rem;
            white-space: nowrap;
        }

        .week-content {
            display: none;
            padding: 0;
            background: white;
        }

        .week-content.show {
            display: block;
        }

        .chart-section {
            padding: 15px;
            background: #fff;
            border-bottom: 1px solid #eee;
        }

        .chart-container {
            position: relative;
            height: 250px;
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
        }

        .chart-title {
            text-align: center;
            font-size: 0.85rem;
            font-weight: bold;
            color: #555;
            margin-bottom: 10px;
        }

        .action-bar {
            padding: 8px 15px;
            background: #fafafa;
            border-bottom: 1px solid #eee;
            display: flex;
            justify-content: flex-end;
        }

        .btn-excel {
            background: #27ae60;
            color: white;
            border: none;
            padding: 5px 12px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.75rem;
            font-weight: 600;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.82rem;
        }

        th {
            background: #f1f2f6;
            color: #555;
            text-align: left;
            padding: 8px 10px;
            font-size: 0.75rem;
            white-space: nowrap;
        }

        td {
            padding: 8px 10px;
            border-bottom: 1px solid #eee;
            color: #333;
            white-space: nowrap;
        }

        .rank {
            font-weight: bold;
            width: 20px;
            height: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            background: #eee;
            font-size: 0.75rem;
        }

        tr:nth-child(1) .rank { background: #ffd700; color: #000; }
        tr:nth-child(2) .rank { background: #cbd5e1; color: #000; }
        tr:nth-child(3) .rank { background: #cd7f32; color: #fff; }

        .score-badge {
            color: #d35400;
            font-weight: bold;
            font-size: 0.85rem;
        }

        .time-badge {
            color: #27ae60;
            font-family: monospace;
            font-size: 0.8rem;
        }

        .class-badge {
            background: #eef2f7;
            color: #333;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.75rem;
            border: 1px solid #ddd;
            white-space: nowrap;
        }

        .attempt-badge {
            background: #fff3e0;
            color: #ef6c00;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.72rem;
            font-weight: 600;
            border: 1px solid #ffe0b2;
            white-space: nowrap;
        }

        footer {
            background: var(--dark);
            color: white;
            text-align: center;
            padding: 15px;
            font-size: 0.75rem;
            margin-top: auto;
        }

        .table-responsive {
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }
    </style>
</head>

<body>
    <header>
        <a href="index.html" class="logo">EduRobot.id.vn 🤖</a>
        <nav><a href="index.html" style="text-decoration:none; color:#333; font-size: 0.85rem; font-weight: 600;">Trang chủ</a></nav>
    </header>

    <section class="hero">
        <h1>🏆 BẢNG VÀNG VINH DANH</h1>
        <p>Thành tích xuất sắc nhất của các nhà thám hiểm (Trọn bộ 35 Trạm)</p>
    </section>

    <!-- BỘ LỌC HỌC KỲ -->
    <div class="filter-bar">
        <button class="btn-filter-bv active" id="btn-bv-all" onclick="filterBv('all')">🌟 TOÀN BỘ (35 TUẦN)</button>
        <button class="btn-filter-bv" id="btn-bv-hk1" onclick="filterBv('hk1')">📘 HỌC KỲ 1 (TUẦN 1 - 18)</button>
        <button class="btn-filter-bv" id="btn-bv-hk2" onclick="filterBv('hk2')">📙 HỌC KỲ 2 (TUẦN 19 - 35)</button>
    </div>

    <main class="admin-container" id="accordion-container"></main>

    <footer>&copy; 2026 EduRobot.id.vn - Lê Thành Long</footer>

    <script>
        const firebaseConfig = {
            databaseURL: "https://gamhoctap-default-rtdb.asia-southeast1.firebasedatabase.app"
        };
        firebase.initializeApp(firebaseConfig);
        const db = firebase.database();

        const charts = {};

        const WEEK_LANDMARKS = {
            1: "Cột cờ Lũng Cú (Hà Giang)",
            2: "Hẻm Tu Sản & Sông Nho Quế",
            3: "Thác Bản Giốc (Cao Bằng)",
            4: "Hồ Ba Bể (Bắc Kạn)",
            5: "Ruộng bậc thang Mù Cang Chải",
            6: "Đỉnh Fansipan (Lào Cai)",
            7: "Thủ đô Hà Nội",
            8: "Vịnh Hạ Long & Yên Tử",
            9: "Tràng An & Cố đô Hoa Lư 🌟",
            10: "Thành Nhà Hồ (Thanh Hóa)",
            11: "Làng Sen Quê Bác (Nghệ An)",
            12: "Ngã ba Đồng Lộc (Hà Tĩnh)",
            13: "VQG Phong Nha - Kẻ Bàng",
            14: "Thành cổ Quảng Trị & Hiền Lương",
            15: "Quần thể Cố đô Huế",
            16: "Cầu Rồng & Ngũ Hành Sơn",
            17: "Phố cổ Hội An (Quảng Nam)",
            18: "Đảo Lý Sơn (Quảng Ngãi) 🏆",
            19: "Kon Tum (Bờ Y - Ngã ba Đông Dương)",
            20: "Gia Lai (Biển Hồ Tơ Nưng)",
            21: "Đắk Lắk (Buôn Đôn, Dray Nur)",
            22: "Đắk Nông (Hồ Tà Đùng)",
            23: "Phú Yên (Gành Đá Đĩa & Mũi Điện)",
            24: "Khánh Hòa (Vịnh Nha Trang, Trầm Hương)",
            25: "Ninh Thuận (Tháp Po Klong Garai)",
            26: "Bình Thuận (Đồi cát Mũi Né, Bàu Trắng)",
            27: "Lâm Đồng (Đỉnh Lang Biang, Đà Lạt) 🌟",
            28: "TP.HCM (Địa đạo Củ Chi, Rừng Sác)",
            29: "Tây Ninh (Núi Bà Đen)",
            30: "TP.HCM (Bến Nhà Rồng, Landmark 81)",
            31: "Đồng Tháp (Sa Đéc, Sen Tháp Mười)",
            32: "Cà Mau (Đất Mũi Cà Mau)",
            33: "Kiên Giang (Đảo Ngọc Phú Quốc)",
            34: "Khánh Hòa (Quần đảo Trường Sa)",
            35: "Đà Nẵng (Quần đảo Hoàng Sa) 🏆"
        };

        function formatTime(s) {
            if (!s || s === 9999) return "---";
            const m = Math.floor(s / 60);
            const rs = s % 60;
            return m > 0 ? `${m}m ${rs}s` : `${rs}s`;
        }

        function filterBv(mode) {
            document.querySelectorAll('.btn-filter-bv').forEach(b => b.classList.remove('active'));
            document.getElementById('btn-bv-' + mode).classList.add('active');
            for (let i = 1; i <= 35; i++) {
                const el = document.getElementById(`accordion-week-${i}`);
                if (!el) continue;
                if (mode === 'hk1') {
                    el.style.display = (i <= 18) ? 'block' : 'none';
                } else if (mode === 'hk2') {
                    el.style.display = (i >= 19) ? 'block' : 'none';
                } else {
                    el.style.display = 'block';
                }
            }
        }

        function initAccordion() {
            const container = document.getElementById('accordion-container');
            let html = '';
            for (let i = 1; i <= 35; i++) {
                const landmark = WEEK_LANDMARKS[i] || "";
                html += `
                <div class="week-accordion" id="accordion-week-${i}">
                    <div class="week-header" onclick="toggleWeek(${i})">
                        <div class="week-title"><span>📂 Tuần ${i}: ${landmark}</span> <span class="week-badge" id="count-${i}">0 bạn</span></div>
                        <span id="icon-${i}">▼</span>
                    </div>
                    <div class="week-content" id="content-${i}">
                        <div class="chart-section" id="chart-section-${i}" style="display:none;">
                            <div class="chart-title">Phân bổ khoảng điểm (Tuần ${i}: ${landmark})</div>
                            <div class="chart-container"><canvas id="chart-canvas-${i}"></canvas></div>
                        </div>
                        <div class="action-bar"><button class="btn-excel" onclick="exportExcel(${i})">📄 Xuất Excel Tuần ${i}</button></div>
                        <div class="table-responsive">
                            <table>
                                <thead>
                                    <tr>
                                        <th>Hạng</th>
                                        <th>Học sinh</th>
                                        <th>Lớp</th>
                                        <th>Trường</th>
                                        <th>Điểm</th>
                                        <th>Thời gian</th>
                                        <th>Lần thi</th>
                                        <th>Ngày đạt</th>
                                    </tr>
                                </thead>
                                <tbody id="tbody-${i}"><tr><td colspan="8" style="text-align:center; padding:20px; color:#999;">Chưa có dữ liệu lượt thi nào.</td></tr></tbody>
                            </table>
                        </div>
                    </div>
                </div>
                `;
            }
            container.innerHTML = html;
        }

        function toggleWeek(i) {
            const content = document.getElementById(`content-${i}`);
            const header = content.previousElementSibling;
            const icon = document.getElementById(`icon-${i}`);
            content.classList.toggle('show');
            header.classList.toggle('active');
            icon.innerText = content.classList.contains('show') ? '▲' : '▼';
        }

        const topLabelsPlugin = {
            id: 'topLabels',
            afterDatasetsDraw(chart) {
                const { ctx } = chart;
                ctx.save();
                chart.data.datasets.forEach((dataset, i) => {
                    chart.getDatasetMeta(i).data.forEach((bar, index) => {
                        const value = dataset.data[index];
                        if (value > 0) {
                            ctx.fillStyle = '#444';
                            ctx.font = 'bold 10px Lexend';
                            ctx.textAlign = 'center';
                            ctx.textBaseline = 'bottom';
                            ctx.fillText(value, bar.x, bar.y - 5);
                        }
                    });
                });
                ctx.restore();
            }
        };

        function updateChart(week, distribution) {
            const ctx = document.getElementById(`chart-canvas-${week}`).getContext('2d');
            if (charts[week]) charts[week].destroy();
            charts[week] = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['50-59', '60-69', '70-79', '80-89', '90-100'],
                    datasets: [{
                        data: distribution,
                        backgroundColor: [
                            'rgba(231, 76, 60, 0.7)', 'rgba(230, 126, 34, 0.7)',
                            'rgba(241, 196, 15, 0.7)', 'rgba(52, 152, 219, 0.7)',
                            'rgba(46, 204, 113, 0.7)'
                        ],
                        borderWidth: 1,
                        borderRadius: 4
                    }]
                },
                plugins: [topLabelsPlugin],
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                        y: { beginAtZero: true, ticks: { stepSize: 1, font: { size: 9 } } },
                        x: { ticks: { font: { size: 9, weight: '600' } } }
                    }
                }
            });
        }

        function exportExcel(week) {
            const table = document.querySelector(`#tbody-${week}`).parentElement;
            const rows = table.querySelectorAll('tr');
            const data = [];

            rows.forEach((row, rowIndex) => {
                const cols = row.querySelectorAll('th, td');
                const rowData = [];
                cols.forEach((col, colIndex) => {
                    let value = col.innerText.replace('⏱ ', '').replace('/100', '');
                    if (colIndex === 2 && rowIndex > 0) {
                        rowData.push({ v: value, t: 's' });
                    } else {
                        rowData.push(value);
                    }
                });
                data.push(rowData);
            });

            const ws = XLSX.utils.aoa_to_sheet(data);
            const wb = XLSX.utils.book_new();
            XLSX.utils.book_append_sheet(wb, ws, "Tuần " + week);
            XLSX.writeFile(wb, `BangVang_Tuan_${week}.xlsx`);
        }

        db.ref('scores').on('value', (snap) => {
            const allData = snap.val() || {};
            for (let i = 1; i <= 35; i++) {
                const weekData = allData[`Tuan_${i}`] || allData[`tuan${i}`];
                const tbody = document.getElementById(`tbody-${i}`);
                const countBadge = document.getElementById(`count-${i}`);
                const chartSection = document.getElementById(`chart-section-${i}`);

                if (!tbody) continue;

                if (!weekData) {
                    tbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:15px; color:#999; font-size:0.8rem;">Chưa có dữ liệu lượt thi nào.</td></tr>`;
                    countBadge.innerText = `0 bạn`;
                    chartSection.style.display = 'none';
                    continue;
                }

                let filteredMap = new Map();
                Object.values(weekData).forEach(entry => {
                    let key = ((entry.fullName || entry.name || "") + "|" + (entry.className || entry.class || "")).toLowerCase().trim();
                    if (!filteredMap.has(key)) filteredMap.set(key, entry);
                    else {
                        let old = filteredMap.get(key);
                        if (entry.score > old.score || (entry.score === old.score && (entry.duration || 999) < (old.duration || 999))) filteredMap.set(key, entry);
                    }
                });

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

                        return (s.score || 0) >= 50;
                    })
                    .sort((a, b) => (b.score !== a.score) ? b.score - a.score : (a.duration || 999) - (b.duration || 999));

                let dist = [0, 0, 0, 0, 0];
                sorted.forEach(s => {
                    let sc = s.score || 0;
                    if (sc <= 59) dist[0]++;
                    else if (sc <= 69) dist[1]++;
                    else if (sc <= 79) dist[2]++;
                    else if (sc <= 89) dist[3]++;
                    else dist[4]++;
                });

                countBadge.innerText = `${sorted.length} bạn`;
                if (sorted.length === 0) {
                    tbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:15px; color:#999; font-size:0.8rem;">Chưa có bạn nào đạt từ 50 điểm trở lên.</td></tr>`;
                    chartSection.style.display = 'none';
                } else {
                    tbody.innerHTML = sorted.map((s, idx) => `
                        <tr>
                            <td><div class="rank">${idx + 1}</div></td>
                            <td><b>${s.fullName || s.name}</b></td>
                            <td><span class="class-badge">${s.className || s.class}</span></td>
                            <td><span style="font-size:0.8rem; color:#555;">${s.schoolName || '---'}</span></td>
                            <td><span class="score-badge">${s.score}/100</span></td>
                            <td><span class="time-badge">⏱ ${formatTime(s.duration)}</span></td>
                            <td><span class="attempt-badge">Lần ${s.attempt || 1}</span></td>
                            <td style="font-size:0.75rem; color:#888;">${s.date || ""}</td>
                        </tr>
                    `).join('');
                    chartSection.style.display = 'block';
                    updateChart(i, dist);
                }
            }
        });

        initAccordion();
    </script>
</body>

</html>
'''

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    p_root = os.path.join(root_dir, "bang-vang.html")
    p_zmp = os.path.join(root_dir, "edubot-zmp", "src", "bang-vang.html")
    p_zmp_www = os.path.join(root_dir, "edubot-zmp", "src", "www", "bang-vang.html")

    with open(p_root, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("  ✓ Đã cập nhật bang-vang.html tại thư mục gốc")

    with open(p_zmp, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("  ✓ Đã cập nhật bang-vang.html tại edubot-zmp/src")

    with open(p_zmp_www, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("  ✓ Đã cập nhật bang-vang.html tại edubot-zmp/src/www")

    print("\nHOÀN TẤT ĐỒNG BỘ BẢNG VÀNG 35 TUẦN CÙNG DANH THẮNG VÀ BỘ LỌC HỌC KỲ!")

if __name__ == "__main__":
    main()
