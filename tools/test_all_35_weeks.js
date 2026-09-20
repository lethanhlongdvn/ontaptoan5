const fs = require('fs');
const { generateSmartDistractors } = require('./test_distractor_engine.js');

let totalQuestions = 0;
let passedQuestions = 0;
let issues = [];

const allWeeksBank = [];
for (let i = 1; i <= 35; i++) {
    const d = JSON.parse(fs.readFileSync(`data/week-${i}.json`, 'utf8'));
    ['V1', 'V2'].forEach(v => {
        if (d.bank && d.bank[v]) {
            d.bank[v].forEach(item => allWeeksBank.push(item));
        }
    });
}

for (let w = 1; w <= 35; w++) {
    const d = JSON.parse(fs.readFileSync(`data/week-${w}.json`, 'utf8'));
    ['V1', 'V2'].forEach(v => {
        if (d.bank && d.bank[v]) {
            d.bank[v].forEach((item, idx) => {
                totalQuestions++;
                const distractors = generateSmartDistractors(item.q, item.a, d.bank[v], allWeeksBank);
                const all4 = [item.a.trim(), ...distractors];
                const uniqueSet = new Set(all4.map(x => x.toLowerCase()));

                if (distractors.length < 3) {
                    issues.push(`[W${w}-${v}-Q${idx + 1}] Only ${distractors.length} distractors for "${item.a}"`);
                } else if (uniqueSet.size < 4) {
                    issues.push(`[W${w}-${v}-Q${idx + 1}] Duplicates: ${JSON.stringify(all4)}`);
                } else {
                    passedQuestions++;
                }
            });
        }
    });
}

console.log(`TOTAL QUESTIONS TESTED: ${totalQuestions}`);
console.log(`PASSED: ${passedQuestions} (${((passedQuestions / totalQuestions) * 100).toFixed(2)}%)`);
console.log(`ISSUES COUNT: ${issues.length}`);
if (issues.length > 0) {
    console.log('Issues:');
    issues.slice(0, 10).forEach(iss => console.log('  !', iss));
}
