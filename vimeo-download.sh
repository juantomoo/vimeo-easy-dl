#!/bin/bash
# Wrapper para ejecutar el descargador de Vimeo
# Uso: ./vimeo-download.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Verificar Python
if command -v python3 &> /dev/null; then
    python3 "$SCRIPT_DIR/vimeo_downloader.py" "$@"
elif command -v python &> /dev/null; then
    python "$SCRIPT_DIR/vimeo_downloader.py" "$@"
else
    echo "Error: Python no está instalado"
    echo "Instala Python 3.8+ para usar esta herramienta"
    exit 1
fi
