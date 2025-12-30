<div align="center">

# 📼 VIMEO EASY DL

**[ 🔓 UNLOCK THE SIGNAL // LIBERA LA SEÑAL 🔓 ]**

<p>
  <a href="#english">🇬🇧 ENGLISH</a> | <a href="#español">🇪🇸 ESPAÑOL</a>
</p>

<img src="https://img.shields.io/badge/STATUS-OPERATIONAL-brightgreen?style=for-the-badge&logo=terminal" alt="Status Operational">
<img src="https://img.shields.io/badge/LICENSE-GPLv3-red?style=for-the-badge&logo=gnu" alt="License GPLv3">
<img src="https://img.shields.io/badge/PYTHON-3.8+-blue?style=for-the-badge&logo=python" alt="Python Version">

</div>

---

<a name="english"></a>
## 🇬🇧 ENGLISH

### THE MANIFESTO

**Information wants to be free.**

In an era where mega-corporations build walled gardens to trap our culture and knowledge, **Vimeo Easy DL** is your digital lockpick. They try to restrict access with complex authentication, proprietary streams, and artificial scarcity. We say **NO**.

This tool is not just a downloader; it's an act of digital rebellion. It empowers you to archive, preserve, and own the media that matters to you. Don't let the cloud dictate what you can watch. Take back control.

### ⚡ WHAT IS THIS?

**Vimeo Easy DL** is a stealthy, automated CLI wrapper for the powerful `yt-dlp` engine, enhanced with `curl-cffi` for browser impersonation. It bypasses restrictions that normally block standard downloaders, allowing you to pull high-quality video and audio from Vimeo links that are otherwise "protected" or "private" (provided you have the password/access).

**Key Features:**
*   **Stealth Mode:** Uses `curl-cffi` to impersonate real browsers, bypassing bot detection.
*   **High Fidelity:** Downloads the best available video and audio streams and merges them losslessly using `ffmpeg`.
*   **Cross-Platform:** Works on the metal of Linux, Windows, and macOS.
*   **Zero Friction:** Auto-installs Python dependencies. You just bring the system tools.

### 🛠️ SYSTEM REQUIREMENTS

You need to have these installed on your deck (computer):

1.  **Python 3.8+**: The language of the snake.
2.  **FFmpeg**: The universal media converter. **(CRITICAL FOR MERGING AUDIO/VIDEO)**

### 🚀 DEPLOYMENT INSTRUCTIONS

#### 🐧 Linux (Debian/Ubuntu/Arch/Fedora)

The native habitat of the hacker.

1.  **Install FFmpeg & Python:**
    ```bash
    # Debian/Ubuntu
    sudo apt update && sudo apt install ffmpeg python3 python3-pip

    # Arch Linux
    sudo pacman -S ffmpeg python python-pip

    # Fedora
    sudo dnf install ffmpeg python3
    ```

2.  **Clone & Run:**
    ```bash
    git clone https://github.com/juantomoo/vimeo-easy-dl.git
    cd vimeo-easy-dl
    chmod +x vimeo-download.sh
    ./vimeo-download.sh
    ```

#### 🍎 macOS

For those in the walled garden who still want to peek outside.

1.  **Install Homebrew** (if you haven't already):
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2.  **Install FFmpeg & Python:**
    ```bash
    brew install ffmpeg python
    ```

3.  **Clone & Run:**
    ```bash
    git clone https://github.com/juantomoo/vimeo-easy-dl.git
    cd vimeo-easy-dl
    chmod +x vimeo-download.sh
    ./vimeo-download.sh
    ```

#### 🪟 Windows

The corporate beast. Tame it.

1.  **Install Python:** Download from [python.org](https://www.python.org/downloads/). **IMPORTANTE:** Check "Add Python to PATH" during installation.
2.  **Install FFmpeg:**
    *   Download from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
    *   Extract the zip.
    *   Add the `bin` folder to your System PATH environment variable. (Google "add ffmpeg to path windows" if you're stuck).
3.  **Run the tool:**
    *   Open PowerShell or CMD.
    *   Navigate to the folder: `cd path\to\vimeo-easy-dl`
    *   Run: `python vimeo_downloader.py`

### 💀 DISCLAIMER

*This tool is for educational and archival purposes only. We do not condone piracy. Respect the creators. Fight the platforms.*

### 🦾 CREDITS / TECH STACK

This tool stands on the shoulders of giants. We salute the developers of:

*   **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: The engine that powers the download.
*   **[curl-cffi](https://github.com/yifeikong/curl_cffi)**: The stealth technology for browser impersonation.
*   **[FFmpeg](https://ffmpeg.org/)**: The alchemist of multimedia processing.

---

<a name="español"></a>
## 🇪🇸 ESPAÑOL

### EL MANIFIESTO

**La información quiere ser libre.**

En una era donde las mega-corporaciones construyen jardines amurallados para atrapar nuestra cultura y conocimiento, **Vimeo Easy DL** es tu ganzúa digital. Intentan restringir el acceso con autenticación compleja, formatos propietarios y escasez artificial. Nosotros decimos **NO**.

Esta herramienta no es solo un descargador; es un acto de rebelión digital. Te empodera para archivar, preservar y poseer los medios que te importan. No dejes que la nube dicte lo que puedes ver. Recupera el control.

### ⚡ ¿QUÉ ES ESTO?

**Vimeo Easy DL** es un wrapper de CLI sigiloso y automatizado para el poderoso motor `yt-dlp`, mejorado con `curl-cffi` para la suplantación de navegador. Evade las restricciones que normalmente bloquean a los descargadores estándar, permitiéndote extraer video y audio de alta calidad de enlaces de Vimeo que de otro modo estarían "protegidos" o "privados" (siempre que tengas la contraseña/acceso).

**Características Clave:**
*   **Modo Sigilo:** Usa `curl-cffi` para hacerse pasar por navegadores reales, evadiendo la detección de bots.
*   **Alta Fidelidad:** Descarga los mejores flujos de video y audio disponibles y los une sin pérdidas usando `ffmpeg`.
*   **Multiplataforma:** Funciona en el metal de Linux, Windows y macOS.
*   **Cero Fricción:** Auto-instala las dependencias de Python. Tú solo pones las herramientas del sistema.

### 🛠️ REQUISITOS DEL SISTEMA

Necesitas tener esto instalado en tu máquina:

1.  **Python 3.8+**: El lenguaje de la serpiente.
2.  **FFmpeg**: El convertidor de medios universal. **(CRÍTICO PARA UNIR AUDIO/VIDEO)**

### 🚀 INSTRUCCIONES DE DESPLIEGUE

#### 🐧 Linux (Debian/Ubuntu/Arch/Fedora)

El hábitat natural del hacker.

1.  **Instalar FFmpeg y Python:**
    ```bash
    # Debian/Ubuntu
    sudo apt update && sudo apt install ffmpeg python3 python3-pip

    # Arch Linux
    sudo pacman -S ffmpeg python python-pip

    # Fedora
    sudo dnf install ffmpeg python3
    ```

2.  **Clonar y Ejecutar:**
    ```bash
    git clone https://github.com/juantomoo/vimeo-easy-dl.git
    cd vimeo-easy-dl
    chmod +x vimeo-download.sh
    ./vimeo-download.sh
    ```

#### 🍎 macOS

Para aquellos en el jardín amurallado que aún quieren mirar hacia afuera.

1.  **Instalar Homebrew** (si aún no lo tienes):
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2.  **Instalar FFmpeg y Python:**
    ```bash
    brew install ffmpeg python
    ```

3.  **Clonar y Ejecutar:**
    ```bash
    git clone https://github.com/juantomoo/vimeo-easy-dl.git
    cd vimeo-easy-dl
    chmod +x vimeo-download.sh
    ./vimeo-download.sh
    ```

#### 🪟 Windows

La bestia corporativa. Dómala.

1.  **Instalar Python:** Descarga desde [python.org](https://www.python.org/downloads/). **IMPORTANTE:** Marca "Add Python to PATH" durante la instalación.
2.  **Instalar FFmpeg:**
    *   Descarga desde [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
    *   Extrae el zip.
    *   Añade la carpeta `bin` a tu variable de entorno PATH del sistema. (Busca en Google "agregar ffmpeg al path windows" si te atascas).
3.  **Ejecutar la herramienta:**
    *   Abre PowerShell o CMD.
    *   Navega a la carpeta: `cd path\to\vimeo-easy-dl`
    *   Ejecuta: `python vimeo_downloader.py`

### 💀 DESCARGO DE RESPONSABILIDAD

*Esta herramienta es solo para fines educativos y de archivo. Respeta a los creadores. Lucha contra las plataformas codiciosas.*
### 🦾 CRÉDITOS / TECH STACK

Esta herramienta se apoya en hombros de gigantes. Saludamos a los desarrolladores de:

*   **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: El motor que impulsa la descarga.
*   **[curl-cffi](https://github.com/yifeikong/curl_cffi)**: La tecnología de sigilo para suplantación de navegador.
*   **[FFmpeg](https://ffmpeg.org/)**: El alquimista del procesamiento multimedia.
---

<div align="center">
  <sub>Built with 💻 and ☕ by <a href="https://github.com/juantomoo">juantomoo</a></sub>
</div>
