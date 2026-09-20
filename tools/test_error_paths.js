const fs = require('fs');
const vm = require('vm');

global.window = global;
global.document = {
    getElementById: (id) => ({
        innerText: '',
        innerHTML: '',
        style: {},
        classList: { add: () => {}, remove: () => {}, contains: () => false },
        appendChild: () => {},
        children: [],
        querySelector: () => ({ innerText: '' }),
        querySelectorAll: () => []
    }),
    querySelectorAll: () => [],
    createElement: (tag) => ({
        className: '',
        innerText: '',
        innerHTML: '',
        classList: { add: () => {}, remove: () => {} },
        appendChild: () => {},
        onclick: null,
        style: {}
    }),
    body: { appendChild: () => {} }
};
global.localStorage = { getItem: () => '1', setItem: () => {}, removeItem: () => {} };
global.playAudioTone = () => {};
global.firebase = { 
    apps: [], 
    initializeApp: () => {}, 
    database: Object.assign(() => ({ ref: () => ({ on: () => {}, once: () => Promise.resolve({ val: () => null }), push: () => Promise.resolve(), update: () => Promise.resolve() }) }), {
        ServerValue: { TIMESTAMP: Date.now() }
    })
};

const engineCode = fs.readFileSync('js/game-engine.js', 'utf8');
const ctx = vm.createContext({ ...global, console });
vm.runInContext(engineCode, ctx);

vm.runInContext(`
currentV1Pool = [{ q: 'Số tự nhiên lớn nhất có 6 chữ số khác nhau', a: '987 654' }];
v1Index = 0;
lives = 3;
isProcessingV1 = false;
console.log('Testing V1 WRONG answer...');
handleV1OptionClick('987 645', '987 654', document.createElement('div'), {});
console.log('V1 wrong answer handled successfully! Wrong log count:', wrongQuestionsLog.length);
console.log('Lives remaining:', lives);

console.log('Testing V1 CORRECT answer...');
isProcessingV1 = false;
handleV1OptionClick('987 654', '987 654', document.createElement('div'), {});
console.log('V1 correct answer handled successfully! Score:', score);

console.log('Testing V2 WRONG answer...');
currentV2Questions = [{ q: 'Một ô tô đi 120km trong 2 giờ', a: '60 km/h' }];
v2Index = 0;
v2Landmarks = ['Chặng 1', 'Chặng 2', 'Chặng 3', 'Đích'];
isProcessingV2 = false;
handleV2ChipClick('50 km/h', '60 km/h', document.createElement('div'), {});
console.log('V2 wrong answer handled successfully! Wrong log count:', wrongQuestionsLog.length);

console.log('Testing V2 CORRECT answer...');
isProcessingV2 = false;
handleV2ChipClick('60 km/h', '60 km/h', document.createElement('div'), {});
console.log('V2 correct answer handled successfully! Score:', score);

console.log('Testing V3 WRONG answer...');
bossQList = [{ q: 'Câu 3', opts: ['10', '20', '30', '40'], c: 0 }];
bossIdx = 0;
currentBossIndices = [0, 1, 2, 3];
bossCorrectIdx = 0;
bossAnswering = false;
checkBossAnswer(1, {});
console.log('V3 wrong answer handled successfully! Wrong log count:', wrongQuestionsLog.length);

console.log('Testing Review Modal generation...');
openReviewModal();
console.log('Review modal generated successfully!');

console.log('Testing Loot Box...');
showLootBox();
handleOpenLootChest();
handleLootContinue();
console.log('Loot Box flow completed successfully!');

console.log('✅ ALL SIMULATION TESTS PASSED WITH 0 ERRORS!');
`, ctx);
