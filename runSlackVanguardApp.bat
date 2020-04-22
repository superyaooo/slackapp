set venv_root_dir=<app_path>\env
set app_root_dir=<app_path>
cd %venv_root_dir%
call %venv_root_dir%\Scripts\activate.bat

cd %app_root_dir%
python %app_root_dir%\app.py

cd %venv_root_dir%
call %venv_root_dir%\Scripts\deactivate.bat
exit
