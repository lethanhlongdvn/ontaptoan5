# -*- coding: utf-8 -*-
"""
Script nâng cấp index.html:
1. Thêm Phân quyền: Học sinh (student), Giáo viên (teacher), Quản trị viên (admin).
2. Form Đăng ký: Có chọn vai trò, lưu status: 'pending'.
3. Quản lý trạng thái: Lưu userRole, userStatus, hiển thị huy hiệu và nút Quản trị.
4. Lịch mở 35 tuần chuẩn (14:00 Thứ Sáu, nghỉ Tết 2 tuần).
5. Phân quyền click trạm:
   - Khách / Chờ duyệt: tối đa đến vòng 8.
   - Giáo viên/Admin duyệt: mở toàn bộ 35 tuần ngay lập tức.
   - Học sinh duyệt: theo lịch mở tự động 14:00 Thứ Sáu.
6. Bảng vàng Top 10: Tích hợp bộ lọc khung giờ chính thức (14:00 T6 - 13:59:59 T6 sau).
"""
import os
import sys
import json
import re

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = os.path.dirname(os.path.abspath(__file__))

from schedule_data import SCHEDULE_CONFIG

with open(os.path.join(ROOT, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Registration Form HTML: Add Role selection & explanation notice
reg_target = '''            <!-- Hàng 1: Tên đăng nhập & Mật khẩu -->'''
reg_replacement = '''            <!-- Chọn Vai trò -->
            <div style="background:rgba(255,255,255,0.04); border:1px solid #334155; border-radius:8px; padding:7px 10px; margin-bottom:8px;">
                <label class="auth-label" style="margin:0 0 4px; font-size:0.75rem; color:var(--text-sec);">Chọn vai trò tham gia:</label>
                <div style="display:flex; gap:12px;">
                    <label style="font-size:0.8rem; color:var(--gold); display:flex; align-items:center; gap:5px; cursor:pointer; font-weight:600;">
                        <input type="radio" name="reg-role" value="student" checked onchange="handleRegRoleChange()"> ⭐ Em là Học sinh
                    </label>
                    <label style="font-size:0.8rem; color:var(--cyan); display:flex; align-items:center; gap:5px; cursor:pointer; font-weight:600;">
                        <input type="radio" name="reg-role" value="teacher" onchange="handleRegRoleChange()"> 🎓 Thầy/Cô là Giáo viên
                    </label>
                </div>
            </div>

            <!-- Ghi chú phê duyệt -->
            <div style="background:rgba(255,152,0,0.12); border:1px dashed var(--p); border-radius:6px; padding:6px 10px; font-size:0.72rem; color:#ffcc80; margin-bottom:8px; line-height:1.4;">
                ℹ️ <b>Lưu ý:</b> Tài khoản sau khi đăng ký sẽ ở trạng thái <b>Chờ duyệt</b>. Khách và tài khoản chờ duyệt được làm quen từ <b>Vòng 1 đến 8</b>. Sau khi Thầy Cô/Admin duyệt sẽ mở hết <b>35 vòng</b>.
            </div>

            <!-- Hàng 1: Tên đăng nhập & Mật khẩu -->'''

if reg_target in html and 'name="reg-role"' not in html:
    html = html.replace(reg_target, reg_replacement, 1)
    print("✓ Đã cập nhật Form Đăng ký (chọn vai trò Học sinh/Giáo viên)")

# 2. Add Modal Thông báo Chặn Vòng > 8 cho khách/chờ duyệt
notice_target = '''    <!-- ĐỒNG HỒ ĐẾM NGƯỢC CHẶNG CHƯA MỞ -->'''
notice_replacement = '''    <!-- CỬA SỔ THÔNG BÁO VÒNG DÀNH CHO TÀI KHOẢN DUYỆT -->
    <div id="locked-station-overlay" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(15,23,42,0.95); z-index:9999; justify-content:center; align-items:center; backdrop-filter:blur(8px); padding:20px;">
        <div class="notice-box" style="background:#1e293b; border:2px solid var(--p); border-radius:16px; padding:24px; max-width:420px; width:90%; text-align:center;">
            <span style="font-size:2.6rem; display:block; margin-bottom:8px;">🔒</span>
            <h2 id="locked-modal-title" style="font-family:'Bungee'; color:var(--gold); font-size:1.15rem; margin:0 0 10px;">YÊU CẦU PHÊ DUYỆT</h2>
            <div id="locked-modal-msg" style="font-size:0.85rem; color:#e2e8f0; line-height:1.5; margin-bottom:18px; text-align:left; background:#0f172a; padding:12px; border-radius:8px; border:1px solid #334155;"></div>
            <div style="display:flex; gap:8px; justify-content:center; flex-wrap:wrap;">
                <button class="btn-nav" id="locked-btn-auth" onclick="handleLockedModalAuth()" style="flex:1; background:var(--p); color:#000; font-weight:700; border:none; padding:10px 14px;">ĐĂNG NHẬP / ĐĂNG KÝ</button>
                <button class="btn-nav" onclick="closeLockedModal()" style="flex:1; border-color:#94a3b8; color:#fff; padding:10px 14px;">ĐÃ HIỂU</button>
            </div>
        </div>
    </div>

    <!-- ĐỒNG HỒ ĐẾM NGƯỢC CHẶNG CHƯA MỞ -->'''

if notice_target in html and 'id="locked-station-overlay"' not in html:
    html = html.replace(notice_target, notice_replacement, 1)
    print("✓ Đã thêm Modal thông báo kiểm soát vòng thi (> vòng 8)")

# 3. Add Leaderboard Tabs (Đua Top Tuần vs Toàn Bộ Lượt Thi) + Week Selector
lb_target = '''        <!-- BẢNG XẾP HẠNG TOP 10 -->
        <section class="leaderboard-sidebar">
            <h3 class="leaderboard-title" id="lb-title">🏆 TOP 10 CAO THỦ - TUẦN 1</h3>'''

lb_replacement = '''        <!-- BẢNG XẾP HẠNG TOP 10 -->
        <section class="leaderboard-sidebar">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:6px;">
                <h3 class="leaderboard-title" id="lb-title" style="margin:0; font-size:0.85rem;">🏆 TOP 10 CAO THỦ</h3>
                <select id="lb-week-select" onchange="loadLeaderboard(Number(this.value))" style="background:#0f172a; color:var(--gold); border:1px solid var(--p); border-radius:6px; padding:4px 8px; font-size:0.8rem; font-weight:bold; font-family:'Lexend';">
                    <!-- Options injected via JS -->
                </select>
            </div>
            <!-- Bộ lọc đua top tuần chính thức -->
            <div style="display:flex; gap:5px; margin-bottom:8px;">
                <button id="btn-lb-official" class="btn-filter-lb active" onclick="setLbFilterMode('official')" style="flex:1; padding:4px 6px; font-size:0.7rem; font-weight:700; border-radius:6px; border:1px solid var(--p); background:var(--p); color:#000; cursor:pointer;">🏆 Đua Top Tuần</button>
                <button id="btn-lb-all" class="btn-filter-lb" onclick="setLbFilterMode('all')" style="flex:1; padding:4px 6px; font-size:0.7rem; font-weight:700; border-radius:6px; border:1px solid #334155; background:#0f172a; color:#94a3b8; cursor:pointer;">🌟 Tất Cả Lượt Thi</button>
            </div>
            <div id="lb-window-info" style="font-size:0.65rem; color:#38bdf8; background:rgba(56,189,248,0.08); padding:4px 6px; border-radius:4px; margin-bottom:8px; text-align:center;">
                ⏱ Khung giờ: 14h00 Thứ Sáu -> 13h59 Thứ Sáu tuần sau
            </div>'''

if lb_target in html and 'id="btn-lb-official"' not in html:
    html = html.replace(lb_target, lb_replacement, 1)
    print("✓ Đã thêm Bộ lọc BXH Đua Top Tuần & Bộ chọn tuần Top 10")

# 4. Replace entire <script> logic from const SCHEDULE to end of script with modern robust engine
script_start_idx = html.find('        // LỊCH MỞ 35 CHẶNG THÁM HIỂM')
if script_start_idx != -1:
    script_end_idx = html.rfind('</script>')
    
    new_script_content = f'''        // LỊCH MỞ 35 CHẶNG THÁM HIỂM (2026 - 2027)
        const SCHEDULE = {json.dumps(SCHEDULE_CONFIG, ensure_ascii=False, indent=12)};

        let currentUsername = localStorage.getItem('studentUsername');
        let currentName = localStorage.getItem('studentName');
        let currentClass = localStorage.getItem('studentClass');
        let currentSchool = localStorage.getItem('studentSchool');
        let currentUserRole = localStorage.getItem('userRole') || 'guest';
        let currentUserStatus = localStorage.getItem('userStatus') || 'pending';
        let currentSelectedWeek = 1;
        let currentLbFilterMode = 'official'; // 'official' (14h T6 -> 13h59 T6 sau) | 'all'
        let noticeInterval;

        window.onload = function () {{
            // 1. Khởi tạo danh sách chọn tuần trên BXH
            initWeekSelectOptions();

            // 2. Tự động đồng bộ tài khoản từ Firebase
            if (currentUsername) {{
                db.ref('users/' + currentUsername).once('value', (snap) => {{
                    const u = snap.val();
                    if (!snap.exists()) {{
                        // Tài khoản không tồn tại trên máy chủ
                        localStorage.removeItem('studentUsername');
                        localStorage.removeItem('studentName');
                        localStorage.removeItem('studentClass');
                        localStorage.removeItem('studentSchool');
                        localStorage.removeItem('userRole');
                        localStorage.removeItem('userStatus');
                        localStorage.removeItem('adminUsername');
                        currentUsername = null;
                        currentName = null;
                        currentUserRole = 'guest';
                        currentUserStatus = 'pending';
                        updateUI();
                        renderStations();
                        loadLeaderboard(1);
                        showLoginModal();
                    }} else {{
                        // Cập nhật thông tin mới nhất
                        currentUserRole = u.role || 'student';
                        currentUserStatus = u.status || 'pending';
                        localStorage.setItem('userRole', currentUserRole);
                        localStorage.setItem('userStatus', currentUserStatus);
                        if (u.role === 'admin') {{
                            localStorage.setItem('adminUsername', u.username);
                        }}
                        updateUI();
                        renderStations();
                        loadLeaderboard(1);
                    }}
                }});
            }} else {{
                currentUserRole = 'guest';
                currentUserStatus = 'pending';
                updateUI();
                renderStations();
                loadLeaderboard(1);
            }}

            const mapImg = document.getElementById('map-img');
            if (mapImg.complete) {{ drawPaths(); }} else {{ mapImg.onload = drawPaths; }}
        }};

        function initWeekSelectOptions() {{
            const sel = document.getElementById('lb-week-select');
            if (!sel) return;
            sel.innerHTML = Array.from({{ length: 35 }}, (_, i) => 1 + i).map(w => 
                `<option value="${{w}}">Tuần ${{w}}</option>`
            ).join('');
            sel.value = currentSelectedWeek;
        }}

        function handleRegRoleChange() {{
            const isTeacher = document.querySelector('input[name="reg-role"]:checked').value === 'teacher';
            const classSelect = document.getElementById('input-reg-class');
            const classLabel = classSelect.previousElementSibling;
            if (isTeacher) {{
                classLabel.innerText = "5. Phụ trách Lớp:";
            }} else {{
                classLabel.innerText = "5. Lớp của em:";
            }}
        }}

        // RENDER ĐẦY ĐỦ 35 TRẠM TRÊN BẢN ĐỒ
        function renderStations() {{
            const holder = document.getElementById('stations-holder');
            holder.innerHTML = '';
            const now = new Date();
            const isApprovedTeacherOrAdmin = (currentUserRole === 'teacher' || currentUserRole === 'admin') && (currentUserStatus === 'approved');

            for (let i = 1; i <= 35; i++) {{
                const sched = SCHEDULE[i];
                const openTime = sched ? new Date(sched.open) : new Date(0);
                const isTimeLocked = now < openTime;
                const isGuestLocked = (i > 8) && (!currentUsername || currentUserStatus !== 'approved');

                let isLocked = false;
                let lockTitle = `Trạm ${{i}}`;

                if (isApprovedTeacherOrAdmin) {{
                    isLocked = false;
                    lockTitle = `Trạm ${{i}} (Quyền Thầy/Cô - Mở toàn bộ 35 tuần)`;
                }} else if (isGuestLocked) {{
                    isLocked = true;
                    lockTitle = `Trạm ${{i}} (Dành riêng cho tài khoản đã duyệt)`;
                }} else if (isTimeLocked) {{
                    isLocked = true;
                    lockTitle = `Trạm ${{i}} (Mở lúc ${{sched ? sched.open_str : '14:00 Thứ Sáu'}}`;
                }}

                const isMilestone = (i === 9 || i === 18 || i === 27 || i === 35);
                const milestoneClass = isMilestone ? ' milestone' : '';
                const lockedClass = isLocked ? ' locked' : '';

                holder.innerHTML += `
                    <div class="station${{milestoneClass}}${{lockedClass}}" id="st-${{i}}" onclick="handleStageClick(${{i}})" title="${{lockTitle}}">
                        ${{i}}
                    </div>
                `;
            }}
            setTimeout(drawPaths, 150);
        }}

        // VẼ ĐƯỜNG NỐI SVG
        function drawPaths() {{
            const svg = document.getElementById('path-svg');
            if (!svg) return;
            svg.innerHTML = '';
            const now = new Date();
            const isApprovedTeacherOrAdmin = (currentUserRole === 'teacher' || currentUserRole === 'admin') && (currentUserStatus === 'approved');

            for (let i = 1; i < 35; i++) {{
                const startEl = document.getElementById(`st-${{i}}`);
                const endEl = document.getElementById(`st-${{i + 1}}`);
                if (!startEl || !endEl) continue;

                const schedNext = SCHEDULE[i + 1];
                const openTimeNext = schedNext ? new Date(schedNext.open) : new Date(0);
                const canDraw = isApprovedTeacherOrAdmin || (now >= openTimeNext && (i + 1 <= 8 || (currentUsername && currentUserStatus === 'approved')));

                if (canDraw) {{
                    const x1 = startEl.offsetLeft;
                    const y1 = startEl.offsetTop;
                    const x2 = endEl.offsetLeft;
                    const y2 = endEl.offsetTop;

                    const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
                    line.setAttribute("x1", x1); line.setAttribute("y1", y1);
                    line.setAttribute("x2", x2); line.setAttribute("y2", y2);

                    const isSea = (i === 17 || i === 18 || i === 32 || i === 33 || i === 34);
                    line.setAttribute("class", isSea ? "sea-line" : "road-line");
                    svg.appendChild(line);
                }}
            }}
        }}
        window.onresize = drawPaths;

        // XỬ LÝ CLICK TRẠM
        function handleStageClick(no) {{
            const isApprovedTeacherOrAdmin = (currentUserRole === 'teacher' || currentUserRole === 'admin') && (currentUserStatus === 'approved');

            // 1. Kiểm tra giới hạn khách / chờ duyệt (tối đa vòng 8)
            if (no > 8) {{
                if (!currentUsername) {{
                    return showLockedStationNotice(
                        no,
                        "🔒 YÊU CẦU ĐĂNG KÝ TÀI KHOẢN",
                        `Trạm <b>${{no}}</b> thuộc hệ thống thử thách nâng cao dành riêng cho tài khoản chính thức.<br><br>` +
                        `• Khách được làm quen tự do từ <b>Trạm 1 đến Trạm 8</b>.<br>` +
                        `• Để tiếp tục từ <b>Trạm 9 đến 35</b>, em hãy nhấn Đăng ký hoặc Đăng nhập nhé!`
                    );
                }}
                if (currentUserStatus !== 'approved') {{
                    return showLockedStationNotice(
                        no,
                        "⏳ TÀI KHOẢN ĐANG CHỜ PHÊ DUYỆT",
                        `Tài khoản <b>@${{currentUsername}}</b> của ${{currentUserRole === 'teacher' ? 'Thầy/Cô' : 'em'}} hiện đang ở trạng thái <b>Chờ Ban Quản Trị phê duyệt</b>.<br><br>` +
                        `• Trong thời gian chờ duyệt, ${{currentUserRole === 'teacher' ? 'Thầy/Cô' : 'em'}} có thể trải nghiệm trước từ <b>Trạm 1 đến 8</b>.<br>` +
                        `• Vui lòng liên hệ Thầy/Cô Quản trị viên để được phê duyệt nhanh chóng!`
                    );
                }}
            }}

            // 2. Giáo viên & Admin đã duyệt: Vào thẳng bất kỳ trạm nào
            if (isApprovedTeacherOrAdmin) {{
                window.location.href = no + ".html";
                return;
            }}

            // 3. Học sinh đã duyệt: Kiểm tra thời gian mở theo lịch tự động (14:00 Thứ Sáu)
            const now = new Date();
            const sched = SCHEDULE[no];
            const openTime = sched ? new Date(sched.open) : new Date(0);
            if (now < openTime) {{
                return showNoticeCountdown(openTime, no, sched ? sched.open_str : null);
            }}

            // Đủ điều kiện: vào game
            window.location.href = no + ".html";
        }}

        function showLockedStationNotice(no, title, msg) {{
            document.getElementById('locked-modal-title').innerHTML = title;
            document.getElementById('locked-modal-msg').innerHTML = msg;
            const authBtn = document.getElementById('locked-btn-auth');
            if (!currentUsername) {{
                authBtn.innerText = "🚀 ĐĂNG NHẬP / ĐĂNG KÝ";
                authBtn.style.display = "inline-block";
            }} else {{
                authBtn.style.display = "none";
            }}
            document.getElementById('locked-station-overlay').style.display = 'flex';
        }}

        function closeLockedModal() {{
            document.getElementById('locked-station-overlay').style.display = 'none';
        }}

        function handleLockedModalAuth() {{
            closeLockedModal();
            showLoginModal();
        }}

        function showNoticeCountdown(endTime, weekNum, openStr) {{
            document.getElementById('countdown-overlay').style.display = 'flex';
            document.getElementById('notice-title').innerText = `CHẶNG ${{weekNum}} CHƯA MỞ`;
            clearInterval(noticeInterval);
            noticeInterval = setInterval(() => {{
                const dist = endTime - new Date();
                if (dist < 0) return location.reload();
                const d = Math.floor(dist / 86400000);
                const h = Math.floor((dist % 86400000) / 3600000);
                const m = Math.floor((dist % 3600000) / 60000);
                const s = Math.floor((dist % 60000) / 1000);
                document.getElementById('timer-display').innerText = `${{d}}n ${{h}}:${{m}}:${{s}}`;
            }}, 1000);
        }}

        function closeNotice() {{
            document.getElementById('countdown-overlay').style.display = 'none';
            clearInterval(noticeInterval);
        }}

        // ==========================================
        // QUẢN LÝ CỬA SỔ ĐĂNG NHẬP & ĐĂNG KÝ
        // ==========================================
        function showLoginModal() {{
            document.getElementById('auth-overlay').style.display = 'flex';
            document.getElementById('card-login').style.display = 'block';
            document.getElementById('card-register').style.display = 'none';
        }}

        function showRegisterModal() {{
            document.getElementById('auth-overlay').style.display = 'flex';
            document.getElementById('card-login').style.display = 'none';
            document.getElementById('card-register').style.display = 'block';
        }}

        function closeAuthModal() {{
            document.getElementById('auth-overlay').style.display = 'none';
        }}

        function toggleRegSchoolInput() {{
            const val = document.getElementById('input-reg-school-select').value;
            const manual = document.getElementById('input-reg-school-manual');
            manual.style.display = (val === 'other') ? 'block' : 'none';
        }}

        // 1. XỬ LÝ ĐĂNG NHẬP
        function handleLogin() {{
            const uInput = document.getElementById('input-login-username').value.trim().toLowerCase();
            const pInput = document.getElementById('input-login-password').value.trim();

            if (!uInput || uInput.length < 2) {{
                alert("Vui lòng nhập Tên đăng nhập của em!");
                document.getElementById('input-login-username').focus();
                return;
            }}
            if (!pInput) {{
                alert("Vui lòng nhập Mật khẩu!");
                document.getElementById('input-login-password').focus();
                return;
            }}

            db.ref('users/' + uInput).once('value', (snap) => {{
                const user = snap.val();
                if (user) {{
                    if (user.password && user.password !== pInput) {{
                        alert("Mật khẩu không chính xác, vui lòng thử lại!");
                        return;
                    }}
                    if (user.status === 'blocked') {{
                        alert("⚠️ Tài khoản của bạn đã bị khóa! Vui lòng liên hệ Thầy/Cô quản trị viên.");
                        return;
                    }}

                    localStorage.setItem('studentUsername', user.username || uInput);
                    localStorage.setItem('studentName', user.fullName);
                    localStorage.setItem('studentClass', user.className || '');
                    localStorage.setItem('studentSchool', user.schoolName || '');
                    localStorage.setItem('userRole', user.role || 'student');
                    localStorage.setItem('userStatus', user.status || 'pending');
                    if (user.role === 'admin') {{
                        localStorage.setItem('adminUsername', user.username || uInput);
                    }}

                    alert(`🎉 Chào mừng ${{user.fullName}} đã quay trở lại!`);
                    location.reload();
                }} else {{
                    alert("Tài khoản chưa tồn tại! Em hãy nhấn 'Đăng ký tài khoản mới' nhé.");
                }}
            }});
        }}

        // 2. XỬ LÝ ĐĂNG KÝ
        function handleRegister() {{
            const u = document.getElementById('input-reg-username').value.trim().toLowerCase();
            const p = document.getElementById('input-reg-password').value.trim();
            const n = document.getElementById('input-reg-name').value.trim();
            const sSelect = document.getElementById('input-reg-school-select').value;
            const c = document.getElementById('input-reg-class').value;
            const roleEl = document.querySelector('input[name="reg-role"]:checked');
            const selectedRole = roleEl ? roleEl.value : 'student';

            let s = sSelect;
            if (sSelect === 'other') {{
                s = document.getElementById('input-reg-school-manual').value.trim();
            }}

            if (!u || u.length < 3) {{
                alert("1. Tên đăng nhập phải từ 3 ký tự trở lên (viết liền không dấu)!");
                return;
            }}
            if (/[\\s\\W]/.test(u)) {{
                alert("1. Tên đăng nhập chỉ gồm chữ cái và số (ví dụ: nam5a1 hoặc lan_5b)!");
                return;
            }}
            if (!p || p.length < 4) {{
                alert("2. Mật khẩu phải có ít nhất 4 ký tự!");
                return;
            }}
            const draftKeywords = ['test', 'abc', 'nhap', 'nháp', '123', 'demo', 'đemo', 'xxx', 'utc', 'bts'];
            const nameLower = n.toLowerCase();
            const words = n.split(/\\s+/).filter(w => w.length > 0);
            if (draftKeywords.some(k => nameLower.includes(k)) || words.length < 2) {{
                alert("3. Vui lòng nhập đầy đủ Họ và Tên thật (ít nhất 2 từ)!");
                return;
            }}
            if (!s) {{
                alert("4. Vui lòng chọn hoặc nhập tên Trường của em!");
                return;
            }}
            if (!c) {{
                alert("5. Vui lòng chọn Lớp!");
                return;
            }}

            db.ref('users/' + u).once('value', (snap) => {{
                if (snap.exists()) {{
                    alert(`⚠️ Tên đăng nhập "${{u}}" đã có người sử dụng rồi! Em hãy chọn tên khác nhé.`);
                    return;
                }}

                const userData = {{
                    username: u,
                    password: p,
                    fullName: n,
                    className: c,
                    schoolName: s,
                    role: selectedRole,
                    status: (u === 'admin') ? 'approved' : 'pending',
                    createdAt: firebase.database.ServerValue.TIMESTAMP
                }};

                db.ref('users/' + u).set(userData, (err) => {{
                    if (err) {{
                        alert("Lỗi khi kết nối máy chủ, vui lòng thử lại!");
                        return;
                    }}
                    localStorage.setItem('studentUsername', u);
                    localStorage.setItem('studentName', n);
                    localStorage.setItem('studentClass', c);
                    localStorage.setItem('studentSchool', s);
                    localStorage.setItem('userRole', selectedRole);
                    localStorage.setItem('userStatus', userData.status);

                    alert(`✨ Đăng ký thành công!\n\nTài khoản của ${{selectedRole === 'teacher' ? 'Thầy/Cô' : 'em'}} đang ở trạng thái CHỜ PHÊ DUYỆT.\n${{selectedRole === 'teacher' ? 'Thầy/Cô' : 'Em'}} có thể trải nghiệm trước từ Vòng 1 đến 8!`);
                    location.reload();
                }});
            }});
        }}

        function updateUI() {{
            const authBtn = document.getElementById('btn-auth-action');
            const regBtn = document.getElementById('btn-footer-register');
            const infoBox = document.getElementById('user-info-box');

            if (currentName) {{
                let roleBadge = '';
                if (currentUserRole === 'admin') {{
                    roleBadge = '<span style="background:#e11d48; color:#fff; padding:1px 6px; border-radius:10px; font-size:0.65rem; font-weight:bold; margin-left:4px;">👑 QUẢN TRỊ</span>';
                }} else if (currentUserRole === 'teacher') {{
                    const stColor = currentUserStatus === 'approved' ? '#00f2ff' : '#ff9800';
                    const stText = currentUserStatus === 'approved' ? '🎓 GIÁO VIÊN' : '🎓 GV (Chờ duyệt)';
                    roleBadge = `<span style="background:rgba(0,242,255,0.15); color:${{stColor}}; border:1px solid ${{stColor}}; padding:1px 6px; border-radius:10px; font-size:0.65rem; font-weight:bold; margin-left:4px;">${{stText}}</span>`;
                }} else {{
                    const stColor = currentUserStatus === 'approved' ? '#2ecc71' : '#ff9800';
                    const stText = currentUserStatus === 'approved' ? '⭐ ĐÃ DUYỆT' : '⏳ CHỜ DUYỆT';
                    roleBadge = `<span style="background:rgba(46,204,113,0.15); color:${{stColor}}; border:1px solid ${{stColor}}; padding:1px 6px; border-radius:10px; font-size:0.65rem; font-weight:bold; margin-left:4px;">${{stText}}</span>`;
                }}

                infoBox.innerHTML = `
                    <div style="display:flex; align-items:center; flex-wrap:wrap;">
                        <span style="font-size:0.95rem; font-weight:bold; color:var(--gold);">${{currentName}}</span>
                        ${{roleBadge}}
                    </div>
                    <span style="font-size:0.75rem; color:var(--text-sec);">${{currentClass}} • @${{currentUsername || ''}}</span>
                    <span style="font-size:0.65rem; color:#94a3b8;">${{currentSchool || ''}}</span>
                `;
                authBtn.innerHTML = "⚙️ ĐĂNG XUẤT";
                authBtn.style.color = "#ff5252";
                authBtn.style.borderColor = "#ff5252";
                if (regBtn) regBtn.style.display = "none";

                // If Admin or Teacher, inject Admin Portal button in footer if not existing
                if ((currentUserRole === 'admin' || currentUserRole === 'teacher') && currentUserStatus === 'approved') {{
                    if (!document.getElementById('btn-admin-portal-nav')) {{
                        const footerBtns = document.querySelector('.footer-buttons');
                        if (footerBtns) {{
                            const aAdmin = document.createElement('a');
                            aAdmin.id = 'btn-admin-portal-nav';
                            aAdmin.href = 'admin.html';
                            aAdmin.className = 'btn-nav';
                            aAdmin.style.cssText = 'color:#fff; background:#e11d48; border-color:#e11d48; font-weight:bold;';
                            aAdmin.innerHTML = '🛡️ PHÊ DUYỆT';
                            footerBtns.insertBefore(aAdmin, authBtn);
                        }}
                    }}
                }}
            }} else {{
                infoBox.innerHTML = `
                    <span style="font-size:0.95rem; font-weight:bold; color:var(--gold);">Khách</span>
                    <span style="font-size:0.75rem; color:var(--text-sec);">Trải nghiệm Vòng 1-8</span>
                `;
                authBtn.innerHTML = "🚀 ĐĂNG NHẬP";
                authBtn.style.color = "var(--p)";
                authBtn.style.borderColor = "var(--p)";
                if (regBtn) regBtn.style.display = "inline-flex";
            }}
        }}

        function handleAuthAction() {{
            if (currentName) {{
                if (confirm(`Đăng xuất tài khoản @${{currentUsername || currentName}}?`)) {{
                    localStorage.removeItem('studentUsername');
                    localStorage.removeItem('studentName');
                    localStorage.removeItem('studentClass');
                    localStorage.removeItem('studentSchool');
                    localStorage.removeItem('userRole');
                    localStorage.removeItem('userStatus');
                    localStorage.removeItem('adminUsername');
                    location.reload();
                }}
            }} else {{
                showLoginModal();
            }}
        }}

        function formatTime(sec) {{
            if (!sec) return "00:00";
            const m = Math.floor(sec / 60), s = sec % 60;
            return `${{m.toString().padStart(2, '0')}}:${{s.toString().padStart(2, '0')}}`;
        }}

        function setLbFilterMode(mode) {{
            currentLbFilterMode = mode;
            const btnOff = document.getElementById('btn-lb-official');
            const btnAll = document.getElementById('btn-lb-all');
            if (btnOff && btnAll) {{
                if (mode === 'official') {{
                    btnOff.style.background = 'var(--p)';
                    btnOff.style.color = '#000';
                    btnOff.style.borderColor = 'var(--p)';
                    btnAll.style.background = '#0f172a';
                    btnAll.style.color = '#94a3b8';
                    btnAll.style.borderColor = '#334155';
                }} else {{
                    btnAll.style.background = 'var(--p)';
                    btnAll.style.color = '#000';
                    btnAll.style.borderColor = 'var(--p)';
                    btnOff.style.background = '#0f172a';
                    btnOff.style.color = '#94a3b8';
                    btnOff.style.borderColor = '#334155';
                }}
            }}
            loadLeaderboard(currentSelectedWeek);
        }}

        function loadLeaderboard(weekNum) {{
            currentSelectedWeek = weekNum;
            const sel = document.getElementById('lb-week-select');
            if (sel) sel.value = weekNum;

            const sched = SCHEDULE[weekNum];
            document.getElementById('lb-title').innerText = `🏆 TOP 10 - TUẦN ${{weekNum}}`;

            const winInfo = document.getElementById('lb-window-info');
            if (winInfo && sched) {{
                winInfo.innerText = currentLbFilterMode === 'official' 
                    ? `⏱ Khung giờ Đua Top: ${{sched.open_str}} -> ${{sched.close_str}}`
                    : `🌟 Chế độ xem: Toàn bộ lượt thi tự luyện của học sinh`;
            }}

            db.ref(`scores/Tuan_${{weekNum}}`).on('value', (snap) => {{
                const data = snap.val();
                const listUI = document.getElementById('leaderboard-list-ui');
                if (!data) {{
                    listUI.innerHTML = '<tr><td colspan="4">Chưa có dữ liệu tuần này</td></tr>';
                    document.getElementById('high-score').innerText = '0';
                    return;
                }}
                let all = []; for (let id in data) all.push(data[id]);

                // Lọc loại bỏ dữ liệu nháp
                const draftKeywords = ['test', 'abc', 'nhap', 'nháp', '123', 'demo', 'đemo', 'xxx', '...', '---', 'utc', 'bts', 'admin'];
                all = all.filter(s => {{
                    let nameValue = (s.fullName || s.name || "").trim();
                    let nameLower = nameValue.toLowerCase();
                    if (draftKeywords.some(k => nameLower.includes(k))) return false;
                    if (/^\\d+$/.test(nameLower)) return false;
                    const words = nameValue.split(/\\s+/).filter(w => w.length > 0);
                    if (words.length < 2) return false;
                    if (words.some(w => w.length > 15)) return false;
                    return true;
                }});

                // Lọc theo khung giờ chính thức (14:00 Thứ Sáu -> 13:59:59 Thứ Sáu sau) nếu chọn chế độ 'official'
                if (currentLbFilterMode === 'official' && sched) {{
                    const openMs = new Date(sched.open).getTime();
                    const closeMs = new Date(sched.close).getTime();
                    all = all.filter(s => {{
                        if (s.timestamp) {{
                            return s.timestamp >= openMs && s.timestamp <= closeMs;
                        }}
                        return true;
                    }});
                }}

                all.sort((a, b) => (b.score !== a.score) ? b.score - a.score : (a.duration || 999) - (b.duration || 999));
                const top10 = []; const seen = new Set();
                for (let s of all) {{
                    let key = ((s.fullName || s.name) + (s.className || s.class)).toLowerCase();
                    if (!seen.has(key)) {{ top10.push(s); seen.add(key); }}
                    if (top10.length >= 10) break;
                }}

                if (top10.length === 0) {{
                    listUI.innerHTML = '<tr><td colspan="4" style="color:#94a3b8; padding:12px;">Chưa có bài nộp hợp lệ trong khung giờ này</td></tr>';
                    document.getElementById('high-score').innerText = '0';
                    return;
                }}

                listUI.innerHTML = top10.map((s, i) => `
                    <tr>
                        <td>${{i + 1}}</td>
                        <td style="text-align:left;">
                            <span style="display:block; font-weight:bold; color:#fff;">${{s.fullName || s.name}}</span>
                            <span style="display:block; font-size:0.75rem; color:#94a3b8; margin-top:2px;">${{s.className || s.class}}</span>
                            <span style="display:block; font-size:0.65rem; color:#64748b; margin-top:2px;">${{s.schoolName || '---'}}</span>
                        </td>
                        <td style="color:var(--p); font-weight:bold;">${{s.score}}</td>
                        <td style="color:#2ecc71;">${{formatTime(s.duration)}}</td>
                    </tr>
                `).join('');
                if (top10.length > 0) document.getElementById('high-score').innerText = top10[0].score;
            }});
        }}

        function shareGame() {{
            const data = {{ title: 'Thám hiểm Việt Nam cùng Robot', text: 'Thách đấu bạn giải toán thám hiểm!', url: window.location.href }};
            if (navigator.share) navigator.share(data); else {{ navigator.clipboard.writeText(window.location.href); alert('Đã sao chép link!'); }}
        }}
    </script>
</body>

</html>
'''
    html = html[:script_start_idx] + new_script_content
    print("✓ Đã thay thế toàn bộ script điều khiển của index.html với logic Phân quyền & Lịch mới")

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("✓ Đã lưu index.html thành công!")
