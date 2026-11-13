@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
    py -3 iniciar.py
) else (
    where python >nul 2>nul
    if errorlevel 1 (
        echo Necesitas Python 3: https://www.python.org/downloads/
    ) else (
        python iniciar.py
    )
)
pause
