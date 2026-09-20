import React, { useState, useEffect } from "react";
import { Page, useNavigate } from "zmp-ui";
import { db } from "../services/firebase";

const SCHEDULE = {
  "1": {
    "week": 1,
    "monday": "2026-09-07",
    "open": "2026-09-11T14:00:00",
    "close": "2026-09-18T13:59:59",
    "open_str": "14:00 ngày 11/09/2026",
    "close_str": "13:59:59 ngày 18/09/2026",
    "is_cap_for_guest": false
  },
  "2": {
    "week": 2,
    "monday": "2026-09-14",
    "open": "2026-09-18T14:00:00",
    "close": "2026-09-25T13:59:59",
    "open_str": "14:00 ngày 18/09/2026",
    "close_str": "13:59:59 ngày 25/09/2026",
    "is_cap_for_guest": false
  },
  "3": {
    "week": 3,
    "monday": "2026-09-21",
    "open": "2026-09-25T14:00:00",
    "close": "2026-10-02T13:59:59",
    "open_str": "14:00 ngày 25/09/2026",
    "close_str": "13:59:59 ngày 02/10/2026",
    "is_cap_for_guest": false
  },
  "4": {
    "week": 4,
    "monday": "2026-09-28",
    "open": "2026-10-02T14:00:00",
    "close": "2026-10-09T13:59:59",
    "open_str": "14:00 ngày 02/10/2026",
    "close_str": "13:59:59 ngày 09/10/2026",
    "is_cap_for_guest": false
  },
  "5": {
    "week": 5,
    "monday": "2026-10-05",
    "open": "2026-10-09T14:00:00",
    "close": "2026-10-16T13:59:59",
    "open_str": "14:00 ngày 09/10/2026",
    "close_str": "13:59:59 ngày 16/10/2026",
    "is_cap_for_guest": false
  },
  "6": {
    "week": 6,
    "monday": "2026-10-12",
    "open": "2026-10-16T14:00:00",
    "close": "2026-10-23T13:59:59",
    "open_str": "14:00 ngày 16/10/2026",
    "close_str": "13:59:59 ngày 23/10/2026",
    "is_cap_for_guest": false
  },
  "7": {
    "week": 7,
    "monday": "2026-10-19",
    "open": "2026-10-23T14:00:00",
    "close": "2026-10-30T13:59:59",
    "open_str": "14:00 ngày 23/10/2026",
    "close_str": "13:59:59 ngày 30/10/2026",
    "is_cap_for_guest": false
  },
  "8": {
    "week": 8,
    "monday": "2026-10-26",
    "open": "2026-10-30T14:00:00",
    "close": "2026-11-06T13:59:59",
    "open_str": "14:00 ngày 30/10/2026",
    "close_str": "13:59:59 ngày 06/11/2026",
    "is_cap_for_guest": true
  },
  "9": {
    "week": 9,
    "monday": "2026-11-02",
    "open": "2026-11-06T14:00:00",
    "close": "2026-11-13T13:59:59",
    "open_str": "14:00 ngày 06/11/2026",
    "close_str": "13:59:59 ngày 13/11/2026",
    "is_cap_for_guest": false
  },
  "10": {
    "week": 10,
    "monday": "2026-11-09",
    "open": "2026-11-13T14:00:00",
    "close": "2026-11-20T13:59:59",
    "open_str": "14:00 ngày 13/11/2026",
    "close_str": "13:59:59 ngày 20/11/2026",
    "is_cap_for_guest": false
  },
  "11": {
    "week": 11,
    "monday": "2026-11-16",
    "open": "2026-11-20T14:00:00",
    "close": "2026-11-27T13:59:59",
    "open_str": "14:00 ngày 20/11/2026",
    "close_str": "13:59:59 ngày 27/11/2026",
    "is_cap_for_guest": false
  },
  "12": {
    "week": 12,
    "monday": "2026-11-23",
    "open": "2026-11-27T14:00:00",
    "close": "2026-12-04T13:59:59",
    "open_str": "14:00 ngày 27/11/2026",
    "close_str": "13:59:59 ngày 04/12/2026",
    "is_cap_for_guest": false
  },
  "13": {
    "week": 13,
    "monday": "2026-11-30",
    "open": "2026-12-04T14:00:00",
    "close": "2026-12-11T13:59:59",
    "open_str": "14:00 ngày 04/12/2026",
    "close_str": "13:59:59 ngày 11/12/2026",
    "is_cap_for_guest": false
  },
  "14": {
    "week": 14,
    "monday": "2026-12-07",
    "open": "2026-12-11T14:00:00",
    "close": "2026-12-18T13:59:59",
    "open_str": "14:00 ngày 11/12/2026",
    "close_str": "13:59:59 ngày 18/12/2026",
    "is_cap_for_guest": false
  },
  "15": {
    "week": 15,
    "monday": "2026-12-14",
    "open": "2026-12-18T14:00:00",
    "close": "2026-12-25T13:59:59",
    "open_str": "14:00 ngày 18/12/2026",
    "close_str": "13:59:59 ngày 25/12/2026",
    "is_cap_for_guest": false
  },
  "16": {
    "week": 16,
    "monday": "2026-12-21",
    "open": "2026-12-25T14:00:00",
    "close": "2027-01-01T13:59:59",
    "open_str": "14:00 ngày 25/12/2026",
    "close_str": "13:59:59 ngày 01/01/2027",
    "is_cap_for_guest": false
  },
  "17": {
    "week": 17,
    "monday": "2026-12-28",
    "open": "2027-01-01T14:00:00",
    "close": "2027-01-08T13:59:59",
    "open_str": "14:00 ngày 01/01/2027",
    "close_str": "13:59:59 ngày 08/01/2027",
    "is_cap_for_guest": false
  },
  "18": {
    "week": 18,
    "monday": "2027-01-04",
    "open": "2027-01-08T14:00:00",
    "close": "2027-01-15T13:59:59",
    "open_str": "14:00 ngày 08/01/2027",
    "close_str": "13:59:59 ngày 15/01/2027",
    "is_cap_for_guest": false
  },
  "19": {
    "week": 19,
    "monday": "2027-01-11",
    "open": "2027-01-15T14:00:00",
    "close": "2027-01-22T13:59:59",
    "open_str": "14:00 ngày 15/01/2027",
    "close_str": "13:59:59 ngày 22/01/2027",
    "is_cap_for_guest": false
  },
  "20": {
    "week": 20,
    "monday": "2027-01-18",
    "open": "2027-01-22T14:00:00",
    "close": "2027-01-29T13:59:59",
    "open_str": "14:00 ngày 22/01/2027",
    "close_str": "13:59:59 ngày 29/01/2027",
    "is_cap_for_guest": false
  },
  "21": {
    "week": 21,
    "monday": "2027-01-25",
    "open": "2027-01-29T14:00:00",
    "close": "2027-02-19T13:59:59",
    "open_str": "14:00 ngày 29/01/2027",
    "close_str": "13:59:59 ngày 19/02/2027",
    "is_cap_for_guest": false
  },
  "22": {
    "week": 22,
    "monday": "2027-02-15",
    "open": "2027-02-19T14:00:00",
    "close": "2027-02-26T13:59:59",
    "open_str": "14:00 ngày 19/02/2027",
    "close_str": "13:59:59 ngày 26/02/2027",
    "is_cap_for_guest": false
  },
  "23": {
    "week": 23,
    "monday": "2027-02-22",
    "open": "2027-02-26T14:00:00",
    "close": "2027-03-05T13:59:59",
    "open_str": "14:00 ngày 26/02/2027",
    "close_str": "13:59:59 ngày 05/03/2027",
    "is_cap_for_guest": false
  },
  "24": {
    "week": 24,
    "monday": "2027-03-01",
    "open": "2027-03-05T14:00:00",
    "close": "2027-03-12T13:59:59",
    "open_str": "14:00 ngày 05/03/2027",
    "close_str": "13:59:59 ngày 12/03/2027",
    "is_cap_for_guest": false
  },
  "25": {
    "week": 25,
    "monday": "2027-03-08",
    "open": "2027-03-12T14:00:00",
    "close": "2027-03-19T13:59:59",
    "open_str": "14:00 ngày 12/03/2027",
    "close_str": "13:59:59 ngày 19/03/2027",
    "is_cap_for_guest": false
  },
  "26": {
    "week": 26,
    "monday": "2027-03-15",
    "open": "2027-03-19T14:00:00",
    "close": "2027-03-26T13:59:59",
    "open_str": "14:00 ngày 19/03/2027",
    "close_str": "13:59:59 ngày 26/03/2027",
    "is_cap_for_guest": false
  },
  "27": {
    "week": 27,
    "monday": "2027-03-22",
    "open": "2027-03-26T14:00:00",
    "close": "2027-04-02T13:59:59",
    "open_str": "14:00 ngày 26/03/2027",
    "close_str": "13:59:59 ngày 02/04/2027",
    "is_cap_for_guest": false
  },
  "28": {
    "week": 28,
    "monday": "2027-03-29",
    "open": "2027-04-02T14:00:00",
    "close": "2027-04-09T13:59:59",
    "open_str": "14:00 ngày 02/04/2027",
    "close_str": "13:59:59 ngày 09/04/2027",
    "is_cap_for_guest": false
  },
  "29": {
    "week": 29,
    "monday": "2027-04-05",
    "open": "2027-04-09T14:00:00",
    "close": "2027-04-16T13:59:59",
    "open_str": "14:00 ngày 09/04/2027",
    "close_str": "13:59:59 ngày 16/04/2027",
    "is_cap_for_guest": false
  },
  "30": {
    "week": 30,
    "monday": "2027-04-12",
    "open": "2027-04-16T14:00:00",
    "close": "2027-04-23T13:59:59",
    "open_str": "14:00 ngày 16/04/2027",
    "close_str": "13:59:59 ngày 23/04/2027",
    "is_cap_for_guest": false
  },
  "31": {
    "week": 31,
    "monday": "2027-04-19",
    "open": "2027-04-23T14:00:00",
    "close": "2027-04-30T13:59:59",
    "open_str": "14:00 ngày 23/04/2027",
    "close_str": "13:59:59 ngày 30/04/2027",
    "is_cap_for_guest": false
  },
  "32": {
    "week": 32,
    "monday": "2027-04-26",
    "open": "2027-04-30T14:00:00",
    "close": "2027-05-07T13:59:59",
    "open_str": "14:00 ngày 30/04/2027",
    "close_str": "13:59:59 ngày 07/05/2027",
    "is_cap_for_guest": false
  },
  "33": {
    "week": 33,
    "monday": "2027-05-03",
    "open": "2027-05-07T14:00:00",
    "close": "2027-05-14T13:59:59",
    "open_str": "14:00 ngày 07/05/2027",
    "close_str": "13:59:59 ngày 14/05/2027",
    "is_cap_for_guest": false
  },
  "34": {
    "week": 34,
    "monday": "2027-05-10",
    "open": "2027-05-14T14:00:00",
    "close": "2027-05-21T13:59:59",
    "open_str": "14:00 ngày 14/05/2027",
    "close_str": "13:59:59 ngày 21/05/2027",
    "is_cap_for_guest": false
  },
  "35": {
    "week": 35,
    "monday": "2027-05-17",
    "open": "2027-05-21T14:00:00",
    "close": "2027-05-28T13:59:59",
    "open_str": "14:00 ngày 21/05/2027",
    "close_str": "13:59:59 ngày 28/05/2027",
    "is_cap_for_guest": false
  }
};

const WEEK_LANDMARKS = {
  "1": "Cột cờ Lũng Cú (Hà Giang)",
  "2": "Hẻm Tu Sản & Sông Nho Quế",
  "3": "Thác Bản Giốc (Cao Bằng)",
  "4": "Hồ Ba Bể (Bắc Kạn)",
  "5": "Ruộng bậc thang Mù Cang Chải",
  "6": "Đỉnh Fansipan (Lào Cai)",
  "7": "Thủ đô Hà Nội",
  "8": "Vịnh Hạ Long & Yên Tử",
  "9": "Tràng An & Cố đô Hoa Lư 🌟",
  "10": "Thành Nhà Hồ (Thanh Hóa)",
  "11": "Làng Sen Quê Bác (Nghệ An)",
  "12": "Ngã ba Đồng Lộc (Hà Tĩnh)",
  "13": "VQG Phong Nha - Kẻ Bàng",
  "14": "Thành cổ Quảng Trị & Hiền Lương",
  "15": "Quần thể Cố đô Huế",
  "16": "Cầu Rồng & Ngũ Hành Sơn",
  "17": "Phố cổ Hội An (Quảng Nam)",
  "18": "Đảo Lý Sơn (Quảng Ngãi) 🏆",
  "19": "Kon Tum (Bờ Y - Ngã ba Đông Dương)",
  "20": "Gia Lai (Biển Hồ Tơ Nưng)",
  "21": "Đắk Lắk (Buôn Đôn, Dray Nur)",
  "22": "Đắk Nông (Hồ Tà Đùng)",
  "23": "Phú Yên (Gành Đá Đĩa & Mũi Điện)",
  "24": "Khánh Hòa (Vịnh Nha Trang, Trầm Hương)",
  "25": "Ninh Thuận (Tháp Po Klong Garai)",
  "26": "Bình Thuận (Đồi cát Mũi Né, Bàu Trắng)",
  "27": "Lâm Đồng (Đỉnh Lang Biang, Đà Lạt) 🌟",
  "28": "TP.HCM (Địa đạo Củ Chi, Rừng Sác)",
  "29": "Tây Ninh (Núi Bà Đen)",
  "30": "TP.HCM (Bến Nhà Rồng, Landmark 81)",
  "31": "Đồng Tháp (Sa Đéc, Sen Tháp Mười)",
  "32": "Cà Mau (Đất Mũi Cà Mau)",
  "33": "Kiên Giang (Đảo Ngọc Phú Quốc)",
  "34": "Khánh Hòa (Quần đảo Trường Sa)",
  "35": "Đà Nẵng (Quần đảo Hoàng Sa) 🏆"
};

function GoldBoardPage() {
  const navigate = useNavigate();
  const [scoresData, setScoresData] = useState({});
  const [activeWeek, setActiveWeek] = useState(null);
  const [loading, setLoading] = useState(true);
  const [filterMode, setFilterMode] = useState("all"); // all, hk1, hk2
  const [lbFilterMode, setLbFilterMode] = useState("official"); // official vs all

  useEffect(() => {
    const scoresRef = db.ref('scores');
    const handleData = (snap) => {
      const data = snap.val() || {};
      setScoresData(data);
      setLoading(false);
    };

    scoresRef.on('value', handleData);
    return () => scoresRef.off('value', handleData);
  }, []);

  const formatTime = (s) => {
    if (!s || s === 9999) return "---";
    const m = Math.floor(s / 60);
    const rs = s % 60;
    return m > 0 ? `${m}m ${rs}s` : `${rs}s`;
  };

  const getWeekLeaderboard = (weekNum) => {
    const weekKey = `Tuan_${weekNum}`;
    const weekData = scoresData[weekKey] || {};
    const sched = SCHEDULE[weekNum];
    
    let entries = Object.values(weekData);

    const draftKeywords = ['test', 'abc', 'nhap', 'nháp', '123', 'demo', 'đemo', 'xxx', '...', '---', 'utc', 'bts', 'admin'];
    entries = entries.filter(s => {
      let nameValue = (s.fullName || s.name || "").trim();
      let nameLower = nameValue.toLowerCase();
      if (draftKeywords.some(k => nameLower.includes(k))) return false;
      if (/^\d+$/.test(nameLower)) return false;
      const words = nameValue.split(/\s+/).filter(w => w.length > 0);
      if (words.length < 2) return false;
      if (words.some(w => w.length > 15)) return false;
      return (s.score || 0) >= 50;
    });

    // Official window filtering (Friday 14:00 to Friday 13:59:59)
    if (lbFilterMode === "official" && sched) {
      const openMs = new Date(sched.open).getTime();
      const closeMs = new Date(sched.close).getTime();
      entries = entries.filter(s => {
        if (s.timestamp) {
          return s.timestamp >= openMs && s.timestamp <= closeMs;
        }
        return true;
      });
    }

    let filteredMap = new Map();
    entries.forEach(entry => {
      let key = ((entry.fullName || entry.name || "") + "|" + (entry.className || entry.class || "")).toLowerCase().trim();
      if (!filteredMap.has(key)) filteredMap.set(key, entry);
      else {
        let old = filteredMap.get(key);
        if (entry.score > old.score || (entry.score === old.score && (entry.duration || 999) < (old.duration || 999))) {
          filteredMap.set(key, entry);
        }
      }
    });

    return Array.from(filteredMap.values())
      .sort((a, b) => (b.score !== a.score) ? b.score - a.score : (a.duration || 999) - (b.duration || 999));
  };

  const toggleWeek = (weekNum) => {
    setActiveWeek(activeWeek === weekNum ? null : weekNum);
  };

  const weeksList = Array.from({ length: 35 }, (_, i) => 1 + i).filter(w => {
    if (filterMode === "hk1") return w <= 18;
    if (filterMode === "hk2") return w >= 19;
    return true;
  });

  return (
    <Page className="page" style={{ padding: "16px", display: "flex", flexDirection: "column", minHeight: "100vh" }}>
      <div style={{ textAlign: "center", marginBottom: "16px", borderBottom: "2px solid var(--p)", paddingBottom: "10px" }}>
        <h1 style={{ fontFamily: "'Bungee', sans-serif", color: "var(--gold)", margin: 0, fontSize: "1.5rem" }}>
          BẢNG VÀNG THÀNH TÍCH
        </h1>
        <p style={{ fontSize: "0.85rem", marginTop: "5px", color: "var(--text-sec)" }}>
          Vinh danh các nhà thám hiểm xuất sắc (Trọn bộ 35 tuần)
        </p>
      </div>

      {/* Mode Selector */}
      <div style={{ display: "flex", gap: "8px", marginBottom: "12px", justifyContent: "center" }}>
        <button 
          onClick={() => setLbFilterMode("official")}
          style={{
            flex: 1, maxWidth: "200px", padding: "6px 12px", borderRadius: "8px",
            border: "1px solid", borderColor: lbFilterMode === "official" ? "var(--p)" : "#334155",
            background: lbFilterMode === "official" ? "var(--p)" : "#1e293b",
            color: lbFilterMode === "official" ? "#000" : "#94a3b8", fontWeight: "bold", fontSize: "0.78rem", cursor: "pointer"
          }}
        >
          🏆 Đua Top Tuần (14h T6)
        </button>
        <button 
          onClick={() => setLbFilterMode("all")}
          style={{
            flex: 1, maxWidth: "200px", padding: "6px 12px", borderRadius: "8px",
            border: "1px solid", borderColor: lbFilterMode === "all" ? "var(--p)" : "#334155",
            background: lbFilterMode === "all" ? "var(--p)" : "#1e293b",
            color: lbFilterMode === "all" ? "#000" : "#94a3b8", fontWeight: "bold", fontSize: "0.78rem", cursor: "pointer"
          }}
        >
          🌟 Tất cả lượt thi
        </button>
      </div>

      {/* Filter Tabs */}
      <div style={{ display: "flex", gap: "8px", marginBottom: "16px", justifyContent: "center" }}>
        <button 
          onClick={() => setFilterMode("all")}
          style={{
            padding: "5px 12px", borderRadius: "20px", border: "1px solid var(--p)",
            background: filterMode === "all" ? "var(--p)" : "#1e293b",
            color: filterMode === "all" ? "#000" : "#fff", fontWeight: "bold", fontSize: "0.75rem", cursor: "pointer"
          }}
        >
          Tất cả (35 Tuần)
        </button>
        <button 
          onClick={() => setFilterMode("hk1")}
          style={{
            padding: "5px 12px", borderRadius: "20px", border: "1px solid var(--p)",
            background: filterMode === "hk1" ? "var(--p)" : "#1e293b",
            color: filterMode === "hk1" ? "#000" : "#fff", fontWeight: "bold", fontSize: "0.75rem", cursor: "pointer"
          }}
        >
          Học kỳ 1 (Tuần 1-18)
        </button>
        <button 
          onClick={() => setFilterMode("hk2")}
          style={{
            padding: "5px 12px", borderRadius: "20px", border: "1px solid var(--p)",
            background: filterMode === "hk2" ? "var(--p)" : "#1e293b",
            color: filterMode === "hk2" ? "#000" : "#fff", fontWeight: "bold", fontSize: "0.75rem", cursor: "pointer"
          }}
        >
          Học kỳ 2 (Tuần 19-35)
        </button>
      </div>

      {loading ? (
        <div style={{ textAlign: "center", padding: "40px", color: "var(--text-sec)" }}>Đang tải bảng vàng...</div>
      ) : (
        <div style={{ flexGrow: 1, marginBottom: "20px" }}>
          {weeksList.map((weekNum) => {
            const list = getWeekLeaderboard(weekNum);
            const sched = SCHEDULE[weekNum];
            const isOpen = activeWeek === weekNum;

            return (
              <div 
                key={weekNum} 
                style={{
                  background: "#1e293b", borderRadius: "12px", marginBottom: "10px",
                  border: "1px solid #334155", overflow: "hidden"
                }}
              >
                <div 
                  onClick={() => toggleWeek(weekNum)}
                  style={{
                    padding: "12px 16px", display: "flex", justifyContent: "space-between",
                    alignItems: "center", cursor: "pointer", background: isOpen ? "rgba(255,152,0,0.1)" : "transparent"
                  }}
                >
                  <div>
                    <span style={{ fontWeight: "bold", color: "var(--gold)", fontSize: "0.95rem" }}>
                      Tuần {weekNum}: {WEEK_LANDMARKS[weekNum]}
                    </span>
                    <div style={{ fontSize: "0.72rem", color: "#94a3b8", marginTop: "2px" }}>
                      ⏱ {sched ? sched.open_str : ""} {list.length > 0 ? `• ${list.length} em xuất sắc` : "• Chưa có bài"}
                    </div>
                  </div>
                  <span style={{ color: "var(--p)", fontSize: "1.2rem", transform: isOpen ? "rotate(180deg)" : "none", transition: "transform 0.2s" }}>
                    ▼
                  </span>
                </div>

                {isOpen && (
                  <div style={{ padding: "0 16px 16px" }}>
                    <div style={{ fontSize: "0.7rem", color: "#64748b", margin: "6px 0 10px", padding: "6px", background: "#0f172a", borderRadius: "6px" }}>
                      {lbFilterMode === "official" && sched 
                        ? `⏱ Khung đua top: ${sched.open_str} -> ${sched.close_str}`
                        : `🌟 Chế độ xem: Toàn bộ lượt thi tự luyện`}
                    </div>
                    {list.length > 0 ? (
                      <table style={{ width: "100%", borderCollapse: "collapse", fontSize: "0.85rem" }}>
                        <thead>
                          <tr style={{ borderBottom: "1px solid #334155", color: "#94a3b8", textAlign: "left" }}>
                            <th style={{ padding: "8px 4px", width: "30px" }}>#</th>
                            <th style={{ padding: "8px 4px" }}>Họ & Tên</th>
                            <th style={{ padding: "8px 4px", textAlign: "center" }}>Lớp</th>
                            <th style={{ padding: "8px 4px", textAlign: "right" }}>Điểm</th>
                            <th style={{ padding: "8px 4px", textAlign: "right" }}>Thời gian</th>
                          </tr>
                        </thead>
                        <tbody>
                          {list.map((item, idx) => (
                            <tr key={idx} style={{ borderBottom: "1px solid rgba(51,65,85,0.4)" }}>
                              <td style={{ padding: "8px 4px", color: idx < 3 ? "var(--gold)" : "#94a3b8", fontWeight: "bold" }}>
                                {idx === 0 ? "🥇" : idx === 1 ? "🥈" : idx === 2 ? "🥉" : idx + 1}
                              </td>
                              <td style={{ padding: "8px 4px", fontWeight: "600", color: "#fff" }}>
                                {item.fullName || item.name}
                              </td>
                              <td style={{ padding: "8px 4px", textAlign: "center", color: "#94a3b8" }}>
                                {item.className || item.class}
                              </td>
                              <td style={{ padding: "8px 4px", textAlign: "right", color: "var(--p)", fontWeight: "bold" }}>
                                {item.score}
                              </td>
                              <td style={{ padding: "8px 4px", textAlign: "right", color: "#2ecc71" }}>
                                {formatTime(item.duration)}
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    ) : (
                      <div style={{ textAlign: "center", padding: "15px", color: "#94a3b8", fontSize: "0.8rem" }}>
                        Chưa có dữ liệu bài nộp hợp lệ trong khung giờ này
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}

      {/* Footer Nav */}
      <div style={{ marginTop: "auto", display: "flex", gap: "10px", justifyContent: "center" }}>
        <button 
          onClick={() => navigate("/")}
          style={{
            flex: 1, padding: "12px", borderRadius: "10px", background: "var(--p)",
            color: "#fff", fontWeight: "bold", border: "none", cursor: "pointer"
          }}
        >
          🗺️ QUAY LẠI BẢN ĐỒ
        </button>
      </div>
    </Page>
  );
}

export default GoldBoardPage;
