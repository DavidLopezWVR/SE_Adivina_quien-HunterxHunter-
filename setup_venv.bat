@echo off
echo 🔧 Creando entorno virtual...
python -m venv venv

echo 🔁 Activando entorno virtual...
call venv\Scripts\activate

echo 📦 Instalando dependencias...
pip install -r requirements.txt

echo ✅ Listo. Puedes ejecutar el juego con:
echo python hxh_adivina_quien.py
pause
