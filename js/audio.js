// ==========================================
// BỘ TỔNG HỢP ÂM THANH SỐNG ĐỘNG (WEB AUDIO API)
// Âm thanh vui tươi, phong phú, kích thích hứng thú cho học sinh
// ==========================================

let audioCtx = null;

function getAudioCtx() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    return audioCtx;
}

function playAudioTone(type) {
    try {
        const ctx = getAudioCtx();
        const now = ctx.currentTime;

        // Chuẩn hóa tham số (hỗ trợ cả boolean true/false cũ lẫn chuỗi loại âm thanh mới)
        let mode = type;
        if (type === true) mode = 'success';
        if (type === false) mode = 'error';

        if (mode === 'combo') {
            // Âm thanh Combo Streak vui tươi (Arpeggio thăng hoa G5 -> C6 -> E6)
            [783.99, 1046.50, 1318.51].forEach((freq, idx) => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(freq, now + idx * 0.08);
                gain.gain.setValueAtTime(0.25, now + idx * 0.08);
                gain.gain.exponentialRampToValueAtTime(0.01, now + idx * 0.08 + 0.25);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now + idx * 0.08);
                osc.stop(now + idx * 0.08 + 0.25);
                osc.onended = () => { osc.disconnect(); gain.disconnect(); };
            });
        } else if (mode === 'success') {
            // Âm thanh Trả lời đúng (Chime ấm áp C5 -> G5)
            [523.25, 783.99].forEach((freq, idx) => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(freq, now + idx * 0.1);
                gain.gain.setValueAtTime(0.22, now + idx * 0.1);
                gain.gain.exponentialRampToValueAtTime(0.01, now + idx * 0.1 + 0.22);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now + idx * 0.1);
                osc.stop(now + idx * 0.1 + 0.22);
                osc.onended = () => { osc.disconnect(); gain.disconnect(); };
            });
        } else if (mode === 'step') {
            // Âm thanh RoBot leo nấc thang (2 nốt thăng hoa vui vẻ F5 -> A5)
            [698.46, 880.00].forEach((freq, idx) => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(freq, now + idx * 0.09);
                gain.gain.setValueAtTime(0.25, now + idx * 0.09);
                gain.gain.exponentialRampToValueAtTime(0.01, now + idx * 0.09 + 0.18);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now + idx * 0.09);
                osc.stop(now + idx * 0.09 + 0.18);
                osc.onended = () => { osc.disconnect(); gain.disconnect(); };
            });
        } else if (mode === 'boss-hit') {
            // Đòn đánh trúng Boss (Tia laser giáng xuống)
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(880, now);
            osc.frequency.exponentialRampToValueAtTime(120, now + 0.3);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(now);
            osc.stop(now + 0.3);
            osc.onended = () => { osc.disconnect(); gain.disconnect(); };
        } else if (mode === 'victory' || mode === 'chest-open') {
            // Chiến thắng Boss & Mở Rương Báu (Fanfare vinh quang)
            [523.25, 659.25, 783.99, 1046.50, 1318.51].forEach((freq, idx) => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(freq, now + idx * 0.1);
                gain.gain.setValueAtTime(0.22, now + idx * 0.1);
                gain.gain.exponentialRampToValueAtTime(0.01, now + idx * 0.1 + 0.35);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now + idx * 0.1);
                osc.stop(now + idx * 0.1 + 0.35);
                osc.onended = () => { osc.disconnect(); gain.disconnect(); };
            });
        } else if (mode === 'scratch') {
            // Tiếng sột soạt vẽ nháp cực êm
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(450, now);
            osc.frequency.exponentialRampToValueAtTime(320, now + 0.05);
            gain.gain.setValueAtTime(0.05, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(now);
            osc.stop(now + 0.05);
            osc.onended = () => { osc.disconnect(); gain.disconnect(); };
        } else {
            // Trả lời sai (Âm trầm vui nhộn nhẹ nhàng, không gây ức chế)
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(220, now);
            osc.frequency.exponentialRampToValueAtTime(110, now + 0.22);
            gain.gain.setValueAtTime(0.2, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.22);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(now);
            osc.stop(now + 0.22);
            osc.onended = () => { osc.disconnect(); gain.disconnect(); };
        }
    } catch (e) {
        // Trình duyệt không hỗ trợ âm thanh
    }
}
