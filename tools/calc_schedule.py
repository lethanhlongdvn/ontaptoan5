import sys
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from datetime import datetime, timedelta

d_start = datetime(2026, 9, 7) # Monday
tet_start = datetime(2027, 2, 1) # Monday
tet_end = datetime(2027, 2, 14) # Sunday

current_monday = d_start
week_num = 1
schedule = {}

print("=== LỊCH MỞ THỬ THÁCH 35 TUẦN (NĂM HỌC 2026 - 2027) ===")
while week_num <= 35:
    current_friday = current_monday + timedelta(days=4)
    # Check if this Monday falls in Tet break
    if tet_start <= current_monday <= tet_end:
        print(f"*** NGHỈ TẾT NGUYÊN ĐÁN (1/2/2027 - 14/2/2027): Thứ 2 {current_monday.strftime('%d/%m/%Y')} ***")
        current_monday += timedelta(weeks=1)
        continue
    open_time = current_friday.replace(hour=14, minute=0, second=0)
    # Next Friday 13:59:59
    # If next week is Tet, when does the next week open?
    # Next opening is either next Friday, or after Tet!
    # Let's check next opened week's Friday
    next_week_monday = current_monday + timedelta(weeks=1)
    while tet_start <= next_week_monday <= tet_end:
        next_week_monday += timedelta(weeks=1)
    next_friday = next_week_monday + timedelta(days=4)
    close_time = next_friday.replace(hour=13, minute=59, second=59)

    schedule[week_num] = {
        "open": open_time.strftime("%Y-%m-%dT%H:%M:%S"),
        "close": close_time.strftime("%Y-%m-%dT%H:%M:%S"),
        "open_str": open_time.strftime("%H:%M ngày %d/%m/%Y"),
        "close_str": close_time.strftime("%H:%M:%S ngày %d/%m/%Y")
    }
    print(f"Tuần {week_num:02d}: Mở {schedule[week_num]['open_str']} (Thứ 6) -> Chốt BXH: {schedule[week_num]['close_str']} (Thứ 6 tuần sau)")
    current_monday += timedelta(weeks=1)
    week_num += 1
