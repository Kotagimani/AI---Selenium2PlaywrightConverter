@echo off
echo ==========================================
echo   🚀 B.L.A.S.T. Converter App (Pro)
echo ==========================================
echo Ensuring dependencies...
python -m pip install -r requirements.txt
echo.
echo Starting FastAPI server...
echo Open your browser to: http://localhost:8000
echo.
python backend/server.py
pause
