/**
 * ====================================================================
 * EDUBOT-BTCT5: ANTIGRAVITY PARTICLE SYSTEM & CELEBRATION ENGINE
 * Tích hợp công nghệ hoạt họa không trọng lực (Google Antigravity style)
 * Tối ưu GPU (Sprite Caching, Canvas Desynchronized) cho Mobile & Desktop
 * Hỗ trợ 2 chế độ:
 *  1. Celebration / Fireworks (Bùng nổ ăn mừng chiến thắng / mở rương)
 *  2. Ambient Background (Hiệu ứng nền không gian vũ trụ toán học lơ lửng)
 * ====================================================================
 */

(function (window) {
    'use strict';

    // Bảng màu chuẩn EduBot & Gamification
    const DEFAULT_COLORS = [
        '#FF9800', // Cam Robot EduBot
        '#00E5FF', // Xanh Cyan Neon
        '#FFD700', // Vàng Vương Miện Gold
        '#10B981', // Ngọc Lục Bảo Success
        '#8B5CF6', // Tím Vũ Trụ
        '#F43F5E', // Đỏ Hồng Năng Lượng
        '#FFFFFF'  // Trắng Tinh Khiết
    ];

    // Bộ nhớ cache sprites hình khối để tối ưu hóa GPU (không phải vẽ lại path/shadow mỗi frame)
    const spriteCache = {};

    function getSprite(color, shapeType) {
        const key = `${color}_${shapeType}`;
        if (spriteCache[key]) return spriteCache[key];

        const size = 64; // Độ phân giải sprite sắc nét
        const center = size / 2;
        const drawSize = 28;

        const c = document.createElement('canvas');
        c.width = size;
        c.height = size;
        const cx = c.getContext('2d');

        // Đổ bóng phát sáng viền hạt (Bake Shadow/Glow)
        cx.shadowColor = color;
        cx.shadowBlur = 12;
        cx.shadowOffsetX = 0;
        cx.shadowOffsetY = 0;
        cx.fillStyle = color;
        cx.strokeStyle = color;
        cx.lineWidth = 4;
        cx.lineCap = 'round';
        cx.lineJoin = 'round';

        cx.translate(center, center);
        cx.beginPath();

        switch (shapeType) {
            case 0: // Tròn (Circle)
                cx.arc(0, 0, drawSize / 2, 0, Math.PI * 2);
                cx.fill();
                break;

            case 1: // Vuông (Square)
                cx.rect(-drawSize / 2, -drawSize / 2, drawSize, drawSize);
                cx.fill();
                break;

            case 2: // Tam giác (Triangle)
                cx.moveTo(0, -drawSize / 2);
                cx.lineTo(drawSize / 2, drawSize / 2);
                cx.lineTo(-drawSize / 2, drawSize / 2);
                cx.closePath();
                cx.fill();
                break;

            case 3: // Ngôi sao 5 cánh (Star ★)
                const points = 5;
                const outer = drawSize / 2;
                const inner = outer / 2.2;
                for (let i = 0; i < points * 2; i++) {
                    const r = (i % 2 === 0) ? outer : inner;
                    const angle = (i * Math.PI) / points - Math.PI / 2;
                    const x = Math.cos(angle) * r;
                    const y = Math.sin(angle) * r;
                    if (i === 0) cx.moveTo(x, y);
                    else cx.lineTo(x, y);
                }
                cx.closePath();
                cx.fill();
                break;

            case 4: // Phép cộng (+)
                const plusLen = drawSize / 2.2;
                cx.moveTo(-plusLen, 0); cx.lineTo(plusLen, 0);
                cx.moveTo(0, -plusLen); cx.lineTo(0, plusLen);
                cx.stroke();
                break;

            case 5: // Phép nhân (×)
                const crossLen = drawSize / 2.4;
                cx.moveTo(-crossLen, -crossLen); cx.lineTo(crossLen, crossLen);
                cx.moveTo(crossLen, -crossLen); cx.lineTo(-crossLen, crossLen);
                cx.stroke();
                break;

            case 6: // Kim cương / Hình thoi (Diamond ◆)
                cx.moveTo(0, -drawSize / 1.8);
                cx.lineTo(drawSize / 2, 0);
                cx.lineTo(0, drawSize / 1.8);
                cx.lineTo(-drawSize / 2, 0);
                cx.closePath();
                cx.fill();
                break;

            default:
                cx.arc(0, 0, drawSize / 2, 0, Math.PI * 2);
                cx.fill();
                break;
        }

        spriteCache[key] = c;
        return c;
    }

    // ==============================================================
    // 1. CELEBRATION ENGINE (ĂN MỪNG CHIẾN THẮNG & MỞ RƯƠNG)
    // ==============================================================
    class AntigravityEngine {
        constructor() {
            this.canvas = null;
            this.ctx = null;
            this.particles = [];
            this.animId = null;
            this.width = window.innerWidth;
            this.height = window.innerHeight;
            this.dpr = window.devicePixelRatio || 1;
            this.mouse = { x: -9999, y: -9999, radius: 140 };
            this.active = false;
            this.autoStopTimer = null;
            this.mode = 'celebration'; // 'celebration' | 'pattern'

            this.boundResize = this.resize.bind(this);
            this.boundMouseMove = this.onMouseMove.bind(this);
            this.boundTouchMove = this.onTouchMove.bind(this);
        }

        ensureCanvas() {
            if (!this.canvas) {
                this.canvas = document.getElementById('fireworks-canvas') || document.getElementById('antigravity-canvas');
                if (!this.canvas) {
                    this.canvas = document.createElement('canvas');
                    this.canvas.id = 'antigravity-canvas';
                    document.body.appendChild(this.canvas);
                }
            }

            Object.assign(this.canvas.style, {
                position: 'fixed',
                top: '0',
                left: '0',
                width: '100%',
                height: '100%',
                pointerEvents: 'none',
                zIndex: '10000',
                display: 'block'
            });

            this.ctx = this.canvas.getContext('2d', {
                alpha: true,
                desynchronized: true,
                willReadFrequently: false
            });

            this.resize();
            window.removeEventListener('resize', this.boundResize);
            window.addEventListener('resize', this.boundResize);

            window.removeEventListener('mousemove', this.boundMouseMove);
            window.addEventListener('mousemove', this.boundMouseMove);
            window.removeEventListener('touchmove', this.boundTouchMove);
            window.addEventListener('touchmove', this.boundTouchMove, { passive: true });
        }

        resize() {
            if (!this.canvas || !this.ctx) return;
            this.dpr = window.devicePixelRatio || 1;
            this.width = window.innerWidth;
            this.height = window.innerHeight;

            this.canvas.width = this.width * this.dpr;
            this.canvas.height = this.height * this.dpr;
            this.ctx.scale(this.dpr, this.dpr);
            this.ctx.imageSmoothingEnabled = true;
            this.ctx.imageSmoothingQuality = 'high';
        }

        onMouseMove(e) {
            this.mouse.x = e.clientX;
            this.mouse.y = e.clientY;
        }

        onTouchMove(e) {
            if (e.touches && e.touches.length > 0) {
                this.mouse.x = e.touches[0].clientX;
                this.mouse.y = e.touches[0].clientY;
            }
        }

        burst(options = {}) {
            this.ensureCanvas();
            this.mode = options.mode || 'celebration';
            this.active = true;

            const count = options.count || (window.innerWidth < 600 ? 55 : 85);
            const originX = options.x !== undefined ? options.x : this.width / 2;
            const originY = options.y !== undefined ? options.y : this.height * 0.45;
            const colors = options.colors || DEFAULT_COLORS;

            this.particles = [];

            for (let i = 0; i < count; i++) {
                const angle = Math.random() * Math.PI * 2;
                const speed = (Math.random() * 8 + 3) * (options.power || 1.2);
                const color = colors[Math.floor(Math.random() * colors.length)];
                const shapeType = Math.floor(Math.random() * 7); // 0..6
                const sprite = getSprite(color, shapeType);

                this.particles.push({
                    x: originX + (Math.random() - 0.5) * 40,
                    y: originY + (Math.random() - 0.5) * 40,
                    vx: Math.cos(angle) * speed,
                    vy: Math.sin(angle) * speed - 2,
                    rotation: Math.random() * Math.PI * 2,
                    rotationSpeed: (Math.random() - 0.5) * 0.08,
                    visualSize: Math.random() * 14 + 10,
                    color: color,
                    sprite: sprite,
                    shapeType: shapeType,
                    alpha: 1.0,
                    friction: 0.94,
                    antigravity: -0.06,
                    wobble: Math.random() * Math.PI * 2,
                    wobbleSpeed: Math.random() * 0.05 + 0.02,
                    patternTarget: null,
                    life: 1.0,
                    decay: Math.random() * 0.003 + 0.002
                });
            }

            if (this.mode === 'pattern') {
                const r = Math.min(this.width, this.height) * 0.32;
                this.particles.forEach((p, idx) => {
                    const pAngle = (idx / count) * Math.PI * 2;
                    p.patternTarget = {
                        x: originX + Math.cos(pAngle) * r,
                        y: originY + Math.sin(pAngle) * r
                    };
                });
            }

            if (!this.animId) {
                this.loop();
            }

            if (this.autoStopTimer) clearTimeout(this.autoStopTimer);
            const duration = options.duration || 9000;
            this.autoStopTimer = setTimeout(() => {
                this.stop();
            }, duration);
        }

        loop() {
            if (!this.active) {
                if (this.ctx && this.canvas) {
                    this.ctx.clearRect(0, 0, this.width, this.height);
                }
                this.animId = null;
                return;
            }

            this.ctx.clearRect(0, 0, this.width, this.height);

            for (let i = 0; i < this.particles.length; i++) {
                const p = this.particles[i];

                if (p.patternTarget && this.mode === 'pattern') {
                    const dx = p.patternTarget.x - p.x;
                    const dy = p.patternTarget.y - p.y;
                    p.vx += dx * 0.025;
                    p.vy += dy * 0.025;
                    p.vx *= 0.88;
                    p.vy *= 0.88;
                } else {
                    p.vx *= p.friction;
                    p.vy *= p.friction;
                    p.vy += p.antigravity;

                    p.wobble += p.wobbleSpeed;
                    p.x += Math.sin(p.wobble) * 0.8;
                }

                // Tương tác chuột / cảm ứng
                const dxMouse = p.x - this.mouse.x;
                const dyMouse = p.y - this.mouse.y;
                const distMouse = Math.sqrt(dxMouse * dxMouse + dyMouse * dyMouse);
                if (distMouse < this.mouse.radius && distMouse > 0) {
                    const force = (1 - distMouse / this.mouse.radius) * 4;
                    p.vx += (dxMouse / distMouse) * force;
                    p.vy += (dyMouse / distMouse) * force;
                }

                p.x += p.vx;
                p.y += p.vy;
                p.rotation += p.rotationSpeed;

                p.life -= p.decay;
                p.alpha = Math.max(0, p.life);

                if (p.alpha > 0.01) {
                    this.ctx.save();
                    this.ctx.globalAlpha = p.alpha;
                    this.ctx.translate(p.x, p.y);
                    this.ctx.rotate(p.rotation);
                    const drawSize = p.visualSize;
                    this.ctx.drawImage(p.sprite, -drawSize / 2, -drawSize / 2, drawSize, drawSize);
                    this.ctx.restore();
                }

                if (p.life <= 0 || p.y < -80) {
                    this.particles.splice(i, 1);
                    i--;
                }
            }

            if (this.particles.length === 0) {
                this.stop();
                return;
            }

            this.animId = requestAnimationFrame(this.loop.bind(this));
        }

        stop() {
            this.active = false;
            if (this.animId) {
                cancelAnimationFrame(this.animId);
                this.animId = null;
            }
            if (this.ctx && this.canvas) {
                this.ctx.clearRect(0, 0, this.width, this.height);
                this.canvas.style.display = 'none';
            }
        }
    }

    // ==============================================================
    // 2. AMBIENT BACKGROUND ENGINE (NỀN VŨ TRỤ TOÁN HỌC LƠ LỬNG)
    // ==============================================================
    class AmbientAntigravityEngine {
        constructor(canvasOrId, options = {}) {
            this.canvas = typeof canvasOrId === 'string' ? document.getElementById(canvasOrId) : canvasOrId;
            if (!this.canvas) return;

            this.options = Object.assign({
                count: window.innerWidth < 600 ? 25 : 45,
                speed: 0.45,
                colors: DEFAULT_COLORS,
                opacity: 0.5
            }, options);

            this.ctx = this.canvas.getContext('2d', {
                alpha: true,
                desynchronized: true,
                willReadFrequently: false
            });

            this.particles = [];
            this.mouse = { x: -9999, y: -9999, radius: 130 };
            this.animId = null;
            this.width = window.innerWidth;
            this.height = window.innerHeight;

            this.init();
        }

        init() {
            this.resize();
            window.addEventListener('resize', () => this.resize());
            window.addEventListener('mousemove', (e) => {
                const rect = this.canvas.getBoundingClientRect();
                this.mouse.x = e.clientX - rect.left;
                this.mouse.y = e.clientY - rect.top;
            });
            window.addEventListener('touchmove', (e) => {
                if (e.touches && e.touches[0]) {
                    const rect = this.canvas.getBoundingClientRect();
                    this.mouse.x = e.touches[0].clientX - rect.left;
                    this.mouse.y = e.touches[0].clientY - rect.top;
                }
            }, { passive: true });

            this.particles = [];
            for (let i = 0; i < this.options.count; i++) {
                const color = this.options.colors[Math.floor(Math.random() * this.options.colors.length)];
                const shapeType = Math.floor(Math.random() * 7);
                this.particles.push({
                    x: Math.random() * this.width,
                    y: Math.random() * this.height,
                    vx: (Math.random() - 0.5) * 0.35,
                    vy: -(Math.random() * 0.45 + 0.15) * this.options.speed,
                    rotation: Math.random() * Math.PI * 2,
                    rotationSpeed: (Math.random() - 0.5) * 0.015,
                    visualSize: Math.random() * 12 + 8,
                    color: color,
                    sprite: getSprite(color, shapeType),
                    alpha: (Math.random() * 0.35 + 0.15) * this.options.opacity,
                    wobble: Math.random() * Math.PI * 2,
                    wobbleSpeed: Math.random() * 0.02 + 0.008
                });
            }

            this.loop();
        }

        resize() {
            if (!this.canvas || !this.ctx) return;
            const dpr = window.devicePixelRatio || 1;
            const rect = this.canvas.getBoundingClientRect();
            this.width = rect.width || window.innerWidth;
            this.height = rect.height || window.innerHeight;
            this.canvas.width = this.width * dpr;
            this.canvas.height = this.height * dpr;
            this.ctx.scale(dpr, dpr);
            this.ctx.imageSmoothingEnabled = true;
            this.ctx.imageSmoothingQuality = 'high';
        }

        loop() {
            this.ctx.clearRect(0, 0, this.width, this.height);

            for (let i = 0; i < this.particles.length; i++) {
                const p = this.particles[i];

                p.wobble += p.wobbleSpeed;
                p.x += p.vx + Math.sin(p.wobble) * 0.4;
                p.y += p.vy;
                p.rotation += p.rotationSpeed;

                // Chuột dạt hạt né tránh
                const dx = p.x - this.mouse.x;
                const dy = p.y - this.mouse.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < this.mouse.radius && dist > 0) {
                    const force = (1 - dist / this.mouse.radius) * 2;
                    p.x += (dx / dist) * force;
                    p.y += (dy / dist) * force;
                }

                // Cuộn biên tuần hoàn (bay hết lên đỉnh thì trở về đáy)
                if (p.y < -40) {
                    p.y = this.height + 20;
                    p.x = Math.random() * this.width;
                }
                if (p.x < -40) p.x = this.width + 30;
                if (p.x > this.width + 40) p.x = -30;

                this.ctx.save();
                this.ctx.globalAlpha = p.alpha;
                this.ctx.translate(p.x, p.y);
                this.ctx.rotate(p.rotation);
                const s = p.visualSize;
                this.ctx.drawImage(p.sprite, -s / 2, -s / 2, s, s);
                this.ctx.restore();
            }

            this.animId = requestAnimationFrame(this.loop.bind(this));
        }

        stop() {
            if (this.animId) {
                cancelAnimationFrame(this.animId);
                this.animId = null;
            }
            if (this.ctx && this.canvas) {
                this.ctx.clearRect(0, 0, this.width, this.height);
            }
        }
    }

    // Singleton Engine instance cho Celebration
    const celebrationEngine = new AntigravityEngine();

    // Xuất API toàn cục
    window.EduAntigravity = {
        burst: (options) => {
            if (celebrationEngine.canvas) celebrationEngine.canvas.style.display = 'block';
            celebrationEngine.burst(options);
        },
        pattern: (options = {}) => {
            if (celebrationEngine.canvas) celebrationEngine.canvas.style.display = 'block';
            celebrationEngine.burst(Object.assign({ mode: 'pattern', count: 65, duration: 12000 }, options));
        },
        startAmbient: (canvasOrId, options) => {
            return new AmbientAntigravityEngine(canvasOrId, options);
        },
        stop: () => celebrationEngine.stop()
    };

    // Định nghĩa hàm launchFireworks chuẩn mực cho game-engine.js
    window.launchFireworks = function (options = {}) {
        const chest = document.getElementById('loot-chest-icon');
        let originX, originY;
        if (chest) {
            const rect = chest.getBoundingClientRect();
            originX = rect.left + rect.width / 2;
            originY = rect.top + rect.height / 2;
        }

        window.EduAntigravity.burst(Object.assign({
            x: originX,
            y: originY,
            count: window.innerWidth < 600 ? 60 : 90,
            power: 1.3,
            duration: 9000
        }, options));
    };

    // Tương thích ngược
    if (!window.startFireworks) {
        window.startFireworks = window.launchFireworks;
    }

    // Tự động kích hoạt Ambient nếu trang có thẻ #bg-antigravity
    function autoInitAmbient() {
        const ambientEl = document.getElementById('bg-antigravity') || document.querySelector('canvas[data-antigravity="ambient"]');
        if (ambientEl) {
            window.EduAntigravity.startAmbient(ambientEl);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', autoInitAmbient);
    } else {
        autoInitAmbient();
    }

})(window);
