// js/play.js - Điều hướng thông minh đến trạm tương ứng trong hệ thống 35 trạm
const urlParams = new URLSearchParams(window.location.search);
const currentWeek = urlParams.get('week');

if (currentWeek) {
    const weekNum = parseInt(currentWeek, 10);
    if (!isNaN(weekNum) && weekNum >= 1 && weekNum <= 35) {
        window.location.replace(`${weekNum}.html`);
    } else {
        window.location.replace('index.html');
    }
} else {
    window.location.replace('index.html');
}