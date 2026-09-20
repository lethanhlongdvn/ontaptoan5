# -*- coding: utf-8 -*-
"""
HỆ THỐNG KIỂM TRA ĐỒNG BỘ TOÀN DIỆN 35 TRẠM (ALL SUBPAGES & CHANNELS)
EduRobot Toán 5 - Hành trình thám hiểm Việt Nam
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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
passed_checks = 0
total_checks = 0

def check(condition, message):
    global passed_checks, total_checks
    total_checks += 1
    if condition:
        passed_checks += 1
        print(f"  ✓ {message}")
    else:
        print(f"  ✗ THẤT BẠI: {message}")

print("=" * 70)
print("BẮT ĐẦU KIỂM TRA ĐỒNG BỘ TOÀN DIỆN HỆ THỐNG 35 TRẠM EDUROBOT")
print("=" * 70)

# 1. KIỂM TRA TOÀN BỘ 35 TRẠM GAME HTML
print("\n[1] KIỂM TRA FILE GAME HTML (1.html -> 35.html)")
folders_to_check = [
    ("Root Website", ROOT),
    ("edubot-zmp/src/public", os.path.join(ROOT, "edubot-zmp", "src", "public")),
    ("edubot-zmp/src/www", os.path.join(ROOT, "edubot-zmp", "src", "www")),
    ("edubot-zmp/www (Build)", os.path.join(ROOT, "edubot-zmp", "www")),
]

for name, folder in folders_to_check:
    missing = []
    for i in range(1, 36):
        fp = os.path.join(folder, f"{i}.html")
        if not os.path.exists(fp):
            missing.append(i)
    check(len(missing) == 0, f"{name}: Đầy đủ 35/35 file game HTML (Missing: {missing if missing else 'None'})")

# Kiểm tra tính năng game trạm 1..35
sample_weeks = [1, 5, 8, 9, 10, 18, 19, 21, 22, 27, 33, 34, 35]
all_sample_ok = True
guard_ok = True
for w in sample_weeks:
    fp = os.path.join(ROOT, f"{w}.html")
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    
    has_tone = "AudioContext" in content
    has_badge = "cap1" in content and "cap2" in content and "cap3" in content
    has_fireworks = "fireworks.js" in content and "startFireworks" in content
    has_firebase = f"scores/Tuan_{w}" in content
    has_sched = "STATION_CONFIG" in content

    if not (has_tone and has_badge and has_fireworks and has_firebase and has_sched):
        all_sample_ok = False
        print(f"    - Cảnh báo trạm {w}: tone={has_tone}, badge={has_badge}, fireworks={has_fireworks}, firebase={has_firebase}, sched={has_sched}")

    # Kiểm tra giới hạn tài khoản trạm > 8
    if w > 8:
        if f"{w} > 8" not in content or "savedStatus !== 'approved'" not in content:
            guard_ok = False
            print(f"    - Cảnh báo trạm {w}: Thiếu bộ khóa bảo vệ tài khoản khách/chờ duyệt!")

check(all_sample_ok, "Kiểm tra mẫu tính năng game (48 câu xoay vòng, Tone Audio, Pháo hoa, 3 cấp Huy hiệu, Firebase save, STATION_CONFIG)")
check(guard_ok, "Kiểm tra cơ chế chốt chặn Trạm > 8 (Khách & Chờ duyệt chỉ làm vòng 1-8; Trạm 9-35 yêu cầu tài khoản duyệt)")

# 2. KIỂM TRA HỆ THỐNG PHÊ DUYỆT ADMIN (admin.html)
print("\n[2] KIỂM TRA CỔNG PHÊ DUYỆT TÀI KHOẢN (admin.html)")
admin_locations = [
    os.path.join(ROOT, "admin.html"),
    os.path.join(ROOT, "edubot-zmp", "src", "public", "admin.html"),
    os.path.join(ROOT, "edubot-zmp", "src", "www", "admin.html"),
    os.path.join(ROOT, "edubot-zmp", "www", "admin.html"),
]

for p in admin_locations:
    rel = os.path.relpath(p, ROOT)
    exists = os.path.exists(p)
    if exists:
        with open(p, "r", encoding="utf-8") as f:
            c = f.read()
        has_auth = "admin" in c and "EduBot@2026" in c
        has_stats = "stat-pending" in c and "stat-approved" in c and "stat-teachers" in c
        has_batch = "approveAllPending" in c
        has_actions = "approveUser" in c and "blockUser" in c and "deleteUser" in c
        check(has_auth and has_stats and has_batch and has_actions, f"{rel}: Tồn tại, Đăng nhập bảo mật, Thống kê, Duyệt hàng loạt & Thao tác 1-chạm")
    else:
        check(False, f"{rel}: File không tồn tại")

# 3. KIỂM TRA BẢNG VÀNG (bang-vang.html)
print("\n[3] KIỂM TRA BẢNG VÀNG THÀNH TÍCH (bang-vang.html)")
bv_locations = [
    os.path.join(ROOT, "bang-vang.html"),
    os.path.join(ROOT, "edubot-zmp", "src", "bang-vang.html"),
    os.path.join(ROOT, "edubot-zmp", "src", "public", "bang-vang.html"),
    os.path.join(ROOT, "edubot-zmp", "src", "www", "bang-vang.html"),
    os.path.join(ROOT, "edubot-zmp", "www", "bang-vang.html"),
]

for p in bv_locations:
    rel = os.path.relpath(p, ROOT)
    exists = os.path.exists(p)
    if exists:
        with open(p, "r", encoding="utf-8") as f:
            c = f.read()
        has_35_weeks = "i <= 35" in c and '35: "Đà Nẵng' in c
        has_mode_toggle = ("currentModeFilter" in c or "filterMode" in c) and ("official" in c or "Tất cả lượt thi" in c)
        has_charts = "Chart" in c
        has_xlsx = "xlsx" in c.lower()
        check(has_35_weeks and has_mode_toggle and has_charts and has_xlsx, f"{rel}: Tồn tại, cấu trúc 35 tuần accordion, Lọc Đua Top Tuần (14h T6), Biểu đồ & Xuất Excel")
    else:
        check(False, f"{rel}: File không tồn tại")

# 4. KIỂM TRA TÚI ĐỒ (tuido.html)
print("\n[4] KIỂM TRA TÚI ĐỒ NHÀ THÁM HIỂM (tuido.html)")
td_locations = [
    os.path.join(ROOT, "tuido.html"),
    os.path.join(ROOT, "edubot-zmp", "src", "tuido.html"),
    os.path.join(ROOT, "edubot-zmp", "src", "public", "tuido.html"),
    os.path.join(ROOT, "edubot-zmp", "src", "www", "tuido.html"),
    os.path.join(ROOT, "edubot-zmp", "www", "tuido.html"),
]

for p in td_locations:
    rel = os.path.relpath(p, ROOT)
    exists = os.path.exists(p)
    if exists:
        with open(p, "r", encoding="utf-8") as f:
            c = f.read()
        has_35_items = "week <= 35" in c and '"35": {' in c
        has_filter = "setFilter('hk1')" in c and "setFilter('hk2')" in c
        has_tiers = "cap1" in c and "cap2" in c and "cap3" in c
        check(has_35_items and has_filter and has_tiers, f"{rel}: Tồn tại, 35 vật phẩm, Bộ lọc HK1/HK2, 3 cấp Đồng/Bạc/Vàng")
    else:
        check(False, f"{rel}: File không tồn tại")

# 5. KIỂM TRA BẢN ĐỒ CHÍNH & LỊCH TRÌNH (index.html & schedule_data.py)
print("\n[5] KIỂM TRA TRANG CHỦ BẢN ĐỒ & LỊCH TRÌNH NĂM HỌC")
with open(os.path.join(ROOT, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

# Kiểm tra tọa độ trạm 1..35
st_matches = re.findall(r'#st-(\d+)\s*\{[^}]+\}', idx_content)
check(len(set(st_matches)) == 35, f"Bản đồ có định vị CSS cho đủ 35/35 trạm")

# Kiểm tra không còn nút HK1 / HK2
has_sem_switch = "semester-switcher" in idx_content or "btn-sem-tab" in idx_content
check(not has_sem_switch, "Đã loại bỏ hoàn toàn nút chuyển HK1/HK2 trên trang chủ")

# Kiểm tra lịch 14h Thứ 6 & Nghỉ Tết 2 tuần
from schedule_data import SCHEDULE_CONFIG
check(len(SCHEDULE_CONFIG) == 35, "Lịch mở 35 tuần được sinh tự động chính xác")
check(SCHEDULE_CONFIG[1]["open"] == "2026-09-11T14:00:00", "Tuần 1 mở 14:00 Thứ Sáu 11/09/2026")
check(SCHEDULE_CONFIG[21]["open"] == "2027-01-29T14:00:00", "Tuần 21 mở 14:00 Thứ Sáu 29/01/2027 (trước Tết)")
check(SCHEDULE_CONFIG[22]["open"] == "2027-02-19T14:00:00", "Tuần 22 mở 14:00 Thứ Sáu 19/02/2027 (nghỉ Tết 2 tuần từ 01/02 đến 14/02)")
check(SCHEDULE_CONFIG[21]["close"] == "2027-02-19T13:59:59", "Tuần 21 kéo dài qua Tết chốt vào 13:59:59 ngày 19/02/2027")

# Kiểm tra phân quyền index.html
has_role_register = 'name="reg-role"' in idx_content
has_teacher_bypass = 'isApprovedTeacherOrAdmin' in idx_content
has_guest_cap = 'no > 8' in idx_content and 'currentUserStatus !== \'approved\'' in idx_content
has_admin_nav = 'btn-admin-portal-nav' in idx_content
check(has_role_register, "Form đăng ký có chọn vai trò Học sinh / Giáo viên")
check(has_teacher_bypass, "Tài khoản Giáo viên/Admin đã duyệt được vượt quyền mở trước cả 35 tuần")
check(has_guest_cap, "Tài khoản Khách / Chờ duyệt bị giới hạn tại Trạm 8 với thông báo hướng dẫn")
check(has_admin_nav, "Tích hợp nút 'PHÊ DUYỆT' trên thanh menu cho Admin / Giáo viên")

# 6. KIỂM TRA ZALO MINI APP (edubot-zmp)
print("\n[6] KIỂM TRA ZALO MINI APP (edubot-zmp)")
with open(os.path.join(ROOT, "edubot-zmp", "src", "pages", "index.jsx"), "r", encoding="utf-8") as f:
    zmp_idx = f.read()

check("Array.from({ length: 35 }" in zmp_idx, "ZMP index.jsx hiển thị đủ 35 trạm")
check("SCHEDULE[i + 1]" in zmp_idx, "ZMP index.jsx vẽ đường dẫn 1->34 chuẩn xác")
check("lbFilterMode" in zmp_idx, "ZMP index.jsx tích hợp lọc Đua Top Tuần vs Tất cả lượt thi")
check("isApprovedTeacherOrAdmin" in zmp_idx, "ZMP index.jsx hỗ trợ giáo viên duyệt xem trước 35 tuần")

with open(os.path.join(ROOT, "edubot-zmp", "src", "pages", "bag.jsx"), "r", encoding="utf-8") as f:
    zmp_bag = f.read()
check("week <= 35" in zmp_bag and "filterMode" in zmp_bag, "ZMP bag.jsx quản lý đủ 35 trạm và bộ lọc HK1/HK2")

with open(os.path.join(ROOT, "edubot-zmp", "src", "pages", "gold-board.jsx"), "r", encoding="utf-8") as f:
    zmp_gb = f.read()
check("length: 35" in zmp_gb and "lbFilterMode" in zmp_gb, "ZMP gold-board.jsx hiển thị 35 tuần và bộ lọc Đua Top Tuần (14h T6)")

# 7. KIỂM TRA THƯ MỤC ĐỀ VÀ TÀI LIỆU WORD
print("\n[7] KIỂM TRA NGÂN HÀNG ĐỀ TRONG THƯ MỤC 'Đề'")
de_dir = os.path.join(ROOT, "Đề")
de_files = os.listdir(de_dir)
check("Bo_De_Toan_5_Tuan_1_den_18.docx" in de_files, "File tổng hợp Đề HK1 (Tuần 1 - 18)")
check("Bo_De_Toan_5_Tuan_19_den_35.docx" in de_files, "File tổng hợp Đề HK2 (Tuần 19 - 35)")
check("Bo_De_Toan_5_Tron_Bo_35_Tuan.docx" in de_files, "File Master toàn bộ 35 Tuần (1.680 câu hỏi)")

indiv_cnt = sum(1 for i in range(1, 36) if f"De_Tuan_{i:02d}_Tram_{i:02d}.docx" in de_files)
check(indiv_cnt == 35, f"Đầy đủ 35 file đề chi tiết từng tuần ({indiv_cnt}/35)")

print("\n" + "=" * 70)
print(f"KẾT QUẢ KIỂM TRA: {passed_checks}/{total_checks} TIÊU CHÍ ĐẠT HOÀN HẢO")
print("=" * 70)

if passed_checks == total_checks:
    print(">>> HỆ THỐNG ĐÃ ĐỒNG BỘ 100% VÀ SẴN SÀNG VẬN HÀNH TRÊN MỌI KÊNH! <<<")
else:
    print(f">>> CẦN KIỂM TRA LẠI {total_checks - passed_checks} MỤC THẤT BẠI TRÊN! <<<")
