# -*- coding: utf-8 -*-
"""
CÔNG CỤ TỰ ĐỘNG QUÉT & DỌN DẸP ĐIỂM SỐ CỦA CÁC TÀI KHOẢN ĐÃ BỊ XÓA (ORPHANED SCORES)
EduBot - Toán 5 Cùng Robot

Cách dùng:
  - Xem danh sách điểm mồ côi (không xóa):
      python tools/clean_orphaned_scores.py
  - Thực hiện dọn dẹp triệt để trên Firebase (tự động sao lưu trước):
      python tools/clean_orphaned_scores.py --apply
"""

import os
import sys
import json
import urllib.request
from datetime import datetime

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKUP_DIR = os.path.join(ROOT, "backup")
FIREBASE_DB_URL = "https://gamhoctap-default-rtdb.asia-southeast1.firebasedatabase.app"

def main():
    apply_mode = "--apply" in sys.argv
    print("=" * 70)
    print("CÔNG CỤ ĐỒNG BỘ & DỌN DẸP ĐIỂM THI CỦA TÀI KHOẢN ĐÃ BỊ XÓA")
    print(f"Chế độ: {'THỰC THI XÓA TRIỆT ĐỂ (CÓ SAO LƯU)' if apply_mode else 'XEM THỬ / DRY-RUN (AN TOÀN)'}")
    print("=" * 70)

    # 1. Tải danh sách users hiện tại
    print("\n1. Đang tải danh sách tài khoản hiện tại từ Firebase...")
    req_u = urllib.request.Request(f"{FIREBASE_DB_URL}/users.json", headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req_u) as resp:
            users_data = json.loads(resp.read().decode('utf-8')) or {}
    except Exception as e:
        print(f"  ✗ Lỗi tải users: {e}")
        return

    valid_usernames = set(k.lower() for k in users_data.keys())
    print(f"  ✓ Tìm thấy {len(users_data)} tài khoản hợp lệ đang tồn tại trong hệ thống.")

    # 2. Tải toàn bộ scores
    print("\n2. Đang tải toàn bộ dữ liệu điểm số (35 tuần) từ Firebase...")
    req_s = urllib.request.Request(f"{FIREBASE_DB_URL}/scores.json", headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req_s) as resp:
            scores_data = json.loads(resp.read().decode('utf-8')) or {}
    except Exception as e:
        print(f"  ✗ Lỗi tải scores: {e}")
        return

    # Tự động sao lưu dữ liệu hiện tại
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"firebase_scores_backup_before_orphan_clean_{timestamp}.json")
    with open(backup_file, "w", encoding="utf-8") as f:
        json.dump(scores_data, f, ensure_ascii=False, indent=2)
    print(f"  ✓ Đã tự động sao lưu toàn bộ điểm số hiện tại vào:\n    {backup_file}")

    # 3. Phân tích điểm mồ côi
    total_scores = 0
    orphans = [] # list of (week_key, push_id, username, full_name, score)
    by_student = {}

    for week_key, records in scores_data.items():
        if not isinstance(records, dict):
            continue
        for push_id, item in records.items():
            if not isinstance(item, dict):
                continue
            total_scores += 1
            uname = (item.get('username') or '').strip().lower()
            fname = (item.get('fullName') or item.get('name') or '').strip()
            score = item.get('score', 0)

            # Bỏ qua tài khoản khách hợp lệ (guest_...)
            if uname.startswith('guest_'):
                continue

            # Nếu có username mà không tồn tại trong danh sách users -> điểm mồ côi
            if uname and uname not in valid_usernames:
                orphans.append((week_key, push_id, uname, fname, score))
                lbl = f"@{uname} ({fname or 'Không rõ tên'})"
                by_student[lbl] = by_student.get(lbl, 0) + 1

    print(f"\n3. Kết quả phân tích:")
    print(f"  - Tổng số lượt thi đang có trên hệ thống: {total_scores}")
    print(f"  - Số lượt thi của tài khoản ĐÃ BỊ XÓA: {len(orphans)}")

    if not orphans:
        print("\n🎉 Tuyệt vời! Toàn bộ điểm số trên Bảng Vàng đều hoàn toàn đồng bộ với danh sách tài khoản hiện hữu.")
        return

    print(f"\n  Chi tiết theo từng tài khoản đã xóa ({len(by_student)} thí sinh):")
    for lbl, count in sorted(by_student.items(), key=lambda x: -x[1]):
        print(f"    • {lbl}: {count} lượt thi còn lưu trên Bảng Vàng")

    if not apply_mode:
        print("\n💡 GỢI Ý:")
        print("  Để thực hiện xóa sạch toàn bộ các lượt thi mồ côi này khỏi Firebase, chạy:")
        print("    python tools/clean_orphaned_scores.py --apply")
        return

    # 4. Thực thi dọn dẹp nếu có cờ --apply
    print(f"\n4. Đang tiến hành xóa triệt để {len(orphans)} lượt thi mồ côi trên Firebase...")
    deleted_count = 0
    for week_key, push_id, uname, fname, score in orphans:
        del_url = f"{FIREBASE_DB_URL}/scores/{week_key}/{push_id}.json"
        del_req = urllib.request.Request(del_url, method='DELETE')
        try:
            with urllib.request.urlopen(del_req) as resp:
                deleted_count += 1
        except Exception as e:
            print(f"    ✗ Lỗi khi xóa {week_key}/{push_id}: {e}")

    print(f"\n✅ ĐÃ DỌN DẸP THÀNH CÔNG {deleted_count}/{len(orphans)} LƯỢT THI MỒ CÔI!")
    print("✨ Bảng Vàng hiện đã hoàn toàn sạch sẽ và đồng bộ 100% với danh sách thành viên hiện có.")

if __name__ == "__main__":
    main()
