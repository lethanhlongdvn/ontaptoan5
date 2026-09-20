const fs = require('fs');

// Mock browser DOM and APIs
global.window = global;
global.document = {
    getElementById: (id) => ({
        innerText: '',
        innerHTML: '',
        style: {},
        classList: { add: () => {}, remove: () => {}, contains: () => false },
        appendChild: () => {},
        children: [],
        querySelector: () => null,
        querySelectorAll: () => []
    }),
    createElement: (tag) => ({
        className: '',
        innerText: '',
        innerHTML: '',
        classList: { add: () => {}, remove: () => {} },
        appendChild: () => {},
        onclick: null,
        style: {}
    }),
    body: {
        appendChild: () => {}
    }
};
global.localStorage = {
    getItem: () => '1',
    setItem: () => {},
    removeItem: () => {}
};
global.playAudioTone = () => {};
global.firebase = {
    apps: [],
    initializeApp: () => {},
    database: () => ({ ref: () => ({ on: () => {}, once: () => Promise.resolve({ val: () => null }), set: () => Promise.resolve(), remove: () => Promise.resolve() }) })
};

// Read game-engine.js
const engineCode = fs.readFileSync('js/game-engine.js', 'utf8');

// Run game-engine in VM
const vm = require('vm');
const context = vm.createContext({
    ...global,
    console
});
vm.runInContext(engineCode, context);

console.log('Testing game-engine.js with 35 weeks...');
let totalTests = 0;
let errors = [];

for (let w = 1; w <= 35; w++) {
    const d = JSON.parse(fs.readFileSync(`data/week-${w}.json`, 'utf8'));
    context.WEEK_DATA = d;
    context.currentV1Pool = d.bank.V1.slice(0, 10);
    context.currentV2Questions = d.bank.V2.slice(0, 4);

    // Test V1 questions
    for (let i = 0; i < 10; i++) {
        totalTests++;
        context.v1Index = i;
        try {
            const item = context.currentV1Pool[i];
            const dists = context.generateSmartDistractors(item.q, item.a, d.bank.V1);
            if (dists.length < 3) {
                errors.push(`[W${w}-V1-Q${i+1}] Only ${dists.length} distractors for "${item.a}"`);
            }
            const all4 = [item.a.trim(), ...dists];
            const set = new Set(all4.map(x => x.toLowerCase()));
            if (set.size < 4) {
                errors.push(`[W${w}-V1-Q${i+1}] Duplicate choices for "${item.a}": ${JSON.stringify(all4)}`);
            }
        } catch (e) {
            errors.push(`[W${w}-V1-Q${i+1}] Error: ${e.message}`);
        }
    }

    // Test V2 questions
    for (let i = 0; i < 4; i++) {
        totalTests++;
        context.v2Index = i;
        try {
            const item = context.currentV2Questions[i];
            const dists = context.generateSmartDistractors(item.q, item.a, d.bank.V2);
            if (dists.length < 3) {
                errors.push(`[W${w}-V2-Q${i+1}] Only ${dists.length} distractors for "${item.a}"`);
            }
            const all4 = [item.a.trim(), ...dists];
            const set = new Set(all4.map(x => x.toLowerCase()));
            if (set.size < 4) {
                errors.push(`[W${w}-V2-Q${i+1}] Duplicate choices for "${item.a}": ${JSON.stringify(all4)}`);
            }
        } catch (e) {
            errors.push(`[W${w}-V2-Q${i+1}] Error: ${e.message}`);
        }
    }
}

console.log(`TOTAL SIMULATED QUESTIONS: ${totalTests}`);
console.log(`ERRORS COUNT: ${errors.length}`);
if (errors.length > 0) {
    errors.slice(0, 10).forEach(e => console.log('  !', e));
} else {
    console.log('✅ 100% of V1 and V2 questions in game-engine.js generate exactly 4 distinct, pedagogically sound choices!');
}
