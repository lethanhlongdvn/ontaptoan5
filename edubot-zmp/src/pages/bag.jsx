import React, { useState, useEffect } from "react";
import { Page, useNavigate } from "zmp-ui";
import { db } from "../services/firebase";

const ITEMS_DATA = {
  "1": {
    "name": "Hà Giang - Cột cờ Lũng Cú",
    "icon": "🚩",
    "cap1": "Huy hiệu Cột cờ Lũng Cú Đồng",
    "cap2": "Kính viễn vọng Cực Bắc Bạc",
    "cap3": "Ngọn cờ Thần Phong Hoàng Kim Vàng"
  },
  "2": {
    "name": "Hà Giang - Tu Sản & Nho Quế",
    "icon": "🛶",
    "cap1": "Mảnh ngọc lục bảo Nho Quế Đồng",
    "cap2": "Cung tên Hẻm núi Bạc",
    "cap3": "Song kiếm Tu Sản Long Phụng Vàng"
  },
  "3": {
    "name": "Cao Bằng - Thác Bản Giốc",
    "icon": "🌊",
    "cap1": "Thạch nhũ Bản Giốc Khởi Nguyên Đồng",
    "cap2": "Khiên chắn Thác Bạc Hùng Vĩ",
    "cap3": "Băng Thần Phù Thác Bản Giốc Vàng"
  },
  "4": {
    "name": "Bắc Kạn - Hồ Ba Bể",
    "icon": "⛵",
    "cap1": "Mảnh gỗ Thuyền độc mộc Đồng",
    "cap2": "Ngọc bội Hồ Xanh Bạch Ngân Bạc",
    "cap3": "Minh châu Ba Bể Tỏa Sáng Vàng"
  },
  "5": {
    "name": "Yên Bái - Mù Cang Chải",
    "icon": "🌾",
    "cap1": "Bông lúa nếp nương Đồng Vàng",
    "cap2": "Liềm gặt Mùa Vàng Bạc Ánh",
    "cap3": "Vương miện Sóng Vàng Mù Cang Chải Vàng"
  },
  "6": {
    "name": "Lào Cai - Đỉnh Fansipan",
    "icon": "🏔️",
    "cap1": "Khối đá hoa cương Tây Bắc Đồng",
    "cap2": "La bàn Đỉnh Mây Bạc Tuyết",
    "cap3": "Cây gậy Fansipan Hoàng Kim Vàng"
  },
  "7": {
    "name": "Hà Nội - Hồ Gươm & Cột cờ",
    "icon": "🐢",
    "cap1": "Mảnh Rùa Vàng Thăng Long Đồng",
    "cap2": "Tháp Bút Trí Tuệ Bạc Trắng",
    "cap3": "Thần kiếm Thuận Thiên Hoàng Kim Vàng"
  },
  "8": {
    "name": "Quảng Ninh - Hạ Long & Yên Tử",
    "icon": "🐉",
    "cap1": "Vỏ sò Vịnh Rồng Biển Đông Đồng",
    "cap2": "Chuông đồng Yên Tử Mạ Bạc",
    "cap3": "Trúc Lâm Ngọc Tỷ Long Châu Vàng"
  },
  "9": {
    "name": "Ninh Bình - Tràng An & Hoa Lư",
    "icon": "🏛️",
    "cap1": "Phiến đá Hoa Lư Cố Đô Đồng",
    "cap2": "Ngọc bội Tràng An Tinh Khiết Bạc",
    "cap3": "Ấn Hoàng Đế Đinh Tiên Hoàng Vàng"
  },
  "10": {
    "name": "Thanh Hóa - Thành Nhà Hồ",
    "icon": "🧱",
    "cap1": "Viên gạch cổ Tây Đô Đồng",
    "cap2": "Búa thần Đẽo Đá Bạch Kim Bạc",
    "cap3": "Thành Lũy Thần Thuẫn Hoàng Kim Vàng"
  },
  "11": {
    "name": "Nghệ An - Làng Sen Quê Bác",
    "icon": "🪷",
    "cap1": "Huy hiệu Hoa Sen Đất Việt Đồng",
    "cap2": "Đèn dầu soi sáng Trí Tuệ Bạc",
    "cap3": "Búp Sen Hoàng Kim Đại Trí Vàng"
  },
  "12": {
    "name": "Hà Tĩnh - Ngã ba Đồng Lộc",
    "icon": "⭐",
    "cap1": "Vỏ đạn đồng Lưu Niệm",
    "cap2": "Chuông gió Hòa Bình Bạc Sáng",
    "cap3": "Ngôi sao Chiến công Mười Cô Gái Vàng"
  },
  "13": {
    "name": "Quảng Bình - Phong Nha Kẻ Bàng",
    "icon": "🦇",
    "cap1": "Tinh thể nhũ đá Khởi Hoang Đồng",
    "cap2": "Đèn pin xuyên hang Bạc Băng",
    "cap3": "Trượng thần Động Tiên Sơn Hoàng Kim Vàng"
  },
  "14": {
    "name": "Quảng Trị - Cầu Hiền Lương",
    "icon": "🕊️",
    "cap1": "Mảnh phù điêu Hiền Lương Đồng",
    "cap2": "Nhành Oliu Hòa Bình Mạ Bạc",
    "cap3": "Chuông Khải Hoàn Non Sông Liền Dải Vàng"
  },
  "15": {
    "name": "Huế - Quần thể Cố đô Huế",
    "icon": "👑",
    "cap1": "Tách trà Cung đình Đồng Hun",
    "cap2": "Quạt lụa Ngự Uyển Dát Bạc",
    "cap3": "Bảo kiếm Hoàng Gia Triều Nguyễn Vàng"
  },
  "16": {
    "name": "Đà Nẵng - Cầu Rồng & Ngũ Hành",
    "icon": "🌉",
    "cap1": "Mảnh đá Non Nước Ngũ Hành Đồng",
    "cap2": "Móng vuốt Rồng Bay Bạc Ánh",
    "cap3": "Viên ngọc Rồng Ngũ Hành Thần Lực Vàng"
  },
  "17": {
    "name": "Quảng Nam - Phố cổ Hội An",
    "icon": "🏮",
    "cap1": "Đèn lồng đất nung Hội An Đồng",
    "cap2": "Phù điêu Apsara Chăm-pa Bạc",
    "cap3": "Thần Đăng Cổ Kính Phố Hội Hoàng Kim Vàng"
  },
  "18": {
    "name": "Quảng Ngãi - Đảo Lý Sơn",
    "icon": "🛡️",
    "cap1": "Viên đá núi lửa Lý Sơn Đồng",
    "cap2": "Kính thiên văn Biển Bạch Kim Bạc",
    "cap3": "Cờ lệnh Hùng Binh Hoàng Sa Hoàng Kim Vàng"
  },
  "19": {
    "name": "Kon Tum - Bờ Y Ngã ba ĐD",
    "icon": "🔭",
    "cap1": "Huy hiệu Cột mốc Bờ Y Đồng",
    "cap2": "Mô hình Nhà thờ Gỗ Bạc",
    "cap3": "Chuông bạc Kon Klor Vàng"
  },
  "20": {
    "name": "Gia Lai - Biển Hồ Tơ Nưng",
    "icon": "💧",
    "cap1": "Huy hiệu Giọt ngọc Tơ Nưng Đồng",
    "cap2": "Hoa dã quỳ Chư Đăng Ya Bạc",
    "cap3": "Đôi mắt Pleiku Hoàng Kim Vàng"
  },
  "21": {
    "name": "Đắk Lắk - Buôn Đôn & Dray Nur",
    "icon": "🐘",
    "cap1": "Vòng ngà voi Bản Đôn Đồng",
    "cap2": "Cồng chiêng Đại ngàn Bạc",
    "cap3": "Hạt cà phê Vàng Buôn Ma Thuột"
  },
  "22": {
    "name": "Đắk Nông - Hồ Tà Đùng",
    "icon": "🏞️",
    "cap1": "Huy hiệu Đảo xanh Tà Đùng Đồng",
    "cap2": "Thạch anh núi lửa Chư Blúk Bạc",
    "cap3": "Vương miện Vịnh Tà Đùng Vàng"
  },
  "23": {
    "name": "Phú Yên - Gành Đá Đĩa",
    "icon": "🗿",
    "cap1": "Phiến đá lục giác Bazan Đồng",
    "cap2": "Hải đăng Mũi Điện Bạc",
    "cap3": "Ánh bình minh Đại Lãnh Vàng"
  },
  "24": {
    "name": "Khánh Hòa - Nha Trang & Trầm Hương",
    "icon": "🏖️",
    "cap1": "Vỏ ốc ngọc Nha Trang Đồng",
    "cap2": "Tháp Trầm Hương Bạc",
    "cap3": "San hô biển Ngọc Hoàng Kim Vàng"
  },
  "25": {
    "name": "Ninh Thuận - Tháp Po Klong Garai",
    "icon": "🛕",
    "cap1": "Chùm nho ngọc Ninh Thuận Đồng",
    "cap2": "Tượng thần Shiva Po Klong Garai Bạc",
    "cap3": "Hạt ngọc Vĩnh Hy Vàng"
  },
  "26": {
    "name": "Bình Thuận - Mũi Né & Bàu Trắng",
    "icon": "⏳",
    "cap1": "Đồng hồ cát Mũi Né Đồng",
    "cap2": "Đóa sen Bàu Trắng Bạc",
    "cap3": "Ngọn đuốc Kê Gà Hoàng Kim Vàng"
  },
  "27": {
    "name": "Lâm Đồng - Đỉnh Lang Biang",
    "icon": "🌸",
    "cap1": "Cành hoa bất tử Đà Lạt Đồng",
    "cap2": "Chiếc sừng hươu Lang Biang Bạc",
    "cap3": "Trái tim ngàn hoa Đà Lạt Vàng"
  },
  "28": {
    "name": "TP.HCM - Củ Chi & Rừng Sác",
    "icon": "🎖️",
    "cap1": "Vành mũ tai bèo Đồng",
    "cap2": "Chiếc khăn rằn Chiến khu Bạc",
    "cap3": "Ngôi sao Đất Thép Thành Đồng Vàng"
  },
  "29": {
    "name": "Tây Ninh - Núi Bà Đen",
    "icon": "⛰️",
    "cap1": "Chuông gió đỉnh Mây Núi Bà Đồng",
    "cap2": "Tượng Phật Bà Tây Bổ Đà Sơn Bạc",
    "cap3": "Vương trượng Núi Bà Đen Vàng"
  },
  "30": {
    "name": "TP.HCM - Bến Nhà Rồng & LM81",
    "icon": "🏙️",
    "cap1": "Bánh lái Tàu Bến Nhà Rồng Đồng",
    "cap2": "Mô hình Tòa tháp Landmark 81 Bạc",
    "cap3": "Kim khánh Thành phố Bác Vàng"
  },
  "31": {
    "name": "Đồng Tháp - Sa Đéc & Sen Tháp Mười",
    "icon": "🪷",
    "cap1": "Chiếc giỏ hoa Sa Đéc Đồng",
    "cap2": "Cánh chim Sếu Tràm Chim Bạc",
    "cap3": "Búp sen Ngọc Tháp Mười Vàng"
  },
  "32": {
    "name": "Cà Mau - Đất Mũi Cà Mau",
    "icon": "🧭",
    "cap1": "Chiếc mỏ neo Mũi Cà Mau Đồng",
    "cap2": "Cột mốc Tọa độ GPS 0001 Bạc",
    "cap3": "Con thuyền Cực Nam No Gió Vàng"
  },
  "33": {
    "name": "Kiên Giang - Đảo Ngọc Phú Quốc",
    "icon": "🐚",
    "cap1": "Vỏ trai đảo ngọc Đồng",
    "cap2": "Cabin cáp treo Hòn Thơm Bạc",
    "cap3": "Viên ngọc trai Phú Quốc Hoàng Gia Vàng"
  },
  "34": {
    "name": "Khánh Hòa - Quần đảo Trường Sa",
    "icon": "🇻🇳",
    "cap1": "Quả bàng vuông Trường Sa Đồng",
    "cap2": "Cột mốc Chủ quyền Đảo Bạc",
    "cap3": "Ngôi sao Hải quân Trường Sa Vàng"
  },
  "35": {
    "name": "Đà Nẵng - Quần đảo Hoàng Sa",
    "icon": "🏆",
    "cap1": "Huy chương Chiến sĩ Hoàng Sa Đồng",
    "cap2": "Phiến đá Chủ quyền Hoàng Sa Bạc",
    "cap3": "Cúp Vàng Quán Quân Xuyên Việt"
  }
};

function BagPage() {
  const navigate = useNavigate();
  const currentStudent = localStorage.getItem('studentName') || "";
  const [medals, setMedals] = useState({ gold: 0, silver: 0, bronze: 0 });
  const [inventory, setInventory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filterMode, setFilterMode] = useState("all"); // all, hk1, hk2

  useEffect(() => {
    if (!currentStudent) {
      alert("Vui lòng đăng ký tên tại Bản đồ trước!");
      navigate("/");
      return;
    }

    const loadInventory = async () => {
      try {
        const snapshot = await db.ref('scores').once('value');
        const allScores = snapshot.val() || {};

        let newGold = 0;
        let newSilver = 0;
        let newBronze = 0;
        let items = [];

        for (let week = 1; week <= 35; week++) {
          const item = ITEMS_DATA[String(week)];
          const weekKey = "Tuan_" + week;
          const weekData = allScores[weekKey] || {};
          
          let unlocked = false;
          let medalIcon = "";
          let badgeName = "";
          let bestScore = 0;

          const results = Object.values(weekData).filter(s => 
            (s.fullName || s.name || "").trim().toLowerCase() === currentStudent.trim().toLowerCase()
          );

          if (results.length > 0) {
            results.sort((a, b) => b.score - a.score);
            const best = results[0];
            bestScore = best.score || 0;

            if (bestScore >= 50) {
              unlocked = true;
              if (bestScore === 100) {
                newGold++;
                medalIcon = "🥇";
                badgeName = item.cap3;
              } else if (bestScore >= 90) {
                newSilver++;
                medalIcon = "🥈";
                badgeName = item.cap2;
              } else {
                newBronze++;
                medalIcon = "🥉";
                badgeName = item.cap1;
              }
            }
          }

          items.push({
            week,
            unlocked,
            medalIcon,
            bestScore,
            name: unlocked ? badgeName : item.name,
            icon: unlocked ? item.icon : "🔒",
            status: unlocked ? `${medalIcon} ${bestScore}đ` : `Chưa mở (Tuần ${week})`
          });
        }

        setMedals({ gold: newGold, silver: newSilver, bronze: newBronze });
        setInventory(items);
      } catch (err) {
        console.error("Error loading inventory", err);
      } finally {
        setLoading(false);
      }
    };

    loadInventory();
  }, [currentStudent]);

  if (!currentStudent) return null;

  const filteredItems = inventory.filter(item => {
    if (filterMode === "hk1") return item.week <= 18;
    if (filterMode === "hk2") return item.week >= 19;
    return true;
  });

  return (
    <Page className="page" style={{ padding: "16px", display: "flex", flexDirection: "column", minHeight: "100vh" }}>
      <div style={{ textAlign: "center", marginBottom: "16px", borderBottom: "2px solid var(--p)", paddingBottom: "10px" }}>
        <h1 style={{ fontFamily: "'Bungee', sans-serif", color: "var(--gold)", margin: 0, fontSize: "1.5rem" }}>
          TÚI ĐỒ NHÀ THÁM HIỂM
        </h1>
        <p style={{ marginTop: "5px", fontSize: "0.85rem", color: "#e2e8f0" }}>
          👤 Nhà thám hiểm: <span style={{ color: "var(--gold)", fontWeight: "bold" }}>{currentStudent}</span>
        </p>
      </div>

      {loading ? (
        <div style={{ textAlign: "center", padding: "40px", color: "var(--text-sec)" }}>Đang mở túi đồ...</div>
      ) : (
        <>
          {/* Medals Tally */}
          <div style={{
            display: "flex", justifyContent: "space-around", background: "#1e293b",
            padding: "14px", borderRadius: "14px", marginBottom: "16px",
            border: "1px solid #334155", boxShadow: "inset 0 0 10px rgba(0,0,0,0.5)"
          }}>
            <div style={{ textAlign: "center" }}>
              <span style={{ fontSize: "2rem", display: "block" }}>🥇</span>
              <div style={{ fontSize: "1.4rem", fontWeight: "bold", color: "var(--gold)" }}>{medals.gold}</div>
              <div style={{ fontSize: "0.7rem", color: "#aaa", textTransform: "uppercase" }}>Huy hiệu Vàng</div>
            </div>
            <div style={{ textAlign: "center" }}>
              <span style={{ fontSize: "2rem", display: "block" }}>🥈</span>
              <div style={{ fontSize: "1.4rem", fontWeight: "bold", color: "#e2e8f0" }}>{medals.silver}</div>
              <div style={{ fontSize: "0.7rem", color: "#aaa", textTransform: "uppercase" }}>Huy hiệu Bạc</div>
            </div>
            <div style={{ textAlign: "center" }}>
              <span style={{ fontSize: "2rem", display: "block" }}>🥉</span>
              <div style={{ fontSize: "1.4rem", fontWeight: "bold", color: "#cd7f32" }}>{medals.bronze}</div>
              <div style={{ fontSize: "0.7rem", color: "#aaa", textTransform: "uppercase" }}>Huy hiệu Đồng</div>
            </div>
          </div>

          {/* Filter Tabs */}
          <div style={{ display: "flex", gap: "8px", marginBottom: "14px", justifyContent: "center" }}>
            <button 
              onClick={() => setFilterMode("all")}
              style={{
                padding: "6px 14px", borderRadius: "20px", border: "1px solid var(--p)",
                background: filterMode === "all" ? "var(--p)" : "#1e293b",
                color: filterMode === "all" ? "#000" : "#fff", fontWeight: "bold", fontSize: "0.8rem", cursor: "pointer"
              }}
            >
              Tất cả (35 Trạm)
            </button>
            <button 
              onClick={() => setFilterMode("hk1")}
              style={{
                padding: "6px 14px", borderRadius: "20px", border: "1px solid var(--p)",
                background: filterMode === "hk1" ? "var(--p)" : "#1e293b",
                color: filterMode === "hk1" ? "#000" : "#fff", fontWeight: "bold", fontSize: "0.8rem", cursor: "pointer"
              }}
            >
              Học kỳ 1 (Tuần 1-18)
            </button>
            <button 
              onClick={() => setFilterMode("hk2")}
              style={{
                padding: "6px 14px", borderRadius: "20px", border: "1px solid var(--p)",
                background: filterMode === "hk2" ? "var(--p)" : "#1e293b",
                color: filterMode === "hk2" ? "#000" : "#fff", fontWeight: "bold", fontSize: "0.8rem", cursor: "pointer"
              }}
            >
              Học kỳ 2 (Tuần 19-35)
            </button>
          </div>

          <div style={{ color: "var(--p)", fontFamily: "'Bungee', sans-serif", fontSize: "0.95rem", borderLeft: "4px solid var(--p)", paddingLeft: "10px", marginBottom: "12px" }}>
            🎒 VẬT PHẨM LƯU NIỆM & KỶ NIỆM CHƯƠNG ({filteredItems.filter(i => i.unlocked).length}/{filteredItems.length})
          </div>

          {/* Items Grid */}
          <div style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(135px, 1fr))",
            gap: "10px",
            flexGrow: 1
          }}>
            {filteredItems.map((item) => (
              <div 
                key={item.week}
                style={{
                  background: item.unlocked ? "radial-gradient(circle, #334155 0%, #1e293b 100%)" : "#1e293b",
                  borderRadius: "12px",
                  padding: "10px 8px",
                  textAlign: "center",
                  border: item.unlocked ? "1.5px solid var(--p)" : "1px solid #334155",
                  boxShadow: item.unlocked ? "0 4px 10px rgba(0,0,0,0.3)" : "none",
                  opacity: item.unlocked ? 1 : 0.45,
                  filter: item.unlocked ? "none" : "grayscale(100%)",
                  display: "flex", flexDirection: "column", justifyContent: "space-between"
                }}
              >
                <div>
                  <div style={{ fontSize: "0.65rem", color: "#94a3b8", marginBottom: "2px" }}>TRẠM {item.week}</div>
                  <span style={{ fontSize: "2.2rem", margin: "4px 0", display: "block" }}>{item.icon}</span>
                  <div style={{ fontSize: "0.75rem", fontWeight: "bold", minHeight: "34px", display: "flex", alignItems: "center", justifyContent: "center", lineHeight: "1.2", color: item.unlocked ? "var(--gold)" : "#cbd5e1" }}>
                    {item.name}
                  </div>
                </div>
                <div style={{ fontSize: "0.7rem", color: item.unlocked ? "#2ecc71" : "#94a3b8", fontWeight: "bold", marginTop: "6px" }}>
                  {item.status}
                </div>
              </div>
            ))}
          </div>

          <center style={{ margin: "20px 0" }}>
            <button 
              className="btn-nav" 
              onClick={() => navigate("/")}
              style={{
                display: "inline-block", background: "var(--p)", color: "white", 
                padding: "10px 25px", borderRadius: "20px", fontWeight: "bold", 
                fontSize: "0.95rem", border: "none", cursor: "pointer"
              }}
            >
              QUAY LẠI BẢN ĐỒ
            </button>
          </center>
        </>
      )}

      <footer style={{ background: "#0f172a", padding: "12px", textAlign: "center", borderTop: "1px solid #1e293b", color: "#888", fontSize: "0.75rem", marginTop: "auto" }}>
        <div>© 2026 EduRobot - Hệ thống Học tập Thông minh</div>
        <div style={{ fontSize: "0.65rem", marginTop: "2px" }}>Giáo viên: Lê Thành Long</div>
      </footer>
    </Page>
  );
}

export default BagPage;
