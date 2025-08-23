#!/bin/bash
set -e  # Exit immediately if a command fails

# Ensure script runs from project root
cd "$(dirname "$0")"

# Create data directory if not exists
mkdir -p sample_data

echo "📥 Downloading dataset from Kaggle..."
kaggle datasets download -d eliasdabbas/web-server-access-logs -p sample_data

echo "📂 Unzipping dataset..."
unzip -o sample_data/web-server-access-logs.zip -d sample_data

echo "✅ Dataset ready in sample_data/"
