#!/bin/bash
# setup.sh - Project setup script

# Exit on error
set -e

echo "=== Setting up Web Log Analyzer Project ==="

# 1. Create project folders
echo "[1/6] Creating project folders..."
mkdir -p ~/web-log-analyzer/{output,sample_data}

# 2. Copy sample files (if present in Downloads)
if [ -f ~/Downloads/access.log ]; then
    cp ~/Downloads/access.log ~/web-log-analyzer/sample_data/access.log
    echo "Copied access.log"
else
    echo "⚠️ No access.log found in Downloads. Please add it manually to sample_data/"
fi

if [ -f ~/Downloads/client_hostname.csv ]; then
    cp ~/Downloads/client_hostname.csv ~/web-log-analyzer/sample_data/client_hostname.csv
    echo "Copied client_hostname.csv"
else
    echo "⚠️ No client_hostname.csv found in Downloads. Please add it manually to sample_data/"
fi

# 3. Create virtual environment if not exists
if [ ! -d ~/myenv ]; then
    echo "[2/6] Creating Python virtual environment..."
    sudo apt install -y python3-venv
    python3 -m venv ~/myenv
else
    echo "✅ Virtual environment already exists."
fi

# 4. Activate venv
echo "[3/6] Activating virtual environment..."
source ~/myenv/bin/activate

# 5. Install dependencies
echo "[4/6] Installing dependencies..."
pip install --upgrade pip
pip install pandas numpy matplotlib seaborn

# 6. Run the analyzer (if exists)
if [ -f log_analyzer.py ]; then
    echo "[5/6] Running log analyzer..."
    python3 log_analyzer.py
    echo "[6/6] Report saved in output/report.txt"
else
    echo "⚠️ No log_analyzer.py found. Add your script in the project root."
fi

echo "=== Setup Complete ✅ ==="
