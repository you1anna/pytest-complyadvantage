python -m venv venv
call .\venv\Scripts\activate.bat
python -m pip install -r requirements.txt --disable-pip-version-check
pytest "tests"
pause