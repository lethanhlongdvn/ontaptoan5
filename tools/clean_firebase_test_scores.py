# -*- coding: utf-8 -*-
"""
CÔNG CỤ SAO LƯU & DỌN DẸP LƯỢT THI THỬ NGHIỆM TRÊN FIREBASE
Hệ thống EduBot Toán 5

Cách dùng:
  - Xem danh sách lượt thi thử nghiệm (không xóa):
      python tools/clean_firebase_test_scores.py
  - Thực hiện dọn dẹp thật (có tự động sao lưu trước):
      python tools/clean_firebase_test_scores.py --apply
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

DRAFT_KEYWORDS = ['test', 'abc', 'nhap', 'nháp', '123', 'demo', 'đemo', 'xxx', '...', '---', 'utc', 'bts', 'admin']

def is_draft_entry(item):
    name = (item.get('fullName') or item.get('name') or item.get('username') or '').strip().lower()
    if any(k in name for k in DRAFT_KEYWORDS):
        return True
    if name.isdigit():
        return True
    words = name.split()
    if len(words) < 2:
        return True
    return False

def main():
    apply_mode = "--apply" in sys.argv
    print("=" * 65)
    print("CÔNG CỤ KIỂM TRA & DỌN DẸP DỮ LIỆU ĐIỂM SỐ TRÊN FIREBASE")
    print(f"Chế độ: {'THỰC THI XÓA (CÓ SAO LƯU)' if apply_mode else 'XEM THỬ / DRY-RUN (AN TOÀN)'}")
    print("=" * 65)

    print("\n1. Đang tải dữ liệu điểm số từ Firebase...")
    url = f"{FIREBASE_DB_URL}/scores.json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8')) or {}
    except Exception as e:
        print(f"  ✗ Lỗi kết nối Firebase: {e}")
        return

    # Tự động sao lưu dữ liệu hiện tại
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"firebase_scores_backup_{timestamp}.json")
    with open(backup_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  ✓ Đã tự động sao lưu toàn bộ điểm số vào:\n    {backup_file}")

    # Quét dữ liệu rác
    total_entries = 0
    draft_entries = []
    for tuan_key, records in data.items():
        if not isinstance(records, dict):
            continue
        for push_id, item in records.items():
            if not isinstance(item, dict):
                continue
            total_entries += 1
            if is_draft_entry(item):
                name = item.get('fullName') or item.get('name') or item.get('username') or 'Unknown'
                draft_entries.append((tuan_key, push_id, name, item.get('score', 0)))

    print(f"\n2. Kết quả kiểm tra:")
    print(f"  - Tổng số lượt thi đang lưu trên máy chủ: {total_entries}")
    print(f"  - Số lượt thi thử nghiệm (test/nháp/demo) phát hiện: {len(draft_entries)}")

    if draft_entries:
        print("\n  Danh sách lượt thi phát hiện:")
        for tk, pid, name, sc in draft_entries[:20]:
            print(f"    • [{tk}] {name} - Điểm: {sc} (ID: {pid[:8]}...)")
        if len(draft_entries) > 20:
            print(f"    ... và {len(draft_entries) - 20} lượt thi khác.")

    if not draft_entries:
        print("\n🎉 Cơ sở dữ liệu hoàn toàn sạch sẽ! Không có dữ liệu rác.")
        return

    if not apply_mode:
        print("\n💡 GỢI Ý:")
        print("  Hiện tại đang ở chế độ xem thử an toàn. Để xóa các lượt thi thử nghiệm này khỏi Firebase, chạy:")
        print("    python tools/clean_firebase_test_scores.py --apply")
    else:
        print("\n3. Đang thực thi dọn dẹp các lượt thi thử nghiệm...")
        deleted_count = 0
        for tk, pid, name, sc in draft_entries:
            del_url = f"{FIREBASE_DB_URL}/scores/{tk}/{pid}.json"
            del_req = urllib.request.Request(del_url, method='DELETE')
            try:
                with urllib.request.urlopen(del_req) as resp:
                    deleted_count += 1
            except Exception as e:
                print(f"    ✗ Lỗi khi xóa {pid}: {e}")
        print(f"  ✓ Đã dọn dẹp thành công {deleted_count}/{len(draft_entries)} lượt thi rác trên Firebase!")
        print("  Hệ thống sẵn sàng 100% cho học sinh chính thức vào thi!")

if __name__ == "__main__":
    main()
