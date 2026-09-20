const fs = require('fs');

function generateSmartDistractors(q, a, bank, allBank) {
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

    // 1. Variable equation: x = ... or y = ...
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

    // 2. Geometric & Physics Formulas (S =, C =, V =, h =, t =, v =, Sxq, Stp)
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

    // 3. Paired fractions: N1/D1 và N2/D2
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

    // 4. Single fraction: N/D or N/D (hoặc X)
    if (distractors.size < 3) {
        const fracMatch = a.match(/^(\d+)\s*\/\s*(\d+)(.*)$/);
        if (fracMatch && !a.includes('và')) {
            const n = parseInt(fracMatch[1]);
            const d = parseInt(fracMatch[2]);
            if (n !== d && d !== 0) {
                add(`${d}/${n}`); // Inverted
                if (d > n) add(`${d - n}/${d}`); // Complement
                if (n > 1) add(`${n - 1}/${d}`);
                add(`${n + 1}/${d}`);
                if (d > 2) add(`${n}/${d - 1}`);
                add(`${n}/${d + 1}`);
                add(`${n + 1}/${d + 1}`);
                add(`${n * 2}/${d * 2 + 1}`);
            }
        }
    }

    // 5. Mixed numbers: W N/D
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

    // 6. Word comparison / relations / reading of numbers
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

    // 7. Place values (Hàng...)
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

    // 8. Percentages: e.g. 100%, 50%, 25%, 30%
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

    // 9. Expressions with comparison: X > Y or X < Y or X = Y
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

    // 10. Number with unit: <Number> <Unit>
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

    // 11. Pure numbers (integers, spaced numbers, decimals)
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

    // 12. Thematic text pool (Provinces, Landmarks, Waterways)
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

    // 13. Bank fallback: Search bank for items with identical type/pattern
    if (distractors.size < 3 && bank && Array.isArray(bank)) {
        // Step 1: match exact pattern
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

        // Step 2: match similar digit/non-digit profile
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

        // Step 3: general fallback from bank
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

    // Step 4: If still < 3, pull from allBank
    if (distractors.size < 3 && allBank && Array.isArray(allBank)) {
        allBank.forEach(item => {
            if (distractors.size >= 3) return;
            const itemA = (item.a || item).trim();
            if (itemA.toLowerCase() !== a.toLowerCase()) {
                add(itemA);
            }
        });
    }

    return Array.from(distractors).slice(0, 3);
}

module.exports = { generateSmartDistractors };
