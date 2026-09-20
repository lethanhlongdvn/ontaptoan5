import React, { useState, useEffect, useRef } from "react";
import { Page, useNavigate } from "zmp-ui";
import { db } from "../services/firebase";
import Bandogame from "../static/Bandogame.jpg";

export const SCHEDULE = {
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

export const STATION_NAMES = {
  1: "Cột cờ Lũng Cú (Hà Giang)",
  2: "Hẻm Tu Sản & Sông Nho Quế (Hà Giang)",
  3: "Thác Bản Giốc (Cao Bằng)",
  4: "Hồ Ba Bể (Bắc Kạn)",
  5: "Ruộng bậc thang Mù Cang Chải (Yên Bái)",
  6: "Đỉnh Fansipan (Lào Cai)",
  7: "Thủ đô Hà Nội",
  8: "Vịnh Hạ Long & Yên Tử (Quảng Ninh)",
  9: "Tràng An & Cố đô Hoa Lư (Ninh Bình) 🌟 GK1",
  10: "Thành Nhà Hồ (Thanh Hóa)",
  11: "Làng Sen Quê Bác (Nghệ An)",
  12: "Ngã ba Đồng Lộc (Hà Tĩnh)",
  13: "VQG Phong Nha - Kẻ Bàng (Quảng Bình)",
  14: "Thành cổ Quảng Trị, Cầu Hiền Lương & Sông Bến Hải",
  15: "Quần thể Di tích Cố đô Huế (Thừa Thiên Huế)",
  16: "Cầu Rồng & Ngũ Hành Sơn (Đà Nẵng)",
  17: "Phố cổ Hội An (Quảng Nam)",
  18: "Đảo Lý Sơn (Quảng Ngãi) 🏆 CK1",
  19: "Kon Tum (Bờ Y - Ngã ba Đông Dương)",
  20: "Gia Lai (Biển Hồ Tơ Nưng)",
  21: "Đắk Lắk (Buôn Đôn, Thác Dray Nur)",
  22: "Đắk Nông (Hồ Tà Đùng)",
  23: "Phú Yên (Gành Đá Đĩa & Mũi Điện)",
  24: "Khánh Hòa (Vịnh Nha Trang, Tháp Trầm Hương)",
  25: "Ninh Thuận (Tháp Po Klong Garai)",
  26: "Bình Thuận (Đồi cát Mũi Né, Bàu Trắng)",
  27: "Lâm Đồng (Đỉnh Lang Biang, Đà Lạt) 🌟 GK2",
  28: "TP. Hồ Chí Minh (Địa đạo Củ Chi, Rừng Sác)",
  29: "Tây Ninh (Núi Bà Đen)",
  30: "TP. Hồ Chí Minh (Bến Nhà Rồng, Landmark 81)",
  31: "Đồng Tháp (Sa Đéc, Tràm Chim, Sen Tháp Mười)",
  32: "Cà Mau (Đất Mũi Cà Mau)",
  33: "Kiên Giang (Đảo Ngọc Phú Quốc)",
  34: "Khánh Hòa (Quần đảo Trường Sa thiêng liêng)",
};

function getCurrentSchoolWeek() {
  const now = Date.now();
  for (let w = 1; w <= 35; w++) {
    const sched = SCHEDULE[w];
    if (sched) {
      const openTime = new Date(sched.open).getTime();
      const closeTime = new Date(sched.close).getTime();
      if (now >= openTime && now <= closeTime) {
        return w;
      }
    }
  }
  const w1 = SCHEDULE[1];
  if (w1 && now < new Date(w1.open).getTime()) return 1;
  const w35 = SCHEDULE[35];
  if (w35 && now > new Date(w35.close).getTime()) return 35;
  let latest = 1;
  for (let w = 1; w <= 35; w++) {
    const sched = SCHEDULE[w];
    if (sched && now >= new Date(sched.open).getTime()) {
      latest = w;
    }
  }
  return latest;
}

function HomePage() {
  const navigate = useNavigate();
  const [selectedWeek, setSelectedWeek] = useState(getCurrentSchoolWeek);
  const [lbFilterMode, setLbFilterMode] = useState("official"); // official vs all
  const [studentUsername, setStudentUsername] = useState(localStorage.getItem("studentUsername") || "");
  const [studentName, setStudentName] = useState(localStorage.getItem("studentName") || "");
  const [studentClass, setStudentClass] = useState(localStorage.getItem("studentClass") || "");
  const [studentSchool, setStudentSchool] = useState(localStorage.getItem("studentSchool") || "");
  const [userRole, setUserRole] = useState(localStorage.getItem("userRole") || "guest");
  const [userStatus, setUserStatus] = useState(localStorage.getItem("userStatus") || "pending");
  const [highScore, setHighScore] = useState(0);
  const [leaderboard, setLeaderboard] = useState([]);
  
  // Registration Form State
  const [showAuth, setShowAuth] = useState(false);
  const [authMode, setAuthMode] = useState("login"); // login or register
  const [inputUsername, setInputUsername] = useState("");
  const [inputPassword, setInputPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [inputName, setInputName] = useState("");
  const [inputClass, setInputClass] = useState("");
  const [inputSchoolSelect, setInputSchoolSelect] = useState("");
  const [inputSchoolManual, setInputSchoolManual] = useState("");
  const [inputRole, setInputRole] = useState("student");
  
  // Countdown State
  const [countdownEndTime, setCountdownEndTime] = useState(null);
  const [countdownStation, setCountdownStation] = useState(1);
  const [timeLeft, setTimeLeft] = useState("");
  const timerRef = useRef(null);

  // SVG paths
  const [paths, setPaths] = useState([]);
  const mapImgRef = useRef(null);

  const isApprovedTeacherOrAdmin = (userRole === "teacher" || userRole === "admin") && (userStatus === "approved");

  useEffect(() => {
    const sched = SCHEDULE[selectedWeek];
    const scoresRef = db.ref(`scores/Tuan_${selectedWeek}`);
    const handleData = (snap) => {
      const data = snap.val();
      if (!data) {
        setLeaderboard([]);
        setHighScore(0);
        return;
      }
      let all = [];
      for (let id in data) all.push(data[id]);

      const draftKeywords = ['test', 'abc', 'nhap', 'nháp', '123', 'demo', 'đemo', 'xxx', '...', '---', 'utc', 'bts', 'admin'];
      all = all.filter(s => {
        let nameValue = (s.fullName || s.name || "").trim();
        let nameLower = nameValue.toLowerCase();
        if (draftKeywords.some(k => nameLower.includes(k))) return false;
        if (/^\d+$/.test(nameLower)) return false;
        const words = nameValue.split(/\s+/).filter(w => w.length > 0);
        if (words.length < 2) return false;
        if (words.some(w => w.length > 15)) return false;
        return true;
      });

      // Filter by weekly official competition window
      if (lbFilterMode === "official" && sched) {
        const openMs = new Date(sched.open).getTime();
        const closeMs = new Date(sched.close).getTime();
        all = all.filter(s => {
          if (s.timestamp) {
            return s.timestamp >= openMs && s.timestamp <= closeMs;
          }
          return true;
        });
      }

      all.sort((a, b) => (b.score !== a.score) ? b.score - a.score : (a.duration || 999) - (b.duration || 999));
      
      const top10 = [];
      const seen = new Set();
      for (let s of all) {
        let key = ((s.fullName || s.name) + (s.className || s.class)).toLowerCase();
        if (!seen.has(key)) {
          top10.push(s);
          seen.add(key);
        }
        if (top10.length >= 10) break;
      }

      setLeaderboard(top10);
      if (top10.length > 0) {
        setHighScore(top10[0].score);
      } else {
        setHighScore(0);
      }
    };

    scoresRef.on('value', handleData);
    return () => scoresRef.off('value', handleData);
  }, [selectedWeek, lbFilterMode]);

  // Update SVG paths
  const drawPaths = () => {
    const newPaths = [];
    const now = new Date();
    
    for (let i = 1; i < 35; i++) {
      const startEl = document.getElementById(`st-${i}`);
      const endEl = document.getElementById(`st-${i + 1}`);
      const schedNext = SCHEDULE[i + 1];
      const openTimeNext = schedNext ? new Date(schedNext.open) : new Date(0);

      const isOpen = isApprovedTeacherOrAdmin || (now >= openTimeNext);

      if (startEl && endEl && isOpen) {
        const x1 = startEl.offsetLeft + startEl.offsetWidth / 2;
        const y1 = startEl.offsetTop + startEl.offsetHeight / 2;
        const x2 = endEl.offsetLeft + endEl.offsetWidth / 2;
        const y2 = endEl.offsetTop + endEl.offsetHeight / 2;
        
        const isSea = (i === 17 || i === 18 || i === 32 || i === 33 || i === 34);
        newPaths.push({
          id: i,
          x1,
          y1,
          x2,
          y2,
          className: isSea ? "sea-line" : "road-line"
        });
      }
    }
    setPaths(newPaths);
  };

  useEffect(() => {
    window.addEventListener("resize", drawPaths);
    return () => window.removeEventListener("resize", drawPaths);
  }, [isApprovedTeacherOrAdmin]);

  const handleImageLoad = () => {
    setTimeout(drawPaths, 300);
  };

  // Timer Countdown logic
  useEffect(() => {
    if (countdownEndTime) {
      if (timerRef.current) clearInterval(timerRef.current);
      
      const updateTimer = () => {
        const dist = countdownEndTime - new Date();
        if (dist < 0) {
          clearInterval(timerRef.current);
          setCountdownEndTime(null);
          window.location.reload();
          return;
        }
        const d = Math.floor(dist / 86400000);
        const h = Math.floor((dist % 86400000) / 3600000);
        const m = Math.floor((dist % 3600000) / 60000);
        const s = Math.floor((dist % 60000) / 1000);
        setTimeLeft(`${d}n ${h}:${m}:${s}`);
      };
      
      updateTimer();
      timerRef.current = setInterval(updateTimer, 1000);
    }
    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [countdownEndTime]);

  const handleStageClick = (no) => {
    // 1. Check guest / unapproved cap (<= 8)
    if (no > 8) {
      if (!studentUsername) {
        alert(`🔒 YÊU CẦU ĐĂNG KÝ TÀI KHOẢN\n\nTrạm ${no} thuộc hệ thống thử thách nâng cao.\nKhách chỉ được trải nghiệm tự do từ Trạm 1 đến Trạm 8.\nEm vui lòng Đăng ký hoặc Đăng nhập nhé!`);
        setShowAuth(true);
        return;
      }
      if (userStatus !== "approved") {
        alert(`⏳ TÀI KHOẢN CHỜ PHÊ DUYỆT\n\nTài khoản @${studentUsername} đang ở trạng thái Chờ phê duyệt.\nTrong thời gian này, bạn có thể luyện tập từ Trạm 1 đến 8.\nVui lòng liên hệ Thầy/Cô quản trị viên để được duyệt!`);
        return;
      }
    }

    // 2. Approved Teacher & Admin bypass
    if (isApprovedTeacherOrAdmin) {
      window.location.href = `./${no}.html`;
      return;
    }

    // 3. Check schedule
    const now = new Date();
    const sched = SCHEDULE[no];
    const openTime = sched ? new Date(sched.open) : new Date(0);
    if (now < openTime) {
      setCountdownStation(no);
      setCountdownEndTime(openTime);
      return;
    }

    window.location.href = `./${no}.html`;
  };

  const handleAuthAction = () => {
    if (studentName) {
      if (confirm(`Đăng xuất tài khoản @${studentUsername || studentName}?`)) {
        localStorage.clear();
        setStudentUsername("");
        setStudentName("");
        setStudentClass("");
        setStudentSchool("");
        setUserRole("guest");
        setUserStatus("pending");
        window.location.reload();
      }
    } else {
      setShowAuth(true);
      setAuthMode("login");
    }
  };

  const handleLogin = () => {
    const u = inputUsername.trim().toLowerCase();
    const p = inputPassword.trim();
    if (!u) { alert("Vui lòng nhập Tên đăng nhập!"); return; }
    if (!p) { alert("Vui lòng nhập Mật khẩu!"); return; }

    db.ref("users/" + u).once("value", (snap) => {
      let user = snap.val();
      if (!user && u === "admin") {
        user = {
          username: "admin",
          password: "EduBot@2026",
          fullName: "Quản Trị Viên Hệ Thống",
          className: "Ban Quản Trị",
          schoolName: "EduRobot",
          role: "admin",
          status: "approved",
          createdAt: Date.now()
        };
        db.ref("users/admin").set(user);
      }
      if (user) {
        if (user.password && user.password !== p) {
          alert("Mật khẩu không chính xác!");
          return;
        }
        if (user.status === "blocked") {
          alert("⚠️ Tài khoản đã bị khóa!");
          return;
        }
        localStorage.setItem("studentUsername", user.username || u);
        localStorage.setItem("studentName", user.fullName);
        localStorage.setItem("studentClass", user.className || "");
        localStorage.setItem("studentSchool", user.schoolName || "");
        localStorage.setItem("userRole", user.role || "student");
        localStorage.setItem("userStatus", user.status || "pending");
        if (user.role === "admin") {
          localStorage.setItem("adminUsername", user.username || u);
        }

        setStudentUsername(user.username || u);
        setStudentName(user.fullName);
        setStudentClass(user.className || "");
        setStudentSchool(user.schoolName || "");
        setUserRole(user.role || "student");
        setUserStatus(user.status || "pending");
        setShowAuth(false);
        alert(`🎉 Chào mừng ${user.fullName}!`);
      } else {
        alert("Tài khoản chưa tồn tại! Hãy chuyển sang tab Đăng ký nhé.");
      }
    });
  };

  const handleRegister = () => {
    const u = inputUsername.trim().toLowerCase();
    const p = inputPassword.trim();
    const n = inputName.trim();
    const c = inputClass;
    let s = inputSchoolSelect === "other" ? inputSchoolManual.trim() : inputSchoolSelect;

    if (!u || u.length < 3) { alert("Tên đăng nhập từ 3 ký tự trở lên!"); return; }
    if (!p || p.length < 4) { alert("Mật khẩu ít nhất 4 ký tự!"); return; }
    if (!n || n.split(/\s+/).length < 2) { alert("Vui lòng nhập đầy đủ Họ và Tên (ít nhất 2 từ)!"); return; }
    if (!c) { alert("Vui lòng chọn Lớp!"); return; }
    if (!s) { alert("Vui lòng chọn hoặc nhập tên Trường!"); return; }

    db.ref("users/" + u).once("value", (snap) => {
      if (snap.exists()) {
        alert(`⚠️ Tên đăng nhập "${u}" đã tồn tại!`);
        return;
      }
      const userData = {
        username: u,
        password: p,
        fullName: n,
        className: c,
        schoolName: s,
        role: inputRole,
        status: (u === "admin") ? "approved" : "pending",
        createdAt: db.constructor.ServerValue ? db.constructor.ServerValue.TIMESTAMP : Date.now()
      };

      db.ref("users/" + u).set(userData, (err) => {
        if (err) { alert("Lỗi khi lưu tài khoản!"); return; }
        localStorage.setItem("studentUsername", u);
        localStorage.setItem("studentName", n);
        localStorage.setItem("studentClass", c);
        localStorage.setItem("studentSchool", s);
        localStorage.setItem("userRole", inputRole);
        localStorage.setItem("userStatus", userData.status);

        setStudentUsername(u);
        setStudentName(n);
        setStudentClass(c);
        setStudentSchool(s);
        setUserRole(inputRole);
        setUserStatus(userData.status);
        setShowAuth(false);
        alert(`✨ Đăng ký thành công! Tài khoản đang chờ phê duyệt. Bạn có thể luyện tập từ Trạm 1 đến 8.`);
      });
    });
  };

  const formatTime = (sec) => {
    if (!sec) return "00:00";
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  const now = new Date();

  return (
    <Page className="page">
      {/* Welcome Banner */}
      <div className="welcome-banner">
        <h1 className="welcome-text">THÁM HIỂM VIỆT NAM CÙNG ROBOT</h1>
      </div>

      {/* Game Header */}
      <header className="game-header">
        <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
          <div style={{
            width: "36px", height: "36px", borderRadius: "50%",
            background: "linear-gradient(135deg, var(--gold), #f59e0b)",
            display: "flex", alignItems: "center", justifyContent: "center",
            color: "#000", fontWeight: "800"
          }}>
            R
          </div>
          <div style={{ display: "flex", flexDirection: "column", justifyContent: "center", lineHeight: "1.3" }}>
            {studentName ? (
              <>
                <div style={{ display: "flex", alignItems: "center", gap: "5px" }}>
                  <span style={{ fontSize: "0.95rem", fontWeight: "bold", color: "var(--gold)" }}>{studentName}</span>
                  {userRole === "teacher" ? (
                    <span style={{ fontSize: "0.65rem", padding: "1px 5px", borderRadius: "8px", background: "rgba(0,242,255,0.2)", color: "#00f2ff", border: "1px solid #00f2ff" }}>
                      {userStatus === "approved" ? "🎓 GV" : "🎓 GV (Chờ)"}
                    </span>
                  ) : (
                    <span style={{ fontSize: "0.65rem", padding: "1px 5px", borderRadius: "8px", background: userStatus === "approved" ? "rgba(46,204,113,0.2)" : "rgba(255,152,0,0.2)", color: userStatus === "approved" ? "#2ecc71" : "#ff9800", border: "1px solid currentColor" }}>
                      {userStatus === "approved" ? "⭐ Đã duyệt" : "⏳ Chờ duyệt"}
                    </span>
                  )}
                </div>
                <span style={{ fontSize: "0.75rem", color: "var(--text-sec)" }}>{studentClass} • @{studentUsername}</span>
                <span style={{ fontSize: "0.65rem", color: "#94a3b8" }}>{studentSchool}</span>
              </>
            ) : (
              <>
                <span style={{ fontSize: "0.95rem", fontWeight: "bold", color: "var(--gold)" }}>Khách</span>
                <span style={{ fontSize: "0.75rem", color: "var(--text-sec)" }}>Tự luyện Trạm 1-8</span>
              </>
            )}
          </div>
        </div>
        <div style={{ textAlign: "right" }}>
          <span style={{ fontSize: "0.65rem", color: "var(--text-sec)", display: "block" }}>KỶ LỤC TUẦN</span>
          <span style={{ fontSize: "1.2rem", color: "var(--p)", fontWeight: "bold" }}>{highScore}</span>
        </div>
      </header>

      {/* Main Content */}
      <main className="game-content-wrapper">
        <div className="map-container">
          <div className="map-relative-box" id="map-box">
            <img 
              src={Bandogame} 
              alt="Bản đồ" 
              className="map-image" 
              ref={mapImgRef}
              onLoad={handleImageLoad}
            />

            {/* Landmarks */}
            <div className="landmark" id="lm-lungcu">Lũng Cú</div>
            <div className="landmark" id="lm-hanoi">Thủ đô Hà Nội</div>
            <div className="landmark" id="lm-hue">Cố đô Huế</div>
            <div className="landmark" id="lm-tphcm">TP. Hồ Chí Minh</div>
            <div className="landmark" id="lm-camau">Mũi Cà Mau</div>

            {/* Path SVG */}
            <svg id="path-svg">
              {paths.map(path => (
                <line 
                  key={path.id}
                  x1={path.x1} 
                  y1={path.y1} 
                  x2={path.x2} 
                  y2={path.y2} 
                  className={path.className}
                />
              ))}
            </svg>

            {/* Stations */}
            {Array.from({ length: 35 }, (_, i) => 1 + i).map(num => {
              const sched = SCHEDULE[num];
              const stName = STATION_NAMES[num] || `Trạm ${num}`;
              const openTime = sched ? new Date(sched.open) : new Date(0);
              const isLocked = !isApprovedTeacherOrAdmin && (now < openTime || (num > 8 && userStatus !== "approved"));
              let lockStatus = "";
              if (isApprovedTeacherOrAdmin) {
                lockStatus = " • [Quyền Giáo viên: Mở toàn bộ 35 tuần]";
              } else if (num > 8 && userStatus !== "approved") {
                lockStatus = " • [Chỉ dành cho tài khoản đã phê duyệt]";
              } else if (now < openTime) {
                lockStatus = ` • [Chưa mở: Mở lúc ${sched ? sched.open_str : '14:00 Thứ Sáu'}]`;
              }
              return (
                <div 
                  key={num}
                  id={`st-${num}`} 
                  className={`station ${isLocked ? 'locked' : ''}`}
                  onClick={() => handleStageClick(num)}
                >
                  {num}
                  <span className="station-tooltip">
                    <div>Trạm {num}: {stName}</div>
                    {isLocked && !isApprovedTeacherOrAdmin && (
                      <div style={{ fontSize: "0.7rem", color: num > 8 && userStatus !== "approved" ? "#f59e0b" : "#94a3b8", fontWeight: "normal", marginTop: "2px" }}>
                        {num > 8 && userStatus !== "approved" ? "🔒 Cần tài khoản duyệt" : `⏳ Mở: ${sched ? sched.open_str : ''}`}
                      </div>
                    )}
                  </span>
                </div>
              );
            })}
          </div>
        </div>

        {/* Leaderboard */}
        <section className="leaderboard-sidebar">
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "8px" }}>
            <h3 className="leaderboard-title" style={{ margin: 0 }}>🏆 TOP 10 TUẦN {selectedWeek}</h3>
            <select 
              value={selectedWeek} 
              onChange={(e) => setSelectedWeek(Number(e.target.value))}
              style={{ background: "#0f172a", color: "var(--gold)", border: "1px solid var(--p)", borderRadius: "6px", padding: "4px 8px", fontSize: "0.8rem", fontWeight: "bold" }}
            >
              {Array.from({ length: 35 }, (_, i) => 1 + i).map(w => (
                <option key={w} value={w}>Tuần {w}</option>
              ))}
            </select>
          </div>

          <div style={{ display: "flex", gap: "6px", marginBottom: "10px" }}>
            <button
              onClick={() => setLbFilterMode("official")}
              style={{
                flex: 1, padding: "5px", fontSize: "0.72rem", fontWeight: "bold", borderRadius: "6px", cursor: "pointer",
                background: lbFilterMode === "official" ? "var(--p)" : "#0f172a",
                color: lbFilterMode === "official" ? "#000" : "#94a3b8",
                border: "1px solid", borderColor: lbFilterMode === "official" ? "var(--p)" : "#334155"
              }}
            >
              🏆 Đua Top Tuần
            </button>
            <button
              onClick={() => setLbFilterMode("all")}
              style={{
                flex: 1, padding: "5px", fontSize: "0.72rem", fontWeight: "bold", borderRadius: "6px", cursor: "pointer",
                background: lbFilterMode === "all" ? "var(--p)" : "#0f172a",
                color: lbFilterMode === "all" ? "#000" : "#94a3b8",
                border: "1px solid", borderColor: lbFilterMode === "all" ? "var(--p)" : "#334155"
              }}
            >
              🌟 Tất cả lượt thi
            </button>
          </div>

          <div style={{ fontSize: "0.68rem", color: "#64748b", marginBottom: "8px" }}>
            {lbFilterMode === "official" && SCHEDULE[selectedWeek] 
              ? `⏱ Khung đua top: ${SCHEDULE[selectedWeek].open_str} -> ${SCHEDULE[selectedWeek].close_str}`
              : `🌟 Chế độ xem: Toàn bộ lịch sử điểm số`}
          </div>

          <table>
            <thead>
              <tr>
                <th>#</th>
                <th style={{ textAlign: "left" }}>Thí sinh</th>
                <th>Điểm</th>
                <th>Thời gian</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.length > 0 ? (
                leaderboard.map((s, i) => (
                  <tr key={i}>
                    <td>{i + 1}</td>
                    <td style={{ textAlign: "left" }}>
                      <span style={{ display: "block", fontWeight: "bold", color: "#fff" }}>{s.fullName || s.name}</span>
                      <span style={{ display: "block", fontSize: "0.75rem", color: "#94a3b8", marginTop: "2px" }}>{s.className || s.class}</span>
                      <span style={{ display: "block", fontSize: "0.65rem", color: "#64748b", marginTop: "2px" }}>{s.schoolName || '---'}</span>
                    </td>
                    <td style={{ color: "var(--p)", fontWeight: "bold" }}>{s.score}</td>
                    <td style={{ color: "#2ecc71" }}>{formatTime(s.duration)}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="4" style={{ color: "#94a3b8", padding: "12px" }}>Chưa có dữ liệu</td>
                </tr>
              )}
            </tbody>
          </table>
        </section>
      </main>

      {/* Footer */}
      <footer className="game-footer">
        <div className="footer-buttons">
          <button className="btn-nav" onClick={() => navigate("/bag")}>🎒 TÚI ĐỒ</button>
          <button className="btn-nav" onClick={() => navigate("/gold-board")} style={{ color: "var(--gold)", borderColor: "var(--gold)" }}>🏆 BẢNG VÀNG</button>
          <button className="btn-nav btn-share" onClick={() => {
            navigator.clipboard.writeText(window.location.href);
            alert("Đã sao chép link chia sẻ!");
          }}>📤 CHIA SẺ</button>
          {isApprovedTeacherOrAdmin && (
            <button className="btn-nav" onClick={() => window.location.href = "admin.html"} style={{ background: "#e11d48", borderColor: "#e11d48", color: "#fff", fontWeight: "bold" }}>
              🛡️ PHÊ DUYỆT
            </button>
          )}
          <button className="btn-nav" onClick={handleAuthAction} style={studentName ? { color: "#ff5252", borderColor: "#ff5252" } : {}}>
            {studentName ? "⚙️ ĐĂNG XUẤT" : "🚀 ĐĂNG NHẬP"}
          </button>
        </div>
        <div className="copyright-box">
          <p className="copyright-text">@Học toán 5 cùng RoBot - Phát triển bởi: <b>LÊ THÀNH LONG</b></p>
        </div>
      </footer>

      {/* Auth Overlay */}
      {showAuth && (
        <div id="auth-overlay" style={{ display: "flex" }}>
          <div className="auth-card" style={{ maxWidth: "380px" }}>
            <div style={{ display: "flex", justifyContent: "center", gap: "10px", marginBottom: "15px" }}>
              <button 
                onClick={() => setAuthMode("login")}
                style={{
                  padding: "6px 16px", borderRadius: "8px", fontWeight: "bold", fontSize: "0.85rem", cursor: "pointer",
                  background: authMode === "login" ? "var(--p)" : "transparent",
                  color: authMode === "login" ? "#000" : "#94a3b8",
                  border: "1px solid", borderColor: authMode === "login" ? "var(--p)" : "#334155"
                }}
              >
                ĐĂNG NHẬP
              </button>
              <button 
                onClick={() => setAuthMode("register")}
                style={{
                  padding: "6px 16px", borderRadius: "8px", fontWeight: "bold", fontSize: "0.85rem", cursor: "pointer",
                  background: authMode === "register" ? "var(--p)" : "transparent",
                  color: authMode === "register" ? "#000" : "#94a3b8",
                  border: "1px solid", borderColor: authMode === "register" ? "var(--p)" : "#334155"
                }}
              >
                ĐĂNG KÝ
              </button>
            </div>

            <label style={{ display: "block", textAlign: "left", color: "#94a3b8", fontSize: "0.8rem" }}>Tên đăng nhập:</label>
            <input 
              type="text" 
              placeholder="viết liền không dấu..." 
              value={inputUsername}
              onChange={e => setInputUsername(e.target.value)}
            />

            <label style={{ display: "block", textAlign: "left", color: "#94a3b8", fontSize: "0.8rem", marginTop: "8px" }}>Mật khẩu:</label>
            <div style={{ position: "relative", width: "100%" }}>
              <input 
                type={showPassword ? "text" : "password"} 
                placeholder="nhập mật khẩu..." 
                value={inputPassword}
                onChange={e => setInputPassword(e.target.value)}
                style={{ paddingRight: "40px", boxSizing: "border-box" }}
              />
              <span 
                onClick={() => setShowPassword(!showPassword)}
                style={{
                  position: "absolute",
                  right: "10px",
                  top: "50%",
                  transform: "translateY(-50%)",
                  cursor: "pointer",
                  fontSize: "1.15rem",
                  userSelect: "none"
                }}
                title={showPassword ? "Ẩn mật khẩu" : "Hiện mật khẩu"}
              >
                {showPassword ? "🙈" : "👁️"}
              </span>
            </div>

            {authMode === "register" && (
              <>
                <label style={{ display: "block", textAlign: "left", color: "#94a3b8", fontSize: "0.8rem", marginTop: "8px" }}>Vai trò:</label>
                <div style={{ display: "flex", gap: "15px", margin: "6px 0 10px" }}>
                  <label style={{ color: "#fff", fontSize: "0.85rem", display: "flex", alignItems: "center", gap: "4px" }}>
                    <input type="radio" name="zmp-role" value="student" checked={inputRole === "student"} onChange={() => setInputRole("student")} /> Học sinh
                  </label>
                  <label style={{ color: "#fff", fontSize: "0.85rem", display: "flex", alignItems: "center", gap: "4px" }}>
                    <input type="radio" name="zmp-role" value="teacher" checked={inputRole === "teacher"} onChange={() => setInputRole("teacher")} /> Giáo viên
                  </label>
                </div>

                <label style={{ display: "block", textAlign: "left", color: "#94a3b8", fontSize: "0.8rem" }}>Họ và Tên thật:</label>
                <input 
                  type="text" 
                  placeholder="Ví dụ: Nguyễn Văn A" 
                  value={inputName}
                  onChange={e => setInputName(e.target.value)}
                />

                <label style={{ display: "block", textAlign: "left", color: "#94a3b8", fontSize: "0.8rem", marginTop: "8px" }}>Chọn Lớp:</label>
                <select 
                  value={inputClass}
                  onChange={e => setInputClass(e.target.value)}
                  style={{
                    width: "100%", padding: "10px", margin: "4px 0", borderRadius: "8px", 
                    border: "1.5px solid #334155", background: "#0f172a", color: "white"
                  }}
                >
                  <option value="" disabled>-- Chọn lớp --</option>
                  <option value="5/1">5/1</option>
                  <option value="5/2">5/2</option>
                  <option value="5/3">5/3</option>
                  <option value="5/4">5/4</option>
                  <option value="5/5">5/5</option>
                </select>

                <label style={{ display: "block", textAlign: "left", color: "#94a3b8", fontSize: "0.8rem", marginTop: "8px" }}>Chọn Trường:</label>
                <select 
                  value={inputSchoolSelect}
                  onChange={e => setInputSchoolSelect(e.target.value)}
                  style={{
                    width: "100%", padding: "10px", margin: "4px 0", borderRadius: "8px", 
                    border: "1.5px solid #334155", background: "#0f172a", color: "white"
                  }}
                >
                  <option value="" disabled>-- Chọn trường --</option>
                  <option value="Tiểu học Đỗ Văn Nại">Tiểu học Đỗ Văn Nại</option>
                  <option value="Tiểu học Nhị Long">Tiểu học Nhị Long</option>
                  <option value="other">Trường khác...</option>
                </select>

                {inputSchoolSelect === "other" && (
                  <input 
                    type="text" 
                    placeholder="Nhập tên trường của bạn..." 
                    value={inputSchoolManual}
                    onChange={e => setInputSchoolManual(e.target.value)}
                    style={{ marginTop: "4px" }}
                  />
                )}
              </>
            )}

            <div style={{ display: "flex", gap: "10px", marginTop: "15px" }}>
              <button 
                onClick={authMode === "login" ? handleLogin : handleRegister}
                style={{
                  flex: 1, background: "var(--p)", color: "white", padding: "10px", 
                  borderRadius: "8px", border: "none", fontWeight: "700", cursor: "pointer", fontSize: "0.95rem"
                }}
              >
                {authMode === "login" ? "ĐĂNG NHẬP" : "ĐĂNG KÝ"}
              </button>
              <button 
                onClick={() => setShowAuth(false)}
                style={{
                  background: "#0f172a", color: "#94a3b8", padding: "10px 16px", 
                  borderRadius: "8px", border: "1px solid #334155", cursor: "pointer", fontSize: "0.85rem"
                }}
              >
                ĐÓNG
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Countdown Overlay */}
      {countdownEndTime && (
        <div id="countdown-overlay" style={{ display: "flex" }}>
          <div className="notice-box">
            <h2 style={{ fontFamily: "'Bungee', sans-serif", color: "var(--gold)" }}>TRẠM {countdownStation} CHƯA MỞ</h2>
            <p style={{ color: "#94a3b8", fontSize: "0.85rem" }}>
              Thời gian mở: <b>{SCHEDULE[countdownStation] ? SCHEDULE[countdownStation].open_str : ""}</b>
            </p>
            <div className="timer-box">{timeLeft}</div>
            <button 
              className="btn-nav" 
              onClick={() => setCountdownEndTime(null)} 
              style={{ width: "100%", borderColor: "#94a3b8", color: "#fff", marginTop: "10px" }}
            >
              ĐÃ HIỂU
            </button>
          </div>
        </div>
      )}
    </Page>
  );
}

export default HomePage;
