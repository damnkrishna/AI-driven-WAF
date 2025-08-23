#!/bin/bash
set -e

echo "=== Starting Project Setup: AI-driven-WAF ==="

echo
# --- Fix corrupt zsh history file if present (optional) ---
HISTFILE="$HOME/.zsh_history"
if [ -f "$HISTFILE" ]; then
  strings "$HISTFILE" > "$HISTFILE.tmp" && mv "$HISTFILE.tmp" "$HISTFILE"
  echo "📜 Fixed corrupt zsh history file (if corrupted)."
fi

echo
# --- Create project directories ---
echo "[1/6] Creating project folders..."
mkdir -p data-set/sample_data
mkdir -p src/output

# Check for essential files and inform the user if missing
if [ ! -f "data-set/sample_data/access.log" ]; then
  echo "⚠ No access.log found in data-set/sample_data. Please add it manually or run the download script."
fi

if [ ! -f "data-set/sample_data/client_hostname.csv" ]; then
  echo "⚠ No client_hostname.csv found in data-set/sample_data. Please add it manually or run the download script."
fi

echo "✅ Project folders created."

echo
# --- Setup Python Virtual Environment ---
if [ ! -d "$HOME/myenv" ]; then
  echo "[2/6] Creating Python virtual environment at ~/myenv ..."
  python3 -m venv ~/myenv
else
  echo "[2/6] Virtual environment already exists."
fi

echo
echo "[3/6] Activating virtual environment..."
# shellcheck disable=SC1091
source ~/myenv/bin/activate

echo
echo "[4/6] Installing dependencies from requirement.txt..."
if [ -f "requirement.txt" ]; then
  pip install --upgrade pip
  pip install -r requirement.txt
else
  echo "⚠ requirement.txt missing in project root. Install dependencies manually."
fi

echo
# --- Check Kaggle CLI ---
if ! command -v kaggle &> /dev/null; then
  echo "⚠ Kaggle CLI not found. Please install Kaggle CLI and authenticate before downloading datasets."
  echo "   To install: pip install --user kaggle"
  echo "   Authenticate by placing kaggle.json in ~/.kaggle/ with chmod 600."
  echo "   See https://www.kaggle.com/docs/api for details."
else
  echo "[5/6] Kaggle CLI found."

  # Download Kaggle data (if not already downloaded)
  if [ ! -f "data-set/sample_data/web-server-access-logs.zip" ]; then
    echo "📥 Downloading dataset from Kaggle..."
    kaggle datasets download -d eliasdabbas/web-server-access-logs -p data-set/sample_data
    echo "📂 Unzipping dataset..."
    unzip -o data-set/sample_data/web-server-access-logs.zip -d data-set/sample_data
    echo "✅ Dataset ready in data-set/sample_data/"
  else
    echo "✅ Dataset already downloaded."
  fi
fi

echo
echo "[6/6] Setup Complete ✅"
echo
echo "Next steps:"
echo "- Activate virtual environment (if not already):"
echo "    source ~/myenv/bin/activate"
echo "- Add your log_analyzer.py script to 'Passive' or 'src' directory as required."
echo "- Run your analyzer script with Python."
echo "- Make sure dataset files (access.log, client_hostname.csv) are in data-set/sample_data."
echo "- If missing, obtain Kaggle API token and use the download_data.sh script or manually add data."
echo
echo "Happy analyzing! 🚀"
