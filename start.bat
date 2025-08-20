@echo off
start cmd /k "venv\Scripts\activate.bat && python -m consumers.product.consumer"
@REM start cmd /k "venv\Scripts\activate.bat && python -m consumers.temp.consumer"
start cmd /k "venv\Scripts\activate.bat && python main.py"
