# -*- coding: utf-8 -*-
"""
Dữ liệu Lịch mở thử thách 35 tuần năm học 2026 - 2027
EduRobot Toán 5
- Khai giảng: Thứ 2, ngày 07/09/2026
- Mở tự động: 14:00 Thứ Sáu hàng tuần
- Nghỉ Tết Nguyên Đán: 01/02/2027 - 14/02/2027 (2 tuần không mở vòng mới)
- Chốt Bảng Vàng: 14:00 Thứ Sáu tuần đó đến 13:59:59 Thứ Sáu tuần kế tiếp
"""

from datetime import datetime, timedelta

d_start = datetime(2026, 9, 7) # Monday
tet_start = datetime(2027, 2, 1) # Monday
tet_end = datetime(2027, 2, 14) # Sunday

current_monday = d_start
week_num = 1
SCHEDULE_CONFIG = {}

while week_num <= 35:
    current_friday = current_monday + timedelta(days=4)
    if tet_start <= current_monday <= tet_end:
        current_monday += timedelta(weeks=1)
        continue
    
    open_time = current_friday.replace(hour=14, minute=0, second=0)
    
    # Calculate close time (when next week opens, or next Friday after Tet)
    next_monday = current_monday + timedelta(weeks=1)
    while tet_start <= next_monday <= tet_end:
        next_monday += timedelta(weeks=1)
    next_friday = next_monday + timedelta(days=4)
    close_time = next_friday.replace(hour=13, minute=59, second=59)

    SCHEDULE_CONFIG[week_num] = {
        "week": week_num,
        "monday": current_monday.strftime("%Y-%m-%d"),
        "open": open_time.strftime("%Y-%m-%dT%H:%M:%S"),
        "close": close_time.strftime("%Y-%m-%dT%H:%M:%S"),
        "open_str": open_time.strftime("%H:%M ngày %d/%m/%Y"),
        "close_str": close_time.strftime("%H:%M:%S ngày %d/%m/%Y"),
        "is_cap_for_guest": (week_num == 8)
    }
    current_monday += timedelta(weeks=1)
    week_num += 1

if __name__ == "__main__":
    import json
    print(json.dumps(SCHEDULE_CONFIG, indent=2, ensure_ascii=False))
