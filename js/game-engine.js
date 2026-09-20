// ==========================================
// LÕI ĐIỀU KHIỂN TRÒ CHƠI - EDUBOT-BTCT5 GAME ENGINE
// Phiên bản: Gamified EdTech Engine (2026)
// Tác giả: LÊ THÀNH LONG
// ==========================================

// 1. CẤU HÌNH FIREBASE
const firebaseConfig = {
    databaseURL: "https://gamhoctap-default-rtdb.asia-southeast1.firebasedatabase.app"
};
if (typeof firebase !== 'undefined' && !firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}
const db = typeof firebase !== 'undefined' ? firebase.database() : null;

// 2. THÔNG TIN HỌC SINH TỪ LOCALSTORAGE
const savedUsername = localStorage.getItem('studentUsername') || '';
let savedName = localStorage.getItem('studentName') || '';
let savedClass = localStorage.getItem('studentClass') || '5';
let savedSchool = localStorage.getItem('studentSchool') || '';
const savedRole = localStorage.getItem('userRole') || 'guest';
const savedStatus = localStorage.getItem('userStatus') || (savedUsername ? 'pending' : 'guest');

// 3. TRẠNG THÁI TOÀN CỤC CỦA TRÒ CHƠI
let currentWeek = 1;
let WEEK_DATA = null;
let isPlaying = false;
let score = 0;
let startTime = 0;
let lives = 3;
let studentAttempt = 1;
let comboCount = 0;

// Vòng 1: Đấu trí Thần tốc (Flash Card Battle)
let currentV1Pool = [];
let v1Index = 0;
let isProcessingV1 = false;
let matchedCountV1 = 0;

// Vòng 2: Hành trình Chinh phục Đỉnh cao (Landmark Stepper Quest)
let currentV2Questions = [];
let v2Index = 0;
let isProcessingV2 = false;
let v2Landmarks = [];

// Vòng 3
let bossQList = [];
let bossIdx = 0;
let bossAnswering = false;
let bossCorrectIdx = -1;
let currentBossIndices = [];

// Kết thúc
let examFinished = false;

// Nhật ký câu sai & ôn tập sư phạm
let wrongQuestionsLog = [];

// Trạng thái Bảng nháp ảo (Virtual Scratchpad)
let isScratchpadOpen = false;
let scratchTool = 'pen'; // 'pen' | 'eraser'
let scratchCanvas = null;
let scratchCtx = null;
let isDrawing = false;
let lastScratchX = 0;
let lastScratchY = 0;

// 4. TIỆN ÍCH HỆ THỐNG
function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}

function formatTime(sec) {
    if (!sec) return "00:00";
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
}

// 5. BẠN ĐỒNG HÀNH ROBOT (MASCOT DIALOGUE, EMOTION & COMBO)
function setMascotSpeech(text) {
    const el = document.getElementById('mascot-speech');
    if (el) {
        el.innerText = text;
        const robot = document.getElementById('mascot-robot');
        if (robot) {
            robot.style.transform = 'scale(1.2) rotate(10deg)';
            setTimeout(() => { robot.style.transform = 'scale(1) rotate(0deg)'; }, 250);
        }
    }
}

function setMascotEmotion(emotion) {
    const robot = document.getElementById('mascot-robot');
    if (!robot) return;
    robot.className = 'mascot-avatar';
    if (emotion === 'happy') {
        robot.innerText = '🤩';
        robot.classList.add('emotion-happy');
    } else if (emotion === 'cheer') {
        robot.innerText = '🎉';
        robot.classList.add('emotion-cheer');
    } else if (emotion === 'comfort') {
        robot.innerText = '🥺';
        robot.classList.add('emotion-comfort');
    } else if (emotion === 'boss') {
        robot.innerText = '⚡';
        robot.classList.add('emotion-boss');
    } else {
        robot.innerText = '🤖';
    }
}

// 5.1. BẢNG NHÁP ẢO VẼ TAY (VIRTUAL SCRATCHPAD)
function toggleScratchpad() {
    const overlay = document.getElementById('scratchpad-overlay');
    if (!overlay) return;
    isScratchpadOpen = !isScratchpadOpen;
    if (isScratchpadOpen) {
        overlay.classList.remove('hidden');
        initScratchpadCanvas();
        playAudioTone('scratch');
    } else {
        overlay.classList.add('hidden');
    }
}

function initScratchpadCanvas() {
    scratchCanvas = document.getElementById('scratchpad-canvas');
    if (!scratchCanvas) return;
    const wrap = document.getElementById('scratchpad-canvas-wrap');
    if (!wrap) return;

    const rect = wrap.getBoundingClientRect();
    if (scratchCanvas.width !== rect.width || scratchCanvas.height !== rect.height) {
        let prevData = null;
        if (scratchCanvas.width > 0 && scratchCanvas.height > 0) {
            try { prevData = scratchCtx ? scratchCtx.getImageData(0, 0, scratchCanvas.width, scratchCanvas.height) : null; } catch(e){}
        }
        scratchCanvas.width = rect.width;
        scratchCanvas.height = rect.height;
        scratchCtx = scratchCanvas.getContext('2d');
        if (prevData) {
            try { scratchCtx.putImageData(prevData, 0, 0); } catch(e){}
        }
    } else {
        scratchCtx = scratchCanvas.getContext('2d');
    }

    if (!scratchCanvas._hasListeners) {
        scratchCanvas._hasListeners = true;

        const getPos = (e) => {
            const r = scratchCanvas.getBoundingClientRect();
            if (e.touches && e.touches.length > 0) {
                return { x: e.touches[0].clientX - r.left, y: e.touches[0].clientY - r.top };
            }
            return { x: e.clientX - r.left, y: e.clientY - r.top };
        };

        const startDraw = (e) => {
            e.preventDefault();
            isDrawing = true;
            const pos = getPos(e);
            lastScratchX = pos.x;
            lastScratchY = pos.y;
        };

        const moveDraw = (e) => {
            if (!isDrawing || !scratchCtx) return;
            e.preventDefault();
            const pos = getPos(e);

            scratchCtx.beginPath();
            scratchCtx.moveTo(lastScratchX, lastScratchY);
            scratchCtx.lineTo(pos.x, pos.y);
            scratchCtx.lineCap = 'round';
            scratchCtx.lineJoin = 'round';

            if (scratchTool === 'eraser') {
                scratchCtx.globalCompositeOperation = 'destination-out';
                scratchCtx.lineWidth = 26;
            } else {
                scratchCtx.globalCompositeOperation = 'source-over';
                scratchCtx.strokeStyle = '#facc15';
                scratchCtx.lineWidth = 3.5;
            }
            scratchCtx.stroke();

            lastScratchX = pos.x;
            lastScratchY = pos.y;
        };

        const stopDraw = () => {
            isDrawing = false;
        };

        scratchCanvas.addEventListener('mousedown', startDraw);
        scratchCanvas.addEventListener('mousemove', moveDraw);
        window.addEventListener('mouseup', stopDraw);

        scratchCanvas.addEventListener('touchstart', startDraw, { passive: false });
        scratchCanvas.addEventListener('touchmove', moveDraw, { passive: false });
        window.addEventListener('touchend', stopDraw);
        window.addEventListener('touchcancel', stopDraw);
    }
}

function setScratchTool(tool) {
    scratchTool = tool;
    const penBtn = document.getElementById('tool-pen');
    const eraserBtn = document.getElementById('tool-eraser');
    if (penBtn) penBtn.classList.toggle('active', tool === 'pen');
    if (eraserBtn) eraserBtn.classList.toggle('active', tool === 'eraser');
}

function clearScratchpad() {
    if (scratchCanvas && scratchCtx) {
        scratchCtx.clearRect(0, 0, scratchCanvas.width, scratchCanvas.height);
        playAudioTone('scratch');
    }
}

// 5.2. BỘ PHÁT SINH GỢI Ý & PHƯƠNG PHÁP GIẢI TOÁN SƯ PHẠM
function generatePedagogicalGuide(q, correctAns) {
    const qLower = (q || '').toLowerCase();
    const aLower = (correctAns || '').toLowerCase();

    if (qLower.includes('phân số') || aLower.includes('/')) {
        return "📌 <b>Cách làm:</b> Khi cộng/trừ hai phân số khác mẫu, trước hết ta phải quy đồng mẫu số rồi mới cộng/trừ tử số. Khi nhân/chia, lấy tử nhân tử, mẫu nhân mẫu (hoặc nhân với phân số đảo ngược).";
    }
    if (aLower.includes('m²') || aLower.includes('ha') || aLower.includes('km²') || aLower.includes('dm²') || aLower.includes('cm²')) {
        return "📌 <b>Cách làm:</b> Hai đơn vị đo diện tích liền kề nhau gấp hoặc kém nhau 100 lần. Đặc biệt: 1 ha = 10 000 m²; 1 km² = 100 ha = 1 000 000 m².";
    }
    if (aLower.includes('m³') || aLower.includes('dm³') || aLower.includes('cm³') || aLower.includes('lít')) {
        return "📌 <b>Cách làm:</b> Hai đơn vị đo thể tích liền kề nhau gấp hoặc kém nhau 1000 lần. Đặc biệt: 1 dm³ = 1 lít = 1000 cm³.";
    }
    if (qLower.includes('vận tốc') || qLower.includes('quãng đường') || qLower.includes('thời gian') || aLower.includes('km/giờ')) {
        return "📌 <b>Cách làm:</b> Ba đại lượng chuyển động đều liên hệ qua công thức: Quãng đường s = v × t; Vận tốc v = s : t; Thời gian t = s : v (cần chú ý đồng nhất đơn vị đo giờ/phút).";
    }
    if (qLower.includes('tam giác')) {
        return "📌 <b>Cách làm:</b> Diện tích hình tam giác S = (a × h) : 2 (đáy a và chiều cao h phải cùng đơn vị đo).";
    }
    if (qLower.includes('hình thang')) {
        return "📌 <b>Cách làm:</b> Diện tích hình thang S = ((a + b) × h) : 2 (tổng hai đáy nhân với chiều cao rồi chia cho 2).";
    }
    if (qLower.includes('hình tròn') || qLower.includes('chu vi') || aLower.includes('3,14')) {
        return "📌 <b>Cách làm:</b> Chu vi hình tròn C = r × 2 × 3,14 = d × 3,14. Diện tích hình tròn S = r × r × 3,14.";
    }
    if (qLower.includes('hình hộp chữ nhật') || qLower.includes('thể tích')) {
        return "📌 <b>Cách làm:</b> Thể tích hình hộp chữ nhật V = a × b × c (dài × rộng × cao). Diện tích xung quanh = Chu vi đáy × chiều cao = (a + b) × 2 × c.";
    }
    if (qLower.includes('lập phương')) {
        return "📌 <b>Cách làm:</b> Hình lập phương cạnh a: Diện tích xung quanh Sxq = a × a × 4; Toàn phần Stp = a × a × 6; Thể tích V = a × a × a.";
    }
    if (qLower.includes('phần trăm') || aLower.includes('%')) {
        return "📌 <b>Cách làm:</b> Muốn tìm a% của số B, ta lấy B : 100 × a (hoặc B × a : 100). Muốn tìm tỉ số phần trăm của hai số, ta tìm thương rồi nhân với 100 kèm ký hiệu %.";
    }
    if (qLower.includes('trung bình cộng')) {
        return "📌 <b>Cách làm:</b> Muốn tìm số trung bình cộng của nhiều số, ta tính tổng các số đó rồi chia cho số các số hạng.";
    }
    if (qLower.includes('thế kỷ') || aLower.includes('năm')) {
        return "📌 <b>Cách làm:</b> 1 thế kỷ = 100 năm. 1/4 thế kỷ = 100 : 4 = 25 năm; 1/2 thế kỷ = 100 : 2 = 50 năm; 3/4 thế kỷ = 75 năm.";
    }
    return "📌 <b>Cách làm:</b> Đọc kỹ đề bài, xác định đại lượng đã cho và đại lượng cần tìm. Mở bảng [📝 Nháp] để đặt tính cẩn thận từng bước.";
}

function updateComboUI() {
    const badge = document.getElementById('combo-badge');
    if (!badge) return;
    if (comboCount >= 2) {
        badge.innerText = `🔥 COMBO x${comboCount}!`;
        badge.classList.remove('hidden');
    } else {
        badge.classList.add('hidden');
    }
}

function spawnFloatingScore(text, event) {
    const layer = document.getElementById('floating-scores-layer');
    if (!layer) return;
    const el = document.createElement('div');
    el.className = 'floating-score';
    el.innerText = text;

    let x = window.innerWidth / 2;
    let y = window.innerHeight / 2;
    if (event && event.clientX) {
        x = event.clientX;
        y = event.clientY;
    }
    el.style.left = `${x}px`;
    el.style.top = `${y}px`;

    layer.appendChild(el);
    setTimeout(() => {
        if (el.parentNode) el.parentNode.removeChild(el);
    }, 900);
}

// 6. NẠP DỮ LIỆU TUẦN (Hỗ trợ cả HTTP Fetch và Fallback file:/// offline)
function loadWeekData(weekNum) {
    return new Promise((resolve, reject) => {
        fetch(`data/week-${weekNum}.json`)
            .then(res => {
                if (!res.ok) throw new Error(`HTTP ${res.status}`);
                return res.json();
            })
            .then(data => resolve(data))
            .catch(() => {
                if (window[`WEEK_DATA_${weekNum}`]) {
                    return resolve(window[`WEEK_DATA_${weekNum}`]);
                }
                const script = document.createElement('script');
                script.src = `data/week-${weekNum}.js`;
                script.onload = () => {
                    if (window[`WEEK_DATA_${weekNum}`]) {
                        resolve(window[`WEEK_DATA_${weekNum}`]);
                    } else {
                        reject(new Error(`Không tìm thấy dữ liệu tuần ${weekNum}`));
                    }
                };
                script.onerror = () => reject(new Error(`Không tải được tệp dữ liệu tuần ${weekNum}`));
                document.head.appendChild(script);
            });
    });
}

// 7. KIỂM TRA QUYỀN TRUY CẬP TRẠM
function checkStationAccess(weekNum, config) {
    const isTeacherOrAdmin = (savedRole === 'teacher' || savedRole === 'admin');
    const isApproved = (savedStatus === 'approved');

    if (!savedUsername || !isApproved) {
        if (weekNum > 8) {
            alert(`🔒 Trạm ${weekNum} đang khóa!\n• Khách và tài khoản chờ duyệt chỉ được trải nghiệm Trạm 1 đến 8.\n• Vui lòng liên hệ Thầy/Cô để được phê duyệt tài khoản.`);
            window.location.href = 'index.html';
            return false;
        }
        return true;
    }

    if (isTeacherOrAdmin && isApproved) {
        return true;
    }

    if (config && config.openTime) {
        const openTime = new Date(config.openTime);
        const now = new Date();
        if (now < openTime) {
            alert(`⏳ Trạm ${weekNum} chưa mở!\nThời gian mở: ${config.openStr || config.openTime}\nHãy quay lại sau nhé!`);
            window.location.href = 'index.html';
            return false;
        }
    }

    return true;
}

// 8. KHỞI TẠO TRANG KHI LOAD
window.onload = async function () {
    const urlParams = new URLSearchParams(window.location.search);
    const paramWeek = urlParams.get('week') || urlParams.get('tuan') || '1';
    currentWeek = parseInt(paramWeek, 10);
    if (isNaN(currentWeek) || currentWeek < 1 || currentWeek > 35) {
        currentWeek = 1;
    }

    document.getElementById('u-name').innerText = savedName || "Nhà thám hiểm";
    document.getElementById('u-class').innerText = `Lớp ${savedClass}`;

    try {
        WEEK_DATA = await loadWeekData(currentWeek);

        document.title = `TUẦN ${currentWeek}: ${WEEK_DATA.stationName.toUpperCase()} - Học toán 5 cùng Robot`;
        if (document.getElementById('station-title')) {
            document.getElementById('station-title').innerText = `TUẦN ${currentWeek}: TRẠM ${currentWeek}`;
        }
        if (document.getElementById('station-subtitle')) {
            document.getElementById('station-subtitle').innerText = WEEK_DATA.stationName;
        }
        if (WEEK_DATA.souvenirs) {
            if (document.getElementById('souv-cap1')) document.getElementById('souv-cap1').innerHTML = `🥉 <b>Cấp 1 (50đ):</b> ${WEEK_DATA.souvenirs.cap1 || '...'}`;
            if (document.getElementById('souv-cap2')) document.getElementById('souv-cap2').innerHTML = `🥈 <b>Cấp 2 (90đ):</b> ${WEEK_DATA.souvenirs.cap2 || '...'}`;
            if (document.getElementById('souv-cap3')) document.getElementById('souv-cap3').innerHTML = `🥇 <b>Cấp 3 (100đ):</b> ${WEEK_DATA.souvenirs.cap3 || '...'}`;
        }

        setMascotSpeech(`Xin chào ${savedName || 'bạn nhỏ'}! Cùng RoBot chinh phục ${WEEK_DATA.stationName} nhé!`);

        if (!checkStationAccess(currentWeek, WEEK_DATA.config)) {
            return;
        }

        if (db) {
            db.ref(`scores/Tuan_${currentWeek}`).once('value', (snap) => {
                const data = snap.val();
                studentAttempt = 1;
                if (data) {
                    for (let id in data) {
                        const rec = data[id];
                        const matchUser = savedUsername && rec.username === savedUsername;
                        const matchName = (rec.fullName || "").toLowerCase() === savedName.toLowerCase() && rec.className === savedClass;
                        if (matchUser || matchName) {
                            studentAttempt++;
                        }
                    }
                }
                const cycle = ((studentAttempt - 1) % 3) + 1;
                document.getElementById('attempt-info').innerText = `Lượt thám hiểm số: ${studentAttempt} (Bộ đề vòng ${cycle})`;
            });
        } else {
            document.getElementById('attempt-info').innerText = `Lượt thám hiểm số: 1 (Bộ đề vòng 1)`;
        }
    } catch (err) {
        console.error("Lỗi nạp dữ liệu game:", err);
        alert(`Không thể tải dữ liệu tuần ${currentWeek}. Vui lòng thử lại sau!`);
        window.location.href = 'index.html';
    }
};

// 9. BẮT ĐẦU VÀO CHƠI
function handleStartGame() {
    isPlaying = true;
    startTime = Date.now();
    wrongQuestionsLog = [];
    document.getElementById('start-overlay').classList.add('hidden');
    document.getElementById('game-playground').classList.remove('hidden');

    const fab = document.getElementById('scratchpad-fab');
    if (fab) fab.classList.remove('hidden');

    setMascotEmotion('normal');
    setMascotSpeech("Vòng 1: Hãy chọn đáp án chính xác để tiếp sức năng lượng cho RoBot nhé!");
    initStage1();
}

// 10. VÒNG 1: ĐẤU TRÍ THẦN TỐC (10 CÂU X 5Đ = 50Đ)
function initStage1() {
    document.getElementById('stage-badge-title').innerText = "VÒNG 1: ĐẤU TRÍ THẦN TỐC";
    document.getElementById('stage-desc-text').innerText = "Chọn đúng đáp án để sạc năng lượng cho RoBot (Mỗi câu đúng: +5 điểm)";

    const cycle = (studentAttempt - 1) % 3;
    currentV1Pool = WEEK_DATA.bank.V1.slice(cycle * 10, cycle * 10 + 10);
    v1Index = 0;
    matchedCountV1 = 0;
    isProcessingV1 = false;
    updateStage1Progress();
    renderV1Question();
}

function updateStage1Progress() {
    const textEl = document.getElementById('stage-progress-text');
    const fillEl = document.getElementById('stage-progress-fill');
    if (textEl) textEl.innerText = `Câu ${Math.min(v1Index + 1, 10)}/10`;
    if (fillEl) fillEl.style.width = `${(v1Index / 10) * 100}%`;
}

// ==========================================
// THUẬT TOÁN SINH ĐÁP ÁN NHIỄU SƯ PHẠM (SMART PEDAGOGICAL DISTRACTOR ENGINE)
// Đảm bảo 100% câu hỏi V1 & V2 sinh ra 3 đáp án nhiễu sát sườn đề bài:
// - Cùng định dạng phân số, cùng mẫu/tử lân cận, phân số đảo ngược
// - Cùng đơn vị đo lường (m², km, kg, năm, chữ số 0, %...)
// - Cùng số chữ số, đảo vị trí chữ số, bẫy toán học phổ biến
// - Khắc phục hoàn toàn việc học sinh đoán mò bằng phương pháp loại trừ!
// ==========================================
function generateSmartDistractors(q, a, bank) {
    a = (a || '').trim();
    q = (q || '').trim();
    const distractors = new Set();

    function add(val) {
        if (!val) return;
        val = String(val).trim();
        if (val.toLowerCase() !== a.toLowerCase() && !distractors.has(val)) {
            distractors.add(val);
        }
    }

    // 1. Biểu thức biến số: x = ... hoặc y = ...
    const varMatch = a.match(/^([xy])\s*=\s*(.+)$/i);
    if (varMatch) {
        const vName = varMatch[1];
        const valPart = varMatch[2].trim();
        
        if (valPart.endsWith('%')) {
            const pNum = parseFloat(valPart);
            if (!isNaN(pNum)) {
                [pNum - 10, pNum + 10, pNum + 20, pNum - 5, pNum + 5].forEach(pn => {
                    if (pn > 0) add(`${vName} = ${pn}%`);
                });
            }
        } else if (valPart.includes(' và ')) {
            add(`${vName} = 8 và ${vName} = 9`);
            add(`${vName} = 10 và ${vName} = 11`);
            add(`${vName} = 9`);
            add(`${vName} = 10`);
        } else {
            const hasComma = valPart.includes(',');
            const rawNum = parseFloat(valPart.replace(',', '.'));
            if (!isNaN(rawNum)) {
                const fmtV = (n) => {
                    if (hasComma) {
                        const decLen = (valPart.split(',')[1] || '').length || 1;
                        return `${vName} = ` + n.toFixed(decLen).replace('.', ',');
                    }
                    return `${vName} = ` + Math.round(n);
                };
                if (rawNum <= 10) {
                    if (rawNum > 1) add(fmtV(rawNum - 1));
                    add(fmtV(rawNum + 1));
                    add(fmtV(rawNum + 2));
                    if (rawNum > 2) add(fmtV(rawNum - 2));
                } else if (rawNum <= 100) {
                    add(fmtV(rawNum + 1));
                    if (rawNum > 1) add(fmtV(rawNum - 1));
                    add(fmtV(rawNum + 5));
                    if (rawNum > 5) add(fmtV(rawNum - 5));
                    add(fmtV(rawNum + 10));
                } else {
                    add(fmtV(rawNum + 10));
                    add(fmtV(rawNum - 10));
                    add(fmtV(rawNum * 2));
                }
            }
        }
    }

    // 2. Công thức hình học & vật lý (S =, C =, V =, h =, t =, v =, Sxq, Stp)
    if (distractors.size < 3 && (a.startsWith('S =') || a.startsWith('C =') || a.startsWith('V =') || a.startsWith('h =') || a.startsWith('t =') || a.startsWith('v =') || a.startsWith('Sxq') || a.startsWith('Stp'))) {
        if (a.includes('a × h') && a.includes(': 2')) {
            add('S = a × h');
            add('S = (a + h) : 2');
            add('S = (a × h) : 4');
            add('C = (a + h) × 2');
        } else if (a.includes('a × h')) {
            add('S = (a × h) : 2');
            add('S = a + h');
            add('S = (a + b) × 2');
            add('S = a × b');
        } else if (a.includes('(m × n) : 2') || a.includes('(d1 × d2) : 2')) {
            add('S = m × n');
            add('S = (m + n) : 2');
            add('S = (m × n) : 4');
            add('C = m × 4');
        } else if (a.includes('(a + b) × h') || a.includes('((a + b) × h) : 2')) {
            add('S = (a + b) × h');
            add('S = (a × b × h) : 2');
            add('S = (a + b + h) : 2');
            add('S = (a × h) : 2');
        } else if (a.includes('r × 2 × 3,14') || a.includes('d × 3,14')) {
            add('C = r × 3,14');
            add('C = r × r × 3,14');
            add('C = d × 2 × 3,14');
            add('S = r × r × 3,14');
        } else if (a.includes('r × r × 3,14')) {
            add('S = r × 2 × 3,14');
            add('S = d × 3,14');
            add('S = d × d × 3,14');
            add('C = r × 2 × 3,14');
        } else if (a.includes('a × a × 4')) {
            add('Sxq = a × a × 6');
            add('Sxq = a × 4');
            add('V = a × a × a');
            add('Stp = a × a × 6');
        } else if (a.includes('a × a × 6')) {
            add('Stp = a × a × 4');
            add('Stp = a × 6');
            add('V = a × a × a');
            add('Sxq = a × a × 4');
        } else if (a.includes('a × a × a')) {
            add('V = a × a × 4');
            add('V = a × a × 6');
            add('V = a × 3');
            add('S = a × a × 6');
        } else if (a.includes('a × b × c')) {
            add('V = (a + b) × c');
            add('Sxq = (a + b) × 2 × c');
            add('V = a × b');
            add('Stp = (a + b) × 2 × c + 2 × a × b');
        } else if (a.includes('(a + b) × 2 × c')) {
            add('Stp = (a + b) × 2 × c + 2 × a × b');
            add('V = a × b × c');
            add('Sxq = (a + b) × c');
            add('S = a × b × 2');
        } else if (a.includes('(v1 + v2)')) {
            add('t = s : (v1 - v2)');
            add('t = s × (v1 + v2)');
            add('t = (v1 + v2) : s');
        } else if (a.includes('(v1 - v2)')) {
            add('t = s : (v1 + v2)');
            add('t = s × (v1 - v2)');
            add('t = (v1 - v2) : s');
        } else if (a.includes('s : t')) {
            add('v = s × t');
            add('v = t : s');
            add('v = s + t');
        } else if (a.includes('h = (S × 2) : (a + b)')) {
            add('h = S : (a + b)');
            add('h = (S × 2) : (a × b)');
            add('h = (S : 2) : (a + b)');
        }
    }

    // 3. Phân số quy đồng ghép đôi: N1/D1 và N2/D2
    if (distractors.size < 3) {
        const pairedMatch = a.match(/^(\d+)\/(\d+)\s+và\s+(\d+)\/(\d+)$/);
        if (pairedMatch) {
            const n1 = parseInt(pairedMatch[1]);
            const d1 = parseInt(pairedMatch[2]);
            const n2 = parseInt(pairedMatch[3]);
            const d2 = parseInt(pairedMatch[4]);
            add(`${n2}/${d2} và ${n1}/${d1}`);
            add(`${n1 + 1}/${d1} và ${n2}/${d2}`);
            add(`${n1}/${d1} và ${n2 + 1}/${d2}`);
            if (n1 > 1) add(`${n1 - 1}/${d1} và ${n2}/${d2}`);
            if (n2 > 1) add(`${n1}/${d1} và ${n2 - 1}/${d2}`);
            add(`${n1}/${d1} và ${n2}/${d2 + 1}`);
        }
    }

    // 4. Phân số đơn: N/D hoặc N/D (hoặc X)
    if (distractors.size < 3) {
        const fracMatch = a.match(/^(\d+)\s*\/\s*(\d+)(.*)$/);
        if (fracMatch && !a.includes('và')) {
            const n = parseInt(fracMatch[1]);
            const d = parseInt(fracMatch[2]);
            if (n !== d && d !== 0) {
                add(`${d}/${n}`); // Nghịch đảo (bẫy kinh điển)
                if (d > n) add(`${d - n}/${d}`); // Phân số bù
                if (n > 1) add(`${n - 1}/${d}`);
                add(`${n + 1}/${d}`);
                if (d > 2) add(`${n}/${d - 1}`);
                add(`${n}/${d + 1}`);
                add(`${n + 1}/${d + 1}`);
                add(`${n * 2}/${d * 2 + 1}`);
            }
        }
    }

    // 5. Hỗn số: W N/D
    if (distractors.size < 3) {
        const mixedMatch = a.match(/^(\d+)\s+(\d+)\/(\d+)(.*)$/);
        if (mixedMatch) {
            const w = parseInt(mixedMatch[1]);
            const n = parseInt(mixedMatch[2]);
            const d = parseInt(mixedMatch[3]);
            if (w > 1) add(`${w - 1} ${n}/${d}`);
            add(`${w + 1} ${n}/${d}`);
            if (n > 1) add(`${w} ${n - 1}/${d}`);
            add(`${w} ${n + 1}/${d}`);
            add(`${w} ${d}/${n}`);
            add(`${w * d + n}/${d}`);
        }
    }

    // 6. So sánh từ ngữ / Phép biến đổi / Đọc số
    if (distractors.size < 3) {
        if (/^bé hơn\s+\d+/i.test(a)) {
            const num = a.replace(/^[^\d]*/, '');
            add(`Lớn hơn ${num}`);
            add(`Bằng ${num}`);
            add(`Bằng 0`);
        } else if (/^lớn hơn\s+\d+/i.test(a)) {
            const num = a.replace(/^[^\d]*/, '');
            add(`Bé hơn ${num}`);
            add(`Bằng ${num}`);
            add(`Gấp đôi ${num}`);
        } else if (/^bằng\s+\d+/i.test(a)) {
            const num = a.replace(/^[^\d]*/, '');
            add(`Bé hơn ${num}`);
            add(`Lớn hơn ${num}`);
            add(`Không so sánh được`);
        } else if (a.toLowerCase().includes('bằng nhau')) {
            add('Lớn hơn (>)');
            add('Bé hơn (<)');
            add('Không so sánh được');
        } else if (/^chia cho\s+\d+/i.test(a)) {
            const num = parseInt(a.replace(/^[^\d]*/, '')) || 2;
            add(`Chia cho ${num === 2 ? 4 : num - 1}`);
            add(`Chia cho ${num + 1}`);
            add(`Nhân với ${num}`);
        } else if (/^gấp\s+\d+\s*lần/i.test(a)) {
            const num = parseInt(a.replace(/^[^\d]*/, '')) || 2;
            add(`Gấp ${num + 1} lần`);
            add(`Gấp ${num === 2 ? 4 : num - 1} lần`);
            add(`Giảm đi ${num} lần`);
        } else if (a === 'Hai và ba phần năm') {
            add('Ba và hai phần năm');
            add('Hai và năm phần ba');
            add('Năm và ba phần hai');
        } else if (a === 'Một phần trăm') {
            add('Mười phần trăm');
            add('Một phần mười');
            add('Một phần nghìn');
        } else if (a.startsWith('Không phẩy không không một')) {
            add('Không phẩy không một (một phần trăm)');
            add('Không phẩy một (một phần mười)');
            add('Một phần nghìn');
        } else if (a === 'Năm phẩy không tám') {
            add('Năm phẩy tám');
            add('Năm phẩy tám mươi');
            add('Năm mươi phẩy tám');
        } else if (a.startsWith('Héc-ta')) {
            add('Đề-ca-mét vuông (dam²)');
            add('A (a)');
            add('Ki-lô-mét vuông (km²)');
        }
    }

    // 7. Giá trị vị trí (Hàng...)
    if (distractors.size < 3) {
        const placeValues = [
            'Hàng đơn vị', 'Hàng chục', 'Hàng trăm', 'Hàng nghìn',
            'Hàng chục nghìn', 'Hàng trăm nghìn',
            'Hàng phần mười', 'Hàng phần trăm', 'Hàng phần nghìn'
        ];
        if (placeValues.some(p => p.toLowerCase() === a.toLowerCase())) {
            placeValues.forEach(p => add(p));
        }
    }

    // 8. Tỉ số phần trăm: e.g. 100%, 50%, 25%, 30%
    if (distractors.size < 3 && /^\d+[\d.,]*%$/.test(a)) {
        const pNum = parseFloat(a.replace('%', '').replace(',', '.'));
        const commonP = [100, 50, 25, 75, 20, 10, 80, 30, 40, 60, 15];
        commonP.forEach(cp => {
            if (cp !== pNum) add(`${cp}%`);
        });
        if (pNum >= 10 && pNum < 100) {
            add(`${pNum + 10}%`);
            if (pNum > 10) add(`${pNum - 10}%`);
            add(`${pNum + 5}%`);
        }
    }

    // 9. Biểu thức so sánh: X > Y hoặc X < Y hoặc X = Y
    if (distractors.size < 3) {
        const compExprMatch = a.match(/^(.+?)\s*([><=])\s*(.+)$/);
        if (compExprMatch && !a.startsWith('S =') && !a.startsWith('C =') && !a.startsWith('V =') && !a.startsWith('x =') && !a.startsWith('y =') && !a.startsWith('h =') && !a.startsWith('t =') && !a.startsWith('v =')) {
            const left = compExprMatch[1].trim();
            const op = compExprMatch[2].trim();
            const right = compExprMatch[3].trim();
            const oppOp = (op === '>') ? '<' : (op === '<' ? '>' : '≠');
            add(`${left} ${oppOp} ${right}`);
            add(`${left} = ${right}`);
            add(`${right} ${op} ${left}`);
            add(`${right} ${oppOp} ${left}`);
        }
    }

    // 10. Số kèm đơn vị: <Số> <Đơn vị>
    if (distractors.size < 3) {
        const unitMatch = a.match(/^([\d\s.,]+)\s+([a-zA-Zà-ỹÀ-Ỹ²³%]+(\/[a-zA-Zà-ỹÀ-Ỹ]+)?.*)$/);
        if (unitMatch && !a.includes('/')) {
            const numStr = unitMatch[1].trim();
            const unit = unitMatch[2].trim();
            const hasSpace = numStr.includes(' ');
            const hasComma = numStr.includes(',');
            const rawNum = parseFloat(numStr.replace(/\s+/g, '').replace(',', '.'));
            if (!isNaN(rawNum)) {
                const fmt = (n) => {
                    if (hasComma) {
                        const decLen = (numStr.split(',')[1] || '').length || 1;
                        return n.toFixed(decLen).replace('.', ',') + ' ' + unit;
                    }
                    if (hasSpace) {
                        return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + ' ' + unit;
                    }
                    return Math.round(n) + ' ' + unit;
                };

                if (rawNum >= 10 && rawNum < 100 && Math.floor(rawNum) === rawNum) {
                    const s = rawNum.toString();
                    if (s.length === 2 && s[0] !== s[1] && s[1] !== '0') {
                        add(fmt(parseInt(s[1] + s[0])));
                    }
                }
                if (rawNum <= 10) {
                    if (rawNum > 1) add(fmt(rawNum - 1));
                    add(fmt(rawNum + 1));
                    add(fmt(rawNum + 2));
                    if (rawNum > 2) add(fmt(rawNum - 2));
                } else if (rawNum <= 100) {
                    add(fmt(rawNum + 10));
                    if (rawNum > 10) add(fmt(rawNum - 10));
                    add(fmt(rawNum + 5));
                    if (rawNum > 5) add(fmt(rawNum - 5));
                    add(fmt(rawNum + 1));
                    if (rawNum > 1) add(fmt(rawNum - 1));
                } else {
                    const delta = Math.pow(10, Math.max(1, Math.floor(Math.log10(rawNum)) - 1));
                    add(fmt(rawNum + delta));
                    if (rawNum > delta) add(fmt(rawNum - delta));
                    add(fmt(rawNum + delta * 2));
                    add(fmt(rawNum * 2));
                    if (rawNum % 2 === 0) add(fmt(rawNum / 2));
                }
            }
        }
    }

    // 11. Số thuần túy (số nguyên, số lớn có dấu cách, số thập phân)
    if (distractors.size < 3) {
        const pureNumMatch = a.match(/^[\d\s.,]+$/);
        if (pureNumMatch && !a.includes('/')) {
            const hasSpace = a.includes(' ');
            const hasComma = a.includes(',');
            const rawNum = parseFloat(a.replace(/\s+/g, '').replace(',', '.'));
            if (!isNaN(rawNum)) {
                const fmt = (n) => {
                    if (hasComma) {
                        const decLen = (a.split(',')[1] || '').length || 1;
                        return n.toFixed(decLen).replace('.', ',');
                    }
                    if (hasSpace) {
                        return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
                    }
                    return Math.round(n).toString();
                };

                const cleanStr = a.replace(/\s+/g, '');
                if (cleanStr === '987654') {
                    add('987 645');
                    add('999 999');
                    add('987 564');
                    add('876 543');
                } else if (cleanStr === '102345') {
                    add('102 354');
                    add('100 000');
                    add('123 456');
                    add('102 435');
                } else if (rawNum >= 10 && rawNum < 100 && Math.floor(rawNum) === rawNum) {
                    const s = rawNum.toString();
                    if (s.length === 2 && s[0] !== s[1] && s[1] !== '0') {
                        add(fmt(parseInt(s[1] + s[0])));
                    }
                    add(fmt(rawNum + 10));
                    if (rawNum > 10) add(fmt(rawNum - 10));
                    add(fmt(rawNum + 1));
                    if (rawNum > 1) add(fmt(rawNum - 1));
                    add(fmt(rawNum + 5));
                } else if (rawNum <= 10) {
                    if (rawNum > 1) add(fmt(rawNum - 1));
                    add(fmt(rawNum + 1));
                    add(fmt(rawNum + 2));
                    add(fmt(rawNum * 2));
                    if (rawNum > 2) add(fmt(rawNum - 2));
                } else {
                    const delta = Math.pow(10, Math.max(1, Math.floor(Math.log10(rawNum)) - 1));
                    add(fmt(rawNum + delta));
                    if (rawNum > delta) add(fmt(rawNum - delta));
                    add(fmt(rawNum + delta * 2));
                    add(fmt(rawNum + 1));
                    if (rawNum > 1) add(fmt(rawNum - 1));
                    add(fmt(rawNum * 2));
                }
            }
        }
    }

    // 12. Kho địa danh & văn hóa đặc trưng
    if (distractors.size < 3) {
        const provinces = [
            'Hà Giang', 'Cao Bằng', 'Bắc Kạn', 'Lạng Sơn', 'Lào Cai', 'Yên Bái',
            'Sơn La', 'Quảng Ninh', 'Hà Nội', 'Ninh Bình', 'Thanh Hóa', 'Nghệ An',
            'Thừa Thiên Huế', 'Đà Nẵng', 'Quảng Nam', 'Khánh Hòa', 'Lâm Đồng',
            'TP. Hồ Chí Minh', 'Cần Thơ', 'Cà Mau', 'Tây Ninh', 'Đồng Tháp'
        ];
        if (provinces.some(p => p.toLowerCase() === a.toLowerCase()) || q.toLowerCase().includes('tỉnh nào') || q.toLowerCase().includes('thành phố nào')) {
            provinces.forEach(p => add(p));
        }

        const passes = ['Đèo Mã Pí Lèng', 'Đèo Khau Phạ', 'Đèo Ô Quy Hồ', 'Đèo Pha Đin', 'Đèo Hải Vân', 'Đèo Cả', 'Đèo Ngoạn Mục'];
        if (passes.some(p => p.toLowerCase() === a.toLowerCase()) || q.toLowerCase().includes('đèo nổi tiếng nào') || q.toLowerCase().includes('con đèo')) {
            passes.forEach(p => add(p));
        }

        const waters = ['Sông Nho Quế', 'Sông Quây Sơn', 'Sông Gâm', 'Sông Hồng', 'Sông Hương', 'Hồ Ba Bể', 'Thác Bản Giốc', 'Thác Đầu Đẳng', 'Sông Sài Gòn', 'Sông Tiền'];
        if (waters.some(w => w.toLowerCase() === a.toLowerCase()) || q.toLowerCase().includes('dòng sông') || q.toLowerCase().includes('thác nước')) {
            waters.forEach(w => add(w));
        }
    }

    // 13. Dự phòng từ Ngân hàng đề: Tìm đáp án đồng nhất định dạng
    if (distractors.size < 3 && bank && Array.isArray(bank)) {
        // Bước 1: Khớp chuẩn xác định dạng (cùng là phân số, cùng là chữ, cùng đơn vị)
        bank.forEach(item => {
            if (distractors.size >= 3) return;
            const itemA = item.a.trim();
            if (itemA.toLowerCase() !== a.toLowerCase()) {
                if (a.includes('/') && itemA.includes('/')) add(itemA);
                else if (!/\d/.test(a) && !/\d/.test(itemA)) add(itemA);
                else if (/\d/.test(a) && /\d/.test(itemA)) {
                    const uA = (a.match(/[a-zA-Zà-ỹÀ-Ỹ²³%]+/) || [])[0];
                    const uB = (itemA.match(/[a-zA-Zà-ỹÀ-Ỹ²³%]+/) || [])[0];
                    if (uA && uB && uA === uB) add(itemA);
                }
            }
        });

        // Bước 2: Khớp cùng nhóm (cùng có chữ hoặc cùng có số)
        if (distractors.size < 3) {
            bank.forEach(item => {
                if (distractors.size >= 3) return;
                const itemA = item.a.trim();
                if (itemA.toLowerCase() !== a.toLowerCase()) {
                    const aHasNum = /\d/.test(a);
                    const bHasNum = /\d/.test(itemA);
                    if (aHasNum === bHasNum) {
                        add(itemA);
                    }
                }
            });
        }

        // Bước 3: Lấy các đáp án khác trong ngân hàng
        if (distractors.size < 3) {
            bank.forEach(item => {
                if (distractors.size >= 3) return;
                const itemA = item.a.trim();
                if (itemA.toLowerCase() !== a.toLowerCase()) {
                    add(itemA);
                }
            });
        }
    }

    return Array.from(distractors).slice(0, 3);
}

function renderV1Question() {
    if (v1Index >= currentV1Pool.length || v1Index >= 10) {
        comboCount = 0;
        updateComboUI();
        setMascotSpeech("🎉 Hoàn thành xuất sắc Vòng 1! Cùng tiến vào Vòng 2 nào!");
        setTimeout(initStage2, 700);
        return;
    }

    const currentItem = currentV1Pool[v1Index];
    const cardBadge = document.getElementById('v1-card-badge');
    const cardText = document.getElementById('v1-question-text');
    const optGrid = document.getElementById('v1-options-grid');
    const cardEl = document.getElementById('v1-card');

    if (cardEl) {
        cardEl.classList.remove('flash-correct', 'shake');
    }
    if (cardBadge) cardBadge.innerText = `⚡ THỬ THÁCH ${v1Index + 1}/10`;
    if (cardText) cardText.innerText = currentItem.q;

    // Sinh 4 phương án: 1 đúng + 3 nhiễu sư phạm sát đề
    const correctAns = currentItem.a.trim();
    const bank = (WEEK_DATA && WEEK_DATA.bank && WEEK_DATA.bank.V1) ? WEEK_DATA.bank.V1 : currentV1Pool;
    const smartDistractors = generateSmartDistractors(currentItem.q, correctAns, bank);
    let options = [correctAns, ...smartDistractors];
    shuffleArray(options);

    const labels = ['A', 'B', 'C', 'D'];
    if (optGrid) {
        optGrid.innerHTML = '';
        options.forEach((optVal, idx) => {
            const orb = document.createElement('div');
            orb.className = 'v1-option-orb';
            orb.innerHTML = `<span class="v1-option-key">${labels[idx]}</span><span class="v1-option-text">${optVal}</span>`;
            orb.onclick = (e) => handleV1OptionClick(optVal, correctAns, orb, e, currentItem);
            optGrid.appendChild(orb);
        });
    }

    updateStage1Progress();
}

function handleV1OptionClick(chosenVal, correctVal, orbEl, event, questionItem) {
    if (isProcessingV1) return;
    isProcessingV1 = true;

    try {
        const isMatch = (chosenVal.trim().toLowerCase() === correctVal.trim().toLowerCase());
        const cardEl = document.getElementById('v1-card');
        const currentItem = questionItem || (currentV1Pool && currentV1Pool[v1Index]) || { q: '', a: correctVal };

        if (isMatch) {
            orbEl.classList.add('correct');
            if (cardEl) cardEl.classList.add('flash-correct');
            comboCount++;
            if (comboCount >= 2) {
                playAudioTone('combo');
                setMascotEmotion('cheer');
                setMascotSpeech(`🔥 Tuyệt đỉnh! Combo x${comboCount} liên tiếp rồi!`);
            } else {
                playAudioTone('success');
                setMascotEmotion('happy');
                const praises = [
                    "Chính xác! Giỏi lắm bạn ơi!",
                    "Chuẩn luôn! Một thử thách nữa đã vượt qua!",
                    "Xuất sắc! Cứ thế phát huy nhé!"
                ];
                setMascotSpeech(praises[Math.floor(Math.random() * praises.length)]);
            }
            updateComboUI();

            score += 5;
            matchedCountV1++;
            updateScoreUI();
            spawnFloatingScore("+5đ", event);

            setTimeout(() => {
                v1Index++;
                isProcessingV1 = false;
                renderV1Question();
            }, 380);
        } else {
            orbEl.classList.add('wrong');
            if (cardEl) cardEl.classList.add('shake');
            comboCount = 0;
            updateComboUI();
            playAudioTone('error');
            lives = Math.max(0, lives - 1);
            updateLivesUI();

            // Ghi nhận câu sai để ôn tập sư phạm sau trận
            wrongQuestionsLog.push({
                q: currentItem.q || (cardEl ? cardEl.querySelector('.v1-card-content')?.innerText : '') || '',
                chosen: chosenVal,
                correct: correctVal,
                round: 'Vòng 1: Đấu Trí Thần Tốc'
            });
            setMascotEmotion('comfort');

            // Highlight đáp án đúng để học sinh quan sát và ghi nhớ
            document.querySelectorAll('.v1-option-orb').forEach(btn => {
                const textSpan = btn.querySelector('.v1-option-text');
                if (textSpan && textSpan.innerText.trim().toLowerCase() === correctVal.trim().toLowerCase()) {
                    btn.classList.add('correct');
                }
            });

            if (lives === 1) {
                setMascotSpeech("⚠️ Cẩn thận nhé, bạn chỉ còn 1 trái tim cuối cùng thôi! Mở [📝 Nháp] để tính cẩn thận nhé.");
            } else {
                setMascotSpeech("Chưa đúng rồi! Hãy quan sát kỹ đáp án đúng hoặc mở [📝 Nháp] để đặt tính nhé.");
            }

            setTimeout(() => {
                if (cardEl) cardEl.classList.remove('shake');
                if (lives <= 0) {
                    alert("⚠️ Em đã hết 3 mạng! Chuyển thẳng sang Vòng 2.");
                    isProcessingV1 = false;
                    initStage2();
                } else {
                    v1Index++;
                    isProcessingV1 = false;
                    renderV1Question();
                }
            }, 800);
        }
    } catch (err) {
        console.error('Error in handleV1OptionClick:', err);
        isProcessingV1 = false;
    }
}

// 11. VÒNG 2: HÀNH TRÌNH CHINH PHỤC ĐỈNH CAO (4 BÀI X 10Đ = 40Đ)
function getWeekLandmarks(weekNum, stationName) {
    if (weekNum === 1) {
        return [
            "Chân núi Rồng",
            "Cổng trời Quản Bạ",
            "Vọng đài ngắm cảnh",
            "Đỉnh Cột cờ Lũng Cú"
        ];
    }
    const cleanName = stationName ? stationName.replace(/Trạm \d+:\s*/i, '') : 'Đích đến';
    return [
        "Chặng 1: Xuất phát",
        "Chặng 2: Tăng tốc",
        "Chặng 3: Vượt chướng ngại",
        `Đích: ${cleanName}`
    ];
}

function initStage2() {
    document.getElementById('stage-1-area').classList.add('hidden');
    document.getElementById('stage-2-area').classList.remove('hidden');
    document.getElementById('stage-badge-title').innerText = "VÒNG 2: HÀNH TRÌNH CHINH PHỤC ĐỈNH CAO";
    document.getElementById('stage-desc-text').innerText = "Chạm đúng chip đáp án để RoBot leo lên nấc thang tiếp theo (Mỗi câu đúng: +10 điểm)";

    const cycle = (studentAttempt - 1) % 3;
    if (WEEK_DATA && WEEK_DATA.bank && WEEK_DATA.bank.V2) {
        currentV2Questions = WEEK_DATA.bank.V2.slice(cycle * 4, cycle * 4 + 4);
    }
    v2Index = 0;
    isProcessingV2 = false;
    v2Landmarks = getWeekLandmarks(currentWeek, (WEEK_DATA ? WEEK_DATA.stationName : ''));

    setMascotSpeech("Vòng 2: Cùng RoBot vượt 4 chặng để chinh phục đỉnh cao nhé!");
    renderV2Mission();
}

function renderV2Mission() {
    if (v2Index >= 4 || v2Index >= currentV2Questions.length) {
        const progFill = document.getElementById('stage-progress-fill');
        if (progFill) progFill.style.width = '66%';
        playAudioTone('combo');
        setMascotSpeech("🎉 Xuất sắc! Bạn đã chinh phục toàn bộ các chặng! Chuẩn bị Đấu Boss nào!");
        setTimeout(initStage3, 800);
        return;
    }

    const currentQ = currentV2Questions[v2Index];
    const totalMissions = Math.min(4, currentV2Questions.length);

    // 1. Cập nhật banner tiến trình
    const progText = document.getElementById('stage-progress-text');
    const progFill = document.getElementById('stage-progress-fill');
    if (progText) progText.innerText = `Chặng ${v2Index + 1}/${totalMissions}`;
    if (progFill) progFill.style.width = `${33 + (v2Index / totalMissions) * 33}%`;

    // 2. Cập nhật Stepper
    const stepperFill = document.getElementById('stepper-fill');
    if (stepperFill) {
        stepperFill.style.width = `${(v2Index / (totalMissions - 1)) * 100}%`;
    }

    const nodesContainer = document.getElementById('stepper-nodes');
    if (nodesContainer) {
        nodesContainer.innerHTML = '';
        v2Landmarks.forEach((lmName, idx) => {
            let statusClass = '';
            let iconOrNum = `${idx + 1}`;
            if (idx < v2Index) {
                statusClass = 'completed';
                iconOrNum = '✓';
            } else if (idx === v2Index) {
                statusClass = 'active';
                iconOrNum = '🤖';
            }
            nodesContainer.innerHTML += `
                <div class="stepper-node ${statusClass}">
                    <div class="stepper-circle">${iconOrNum}</div>
                    <div class="stepper-label">${lmName}</div>
                </div>
            `;
        });
    }

    // 3. Cập nhật Thẻ nhiệm vụ
    const badgeEl = document.getElementById('v2-mission-badge');
    const textEl = document.getElementById('v2-mission-text');
    const slotEl = document.getElementById('v2-slot-target');

    if (badgeEl) badgeEl.innerText = `🚩 CHẶNG ${v2Index + 1}: ${v2Landmarks[v2Index]}`;
    if (textEl) textEl.innerText = currentQ.q;
    if (slotEl) {
        slotEl.innerText = `❓ CHẠM CHIP ĐÁP ÁN BÊN DƯỚI`;
        slotEl.className = 'v2-slot-target';
    }

    // 4. Sinh 4 chip lựa chọn sát sườn đề bài (1 đúng + 3 nhiễu sư phạm)
    const correctAns = currentQ.a.trim();
    const bank = (WEEK_DATA && WEEK_DATA.bank && WEEK_DATA.bank.V2) ? WEEK_DATA.bank.V2 : currentV2Questions;
    const smartDistractors = generateSmartDistractors(currentQ.q, correctAns, bank);
    let chipChoices = [correctAns, ...smartDistractors];
    shuffleArray(chipChoices);

    const choicesContainer = document.getElementById('v2-chip-choices');
    if (choicesContainer) {
        choicesContainer.innerHTML = '';
        chipChoices.forEach(ansVal => {
            const chip = document.createElement('div');
            chip.className = 'v2-chip-btn';
            chip.innerText = ansVal;
            chip.onclick = (e) => handleV2ChipClick(ansVal, correctAns, chip, e, currentQ);
            choicesContainer.appendChild(chip);
        });
    }
}

function handleV2ChipClick(chosenVal, correctVal, chipEl, event, questionItem) {
    if (isProcessingV2) return;
    isProcessingV2 = true;

    try {
        const isMatch = (chosenVal.trim().toLowerCase() === correctVal.trim().toLowerCase());
        const slotEl = document.getElementById('v2-slot-target');
        const currentQ = questionItem || (currentV2Questions && currentV2Questions[v2Index]) || { q: '', a: correctVal };

        if (isMatch) {
            chipEl.classList.add('chosen-correct');
            if (slotEl) {
                slotEl.innerText = `✓ ${chosenVal}`;
                slotEl.classList.add('filled-correct');
            }

            playAudioTone('step');
            score += 10;
            updateScoreUI();
            spawnFloatingScore("+10đ", event);

            setMascotEmotion('cheer');
            const landmarkName = (v2Landmarks && v2Landmarks[v2Index]) ? v2Landmarks[v2Index] : `Chặng ${v2Index + 1}`;
            setMascotSpeech(`Chính xác! RoBot đã vượt qua ${landmarkName} để tiếp bước!`);

            setTimeout(() => {
                v2Index++;
                isProcessingV2 = false;
                renderV2Mission();
            }, 600);
        } else {
            chipEl.classList.add('shake-wrong');
            playAudioTone('error');
            lives = Math.max(0, lives - 1);
            updateLivesUI();

            // Ghi nhận câu sai để ôn tập sư phạm sau trận
            wrongQuestionsLog.push({
                q: currentQ.q || '',
                chosen: chosenVal,
                correct: correctVal,
                round: 'Vòng 2: Chinh Phục Đỉnh Cao'
            });
            setMascotEmotion('comfort');

            if (lives === 1) {
                setMascotSpeech("⚠️ Cẩn thận nhé! Chỉ còn 1 trái tim cuối cùng! Nhớ mở [📝 Nháp] để tính.");
            } else {
                setMascotSpeech("Chưa đúng rồi bạn ơi! Hãy mở bảng [📝 Nháp] góc màn hình để đặt tính cẩn thận nhé.");
            }

            setTimeout(() => {
                chipEl.classList.remove('shake-wrong');
                if (lives <= 0) {
                    alert("⚠️ Em đã hết 3 mạng! Chuyển thẳng sang Đấu Boss.");
                    isProcessingV2 = false;
                    initStage3();
                } else {
                    isProcessingV2 = false;
                }
            }, 500);
        }
    } catch (err) {
        console.error('Error in handleV2ChipClick:', err);
        isProcessingV2 = false;
    }
}

// 12. VÒNG 3: ĐẠI CHIẾN BOSS (2 CÂU X 5Đ = 10Đ)
function initStage3() {
    document.getElementById('stage-2-area').classList.add('hidden');
    document.getElementById('stage-3-area').classList.remove('hidden');
    document.getElementById('stage-badge-title').innerText = "VÒNG 3: ĐẠI CHIẾN BOSS PHÂN LOẠI";
    document.getElementById('stage-desc-text').innerText = "Hạ gục Thủ lĩnh bằng tư duy toán học nhạy bén (Mỗi câu đúng: +5 điểm)";

    const bossNameEl = document.getElementById('boss-name');
    if (bossNameEl && WEEK_DATA) {
        bossNameEl.innerText = `👾 THỦ LĨNH: ${WEEK_DATA.stationName.toUpperCase()}`;
    }

    const progText = document.getElementById('stage-progress-text');
    const progFill = document.getElementById('stage-progress-fill');
    if (progText) progText.innerText = "Câu 1/2";
    if (progFill) progFill.style.width = "0%";

    bossIdx = 0;
    bossAnswering = false;

    if (WEEK_DATA && WEEK_DATA.bank && WEEK_DATA.bank.V3) {
        bossQList = [...WEEK_DATA.bank.V3];
        shuffleArray(bossQList);
        bossQList = bossQList.slice(0, 2);
    } else {
        bossQList = [
            { q: "Tính nhanh diện tích mảnh đất hình chữ nhật có chiều dài 25m và chiều rộng 12m?", opts: ["300 m²", "280 m²", "320 m²", "250 m²"], c: 0 },
            { q: "Một xe máy đi với vận tốc 42 km/giờ trong 2,5 giờ. Quãng đường xe máy đi được là:", opts: ["105 km", "100 km", "110 km", "95 km"], c: 0 }
        ];
    }

    const hpBar = document.getElementById('boss-hp');
    const hpText = document.getElementById('boss-hp-text');
    if (hpBar) hpBar.style.width = "100%";
    if (hpText) hpText.innerText = "100 / 100 HP";

    setMascotEmotion('boss');
    setMascotSpeech("Thủ lĩnh đã xuất hiện! Hãy dồn hết sức mạnh trí tuệ để chiến thắng nhé!");
    renderBossQuestion();
}

function renderBossQuestion() {
    if (bossIdx >= bossQList.length || bossIdx >= 2) {
        // Đã hoàn thành Vòng 3 -> Hiện Rương báu chiến thắng
        setMascotEmotion('cheer');
        setMascotSpeech("🎉 CHIẾN THẮNG HUY HOÀNG! Hãy mở rương báu nhận thưởng nào!");
        setTimeout(showLootBox, 700);
        return;
    }

    const q = bossQList[bossIdx];
    document.getElementById('boss-q-text').innerText = `Câu ${bossIdx + 1}: ${q.q}`;

    const progText = document.getElementById('stage-progress-text');
    const progFill = document.getElementById('stage-progress-fill');
    if (progText) progText.innerText = `Câu ${bossIdx + 1}/2`;
    if (progFill) progFill.style.width = `${(bossIdx / 2) * 100}%`;

    const optBox = document.getElementById('boss-options');
    optBox.innerHTML = '';

    // Xáo trộn 4 phương án
    let indices = [0, 1, 2, 3];
    shuffleArray(indices);
    bossCorrectIdx = indices.indexOf(q.c);
    currentBossIndices = indices;

    const labels = ['A', 'B', 'C', 'D'];
    indices.forEach((origIdx, newIdx) => {
        const btn = document.createElement('button');
        btn.className = 'btn-mcq-opt';
        btn.innerHTML = `<b>${labels[newIdx]}.</b> ${q.opts[origIdx]}`;
        btn.onclick = (e) => checkBossAnswer(newIdx, e);
        optBox.appendChild(btn);
    });

    bossAnswering = false;
}

function checkBossAnswer(optIdx, event) {
    if (bossAnswering) return;
    bossAnswering = true;

    try {
        const bossAvatar = document.getElementById('boss-avatar');
        const hpBar = document.getElementById('boss-hp');
        const hpText = document.getElementById('boss-hp-text');
        const q = (bossQList && bossQList[bossIdx]) ? bossQList[bossIdx] : null;

        if (optIdx === bossCorrectIdx) {
            playAudioTone('boss-hit');
            score += 5;
            updateScoreUI();
            spawnFloatingScore("+5đ (Trúng Boss!)", event);

            setMascotEmotion('happy');
            if (bossAvatar) bossAvatar.classList.add('hit');
            if (bossIdx === 0) {
                if (hpBar) hpBar.style.width = "50%";
                if (hpText) hpText.innerText = "50 / 100 HP";
                setMascotSpeech("⚡ Cú đánh sấm sét! Boss đã mất 50% lượng máu!");
            } else {
                if (hpBar) hpBar.style.width = "0%";
                if (hpText) hpText.innerText = "0 / 100 HP (HẠ GỤC!)";
                setMascotSpeech("🏆 TUYỆT VỜI! Boss đã bị hạ gục hoàn toàn!");
            }
        } else {
            playAudioTone('error');
            setMascotEmotion('comfort');
            setMascotSpeech("Ối! Trả lời chưa chính xác rồi, cẩn thận đòn phản công của Boss!");

            if (q) {
                const chosenOrig = (currentBossIndices && currentBossIndices[optIdx] !== undefined) ? currentBossIndices[optIdx] : optIdx;
                wrongQuestionsLog.push({
                    q: q.q,
                    chosen: (q.opts && q.opts[chosenOrig]) ? q.opts[chosenOrig] : "Phương án đã chọn",
                    correct: (q.opts && q.opts[q.c]) ? q.opts[q.c] : "Đáp án đúng",
                    round: 'Vòng 3: Đại Chiến Boss'
                });
            }
        }

        bossIdx++;
        document.querySelectorAll('.btn-mcq-opt').forEach(b => b.disabled = true);
        setTimeout(() => {
            if (bossAvatar) bossAvatar.classList.remove('hit');
            bossAnswering = false;
            renderBossQuestion();
        }, 850);
    } catch (err) {
        console.error('Error in checkBossAnswer:', err);
        bossAnswering = false;
    }
}

// 13. CẬP NHẬT GIAO DIỆN & LƯU ĐIỂM FIREBASE
function updateScoreUI() {
    document.getElementById('current-score').innerText = score;
}

function updateLivesUI() {
    let hearts = "❤️".repeat(Math.max(0, lives)) + "🖤".repeat(Math.max(0, 3 - lives));
    document.getElementById('lives-display').innerText = hearts;
}

function finishExam() {
    if (examFinished) return;
    examFinished = true;
    isPlaying = false;

    playAudioTone('victory');

    document.getElementById('game-playground').classList.add('hidden');
    document.getElementById('mascot-container').classList.add('hidden');
    const fab = document.getElementById('scratchpad-fab');
    if (fab) fab.classList.add('hidden');

    document.getElementById('result-overlay').classList.remove('hidden');
    document.getElementById('final-score').innerText = score;

    // Nút xem lời giải chi tiết cho các câu sai
    const reviewBtn = document.getElementById('btn-show-review');
    const wrongCountSpan = document.getElementById('wrong-count-badge');
    if (wrongQuestionsLog.length > 0) {
        if (wrongCountSpan) wrongCountSpan.innerText = wrongQuestionsLog.length;
        if (reviewBtn) reviewBtn.classList.remove('hidden');
    } else {
        if (reviewBtn) reviewBtn.classList.add('hidden');
    }

    const durationSec = Math.max(1, Math.floor((Date.now() - startTime) / 1000));

    let souvenirEarned = "Chưa đạt phần thưởng (Cần từ 50 điểm)";
    if (WEEK_DATA && WEEK_DATA.souvenirs) {
        if (score >= 100) souvenirEarned = WEEK_DATA.souvenirs.cap3;
        else if (score >= 90) souvenirEarned = WEEK_DATA.souvenirs.cap2;
        else if (score >= 50) souvenirEarned = WEEK_DATA.souvenirs.cap1;
    }
    document.getElementById('souvenir-badge').innerText = souvenirEarned;

    if (score >= 90 && typeof launchFireworks === 'function') {
        launchFireworks();
    }

    try {
        const prevBest = parseInt(localStorage.getItem(`bestScore_Tuan_${currentWeek}`) || '0', 10);
        localStorage.setItem(`bestScore_Tuan_${currentWeek}`, Math.max(score, prevBest));
        localStorage.setItem('lastCompletedWeek', currentWeek);
        localStorage.setItem('lastCompletedScore', score);
    } catch(e) {}

    if (db) {
        const now = new Date();
        const dateStr = now.toLocaleDateString('vi-VN') + ' ' + now.toLocaleTimeString('vi-VN');

        const scorePayload = {
            username: savedUsername || "guest_" + Math.random().toString(36).substring(7),
            fullName: savedName || "Khách Vãng Lai",
            name: savedName || "Khách Vãng Lai",
            className: savedClass || "5",
            class: savedClass || "5",
            schoolName: savedSchool || "Tự Do",
            role: savedRole || "guest",
            status: savedStatus || "approved",
            score: score,
            duration: durationSec,
            attempt: studentAttempt,
            souvenir: souvenirEarned,
            date: dateStr,
            timestamp: firebase.database.ServerValue.TIMESTAMP
        };

        db.ref(`scores/Tuan_${currentWeek}`).push(scorePayload)
            .then(() => {
                document.getElementById('save-status-msg').innerText = "✅ Đã lưu kết quả thành công lên Bảng Vàng!";
            })
            .catch(() => {
                document.getElementById('save-status-msg').innerText = "⚠️ Không thể kết nối máy chủ để lưu điểm.";
            });

        // Đồng bộ điểm và hoạt động mới nhất vào hồ sơ người dùng
        if (savedUsername && savedUsername !== 'guest' && !savedUsername.startsWith('guest_')) {
            db.ref(`users/${savedUsername}`).update({
                lastScore: score,
                lastActiveWeek: currentWeek,
                lastPlayedAt: firebase.database.ServerValue.TIMESTAMP
            }).catch(() => {});
        }
    } else {
        document.getElementById('save-status-msg').innerText = "Chế độ chơi ngoại tuyến (Offline).";
    }
}

// 14. RƯƠNG BÁU CHIẾN THẮNG (VICTORY LOOT BOX)
function showLootBox() {
    const lootOverlay = document.getElementById('loot-overlay');
    if (!lootOverlay) {
        finishExam();
        return;
    }

    document.getElementById('game-playground').classList.add('hidden');
    document.getElementById('mascot-container').classList.add('hidden');
    const fab = document.getElementById('scratchpad-fab');
    if (fab) fab.classList.add('hidden');

    lootOverlay.classList.remove('hidden');

    const stationName = (WEEK_DATA && WEEK_DATA.stationName) ? WEEK_DATA.stationName : "Việt Nam";
    let title = `Nhà Thám Hiểm ${stationName}`;
    if (score >= 100) title = `Đại Hiệp Sĩ ${stationName}`;
    else if (score >= 90) title = `Dũng Sĩ Chinh Phục ${stationName}`;
    else if (score >= 50) title = `Nhà Thám Hiểm Trẻ ${stationName}`;

    let souvenir = "Huy hiệu Chiến binh";
    if (WEEK_DATA && WEEK_DATA.souvenirs) {
        if (score >= 100) souvenir = WEEK_DATA.souvenirs.cap3;
        else if (score >= 90) souvenir = WEEK_DATA.souvenirs.cap2;
        else if (score >= 50) souvenir = WEEK_DATA.souvenirs.cap1;
    }

    const titleEl = document.getElementById('reward-title');
    const souvEl = document.getElementById('reward-souvenir');
    if (titleEl) titleEl.innerText = title;
    if (souvEl) souvEl.innerText = souvenir;

    const chestIcon = document.getElementById('loot-chest-icon');
    if (chestIcon) {
        chestIcon.className = 'loot-chest-icon';
        chestIcon.innerText = '🎁';
    }
    const rewardContent = document.getElementById('loot-reward-content');
    if (rewardContent) rewardContent.classList.add('hidden');

    const openBtn = document.getElementById('loot-open-btn');
    if (openBtn) openBtn.classList.remove('hidden');

    const continueBtn = document.getElementById('loot-continue-btn');
    if (continueBtn) continueBtn.classList.add('hidden');

    playAudioTone('victory');
}

function handleOpenLootChest() {
    const chestIcon = document.getElementById('loot-chest-icon');
    if (chestIcon) {
        chestIcon.classList.add('opened');
        chestIcon.innerText = '💎';
    }
    playAudioTone('chest-open');

    if (typeof launchFireworks === 'function') {
        launchFireworks();
    }

    const rewardContent = document.getElementById('loot-reward-content');
    if (rewardContent) rewardContent.classList.remove('hidden');

    const openBtn = document.getElementById('loot-open-btn');
    if (openBtn) openBtn.classList.add('hidden');

    const continueBtn = document.getElementById('loot-continue-btn');
    if (continueBtn) continueBtn.classList.remove('hidden');
}

function handleLootContinue() {
    const lootOverlay = document.getElementById('loot-overlay');
    if (lootOverlay) lootOverlay.classList.add('hidden');
    finishExam();
}

// 15. MODAL ÔN TẬP & XEM LỜI GIẢI CHI TIẾT
function openReviewModal() {
    const reviewOverlay = document.getElementById('review-overlay');
    const reviewList = document.getElementById('review-list');
    if (!reviewOverlay || !reviewList) return;

    reviewList.innerHTML = '';
    if (wrongQuestionsLog.length === 0) {
        reviewList.innerHTML = `
            <div style="text-align:center; padding:28px 16px; color:#34d399; font-weight:700; font-size:1.05rem;">
                🎉 Bạn không làm sai câu nào cả! Kiến thức toán học của bạn thật xuất sắc!
            </div>
        `;
    } else {
        wrongQuestionsLog.forEach((item, idx) => {
            const guide = generatePedagogicalGuide(item.q, item.correct);
            const card = document.createElement('div');
            card.className = 'review-item-card';
            card.innerHTML = `
                <div style="font-size:0.75rem; color:#94a3b8; font-weight:700; text-transform:uppercase;">${item.round} • Câu ${idx + 1}</div>
                <div class="review-item-q">${item.q}</div>
                <div class="review-item-row wrong">
                    <span>❌ Bạn đã chọn:</span>
                    <b>${item.chosen}</b>
                </div>
                <div class="review-item-row correct">
                    <span>✔️ Đáp án chính xác:</span>
                    <b>${item.correct}</b>
                </div>
                <div class="review-item-guide">
                    ${guide}
                </div>
            `;
            reviewList.appendChild(card);
        });
    }

    reviewOverlay.classList.remove('hidden');
}

function closeReviewModal() {
    const reviewOverlay = document.getElementById('review-overlay');
    if (reviewOverlay) reviewOverlay.classList.add('hidden');
}
