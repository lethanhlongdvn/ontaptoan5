# -*- coding: utf-8 -*-
"""
Script đồng bộ toàn bộ 35 tuần ra data/week-{w}.json và data/week-{w}.js
Nguồn dữ liệu chuẩn: data_tuan_*.py
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
DATA_DIR = os.path.join(ROOT, "data")
TOOLS_DIR = os.path.join(ROOT, "tools")

sys.path.insert(0, TOOLS_DIR)

from data_tuan_01_06 import TUAN_01_TO_06
from data_tuan_07_12 import TUAN_07_TO_12
from data_tuan_13_18 import TUAN_13_TO_18
from data_tuan_19_24 import TUAN_19_TO_24
from data_tuan_25_30 import TUAN_25_TO_30
from data_tuan_31_35 import TUAN_31_TO_35
from schedule_data import SCHEDULE_CONFIG
from sync_all_35_html import ALL_SOUVENIRS

ALL_35_STATIONS = (
    TUAN_01_TO_06 +
    TUAN_07_TO_12 +
    TUAN_13_TO_18 +
    TUAN_19_TO_24 +
    TUAN_25_TO_30 +
    TUAN_31_TO_35
)

def parse_v3_question(item):
    raw_q = item['q']
    ans_str = item.get('ans_str', '')
    parts = re.split(r'\n(?=[A-D]\.\s*)', raw_q)
    stem = parts[0].strip()
    opts = [re.sub(r'^[A-D]\.\s*', '', p).strip() for p in parts[1:]]
    m = re.match(r'^([A-D])\.', ans_str.strip())
    c = ord(m.group(1)) - ord('A') if m else 0
    return {
        "q": stem,
        "opts": opts,
        "c": c
    }

for st in ALL_35_STATIONS:
    w = st['tuan']
    ten_tram = st['ten_tram']
    souvenirs = ALL_SOUVENIRS.get(w, st.get('souvenirs', {
        'cap1': f'Huy hiệu Trạm {w} Đồng (50đ)',
        'cap2': f'Bảo vật Trạm {w} Bạc (90đ)',
        'cap3': f'Thần bảo Trạm {w} Vàng (100đ)'
    }))
    
    sched = SCHEDULE_CONFIG.get(w, {
        "open": "2026-09-01T00:00:00",
        "open_str": "00:00 ngày 01/09/2026"
    })
    
    v1_data = [{"q": item["q"], "a": item["a"]} for item in st['v1']]
    v2_data = [{"q": item["q"], "a": item["a"]} for item in st['v2']]
    v3_data = [parse_v3_question(item) for item in st['v3']]
    
    week_payload = {
        "week": w,
        "stationName": ten_tram,
        "config": {
            "week": w,
            "openTime": sched["open"],
            "openStr": sched["open_str"]
        },
        "souvenirs": souvenirs,
        "bank": {
            "V1": v1_data,
            "V2": v2_data,
            "V3": v3_data
        }
    }
    
    # Ghi ra data/week-{w}.json
    json_path = os.path.join(DATA_DIR, f"week-{w}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(week_payload, f, ensure_ascii=False, indent=2)
        
    # Ghi ra data/week-{w}.js
    js_path = os.path.join(DATA_DIR, f"week-{w}.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(f"window.WEEK_DATA_{w} = {json.dumps(week_payload, ensure_ascii=False, indent=2)};\n")

print("Đã đồng bộ thành công toàn bộ 35 file week-{w}.json và week-{w}.js vào thư mục data!")
