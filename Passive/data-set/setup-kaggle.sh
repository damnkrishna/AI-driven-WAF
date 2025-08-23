#!/bin/bash
set -e

echo "🔧 Installing Kaggle CLI..."

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "❌ pip could not be found. Please install Python and pip first."
    exit 1
fi

# Install kaggle package (may require sudo depending on environment)
pip install --user kaggle

echo "✅ Kaggle CLI installed."

# Create ~/.kaggle directory if it doesn't exist
KAGGLE_DIR="$HOME/.kaggle"
if [ ! -d "$KAGGLE_DIR" ]; then
    mkdir -p "$KAGGLE_DIR"
    echo "📂 Created $KAGGLE_DIR directory."
else
    echo "📂 $KAGGLE_DIR directory already exists."
fi

echo
echo "🔐 Please download your Kaggle API token (kaggle.json) from:"
echo "   https://www.kaggle.com/account"
echo "   and place it in $KAGGLE_DIR with permissions set to read/write for the user only."
echo
echo "Example commands after downloading kaggle.json:"
echo "   mv /path/to/kaggle.json $KAGGLE_DIR/"
echo "   chmod 600 $KAGGLE_DIR/kaggle.json"
echo
echo "After that, verify by running: kaggle --version"
