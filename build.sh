set -e

echo "activating environment"
source "/home/alex1ne/Desktop/Single codes/python/default_env/bin/activate"

echo "compiling file"
pyinstaller --onefile script.py

echo "making executable"
chmod +x "/home/alex1ne/Desktop/Single codes/python/dist/script"

echo "running program"
"/home/alex1ne/Desktop/Single codes/python/dist/script"

