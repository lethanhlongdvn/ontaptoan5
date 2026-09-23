@echo off
title Trien khai EduBot len Zalo Mini App
cd /d "%~dp0edubot-zmp"
cls
echo ====================================================================
echo       TRIEN KHAI EDUBOT TOAN 5 LEN ZALO MINI APP
echo ====================================================================
echo.
echo   Mini App ID: 636911928251914640 (EduBot)
echo.
echo   [BUOC 1]: DANG NHAP ZALO
echo   - He thong se hoi phuong thuc dang nhap, ban hay BAM PHIM ENTER.
echo   - Man hinh se hien MA QR CODE.
echo   - Mo Zalo tren dien thoai, quet ma QR tren man hinh de dang nhap.
echo.
echo ====================================================================
echo.
call npx --yes zmp-cli login
echo.
echo ====================================================================
echo   [BUOC 2]: DANG TAI DU LIEU APP LEN MAY CHU ZALO CLOUD...
echo ====================================================================
echo.
call npx --yes zmp-cli deploy --passive --desc "Ban 35 tuan chinh thuc" --outputDir www
echo.
echo ====================================================================
echo   HOAN TAT! QUET MA QR MO APP TREN DIEN THOAI!
echo ====================================================================
echo.
pause
