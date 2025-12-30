#!/usr/bin/env python3
"""
Vimeo Video Downloader CLI
Herramienta para descargar videos de Vimeo que requieren autenticación especial.
"""

import subprocess
import sys
import os
import re
import shutil
from pathlib import Path

# Colores para la terminal - CYBERPUNK THEME
class Colors:
    NEON_PINK = '\033[95m'
    NEON_BLUE = '\033[94m'
    NEON_CYAN = '\033[96m'
    NEON_GREEN = '\033[92m'
    NEON_YELLOW = '\033[93m'
    RED_ALERT = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    banner = f"""
{Colors.NEON_PINK}    ██╗   ██╗██╗███╗   ███╗███████╗ ██████╗     ███████╗ █████╗ ███████╗██╗   ██╗
    ██║   ██║██║████╗ ████║██╔════╝██╔═══██╗    ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝
    ██║   ██║██║██╔████╔██║█████╗  ██║   ██║    █████╗  ███████║███████╗ ╚████╔╝ 
    ╚██╗ ██╔╝██║██║╚██╔╝██║██╔══╝  ██║   ██║    ██╔══╝  ██╔══██║╚════██║  ╚██╔╝  
     ╚████╔╝ ██║██║ ╚═╝ ██║███████╗╚██████╔╝    ███████╗██║  ██║███████║   ██║   
      ╚═══╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚═════╝     ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   {Colors.ENDC}
    """
    print(banner)
    print(f"{Colors.NEON_CYAN}{Colors.BOLD}   >>> SYSTEM: {text.upper()} <<<{Colors.ENDC}")
    print(f"{Colors.NEON_PINK}{'='*70}{Colors.ENDC}\n")

def print_credits():
    print(f"{Colors.NEON_BLUE}[*] CORE SYSTEMS ONLINE:{Colors.ENDC}")
    print(f"    {Colors.NEON_GREEN}>> yt-dlp{Colors.ENDC} (The Engine)")
    print(f"    {Colors.NEON_GREEN}>> curl-cffi{Colors.ENDC} (The Stealth Cloak)")
    print(f"    {Colors.NEON_GREEN}>> ffmpeg{Colors.ENDC} (The Alchemist)")
    print(f"{Colors.NEON_PINK}[*] RESPECT TO THE ARCHITECTS.{Colors.ENDC}\n")

def print_success(text):
    print(f"{Colors.NEON_GREEN}[+] SUCCESS: {text}{Colors.ENDC}")

def print_error(text):
    print(f"{Colors.RED_ALERT}[!] ERROR: {text}{Colors.ENDC}")

def print_warning(text):
    print(f"{Colors.NEON_YELLOW}[!] WARNING: {text}{Colors.ENDC}")

def print_info(text):
    print(f"{Colors.NEON_CYAN}[*] INFO: {text}{Colors.ENDC}")

def print_step(number, text):
    print(f"{Colors.NEON_BLUE}{Colors.BOLD}[STEP {number}]{Colors.ENDC} {text}")

def ask_yes_no(question):
    """Pregunta sí/no al usuario."""
    while True:
        response = input(f"{Colors.NEON_YELLOW}[?] {question} (s/n): {Colors.ENDC}").strip().lower()
        if response in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        print_warning("Por favor responde 's' o 'n'")

def run_command(command, capture_output=True):
    """Ejecuta un comando y retorna el resultado."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=capture_output,
            text=True
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def check_python_version():
    """Verifica que Python sea 3.8+"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_error(f"Se requiere Python 3.8+. Versión actual: {version.major}.{version.minor}")
        return False
    print_success(f"Python {version.major}.{version.minor}.{version.micro}")
    return True

def check_pip():
    """Verifica que pip esté instalado."""
    success, stdout, _ = run_command("pip3 --version")
    if success:
        print_success("pip está instalado")
        return True
    
    success, stdout, _ = run_command("pip --version")
    if success:
        print_success("pip está instalado")
        return True
    
    print_error("pip no está instalado")
    return False

def check_yt_dlp():
    """Verifica si yt-dlp está instalado."""
    success, stdout, _ = run_command("yt-dlp --version")
    if success:
        version = stdout.strip()
        print_success(f"yt-dlp {version}")
        return True
    print_error("yt-dlp no está instalado")
    return False

def check_curl_cffi():
    """Verifica si curl-cffi está instalado (necesario para impersonación)."""
    try:
        import curl_cffi
        print_success("curl-cffi está instalado")
        return True
    except ImportError:
        print_error("curl-cffi no está instalado (necesario para bypass de protección)")
        return False

def check_ffmpeg():
    """Verifica si ffmpeg está instalado."""
    if shutil.which("ffmpeg"):
        success, stdout, _ = run_command("ffmpeg -version")
        if success:
            first_line = stdout.split('\n')[0] if stdout else "instalado"
            print_success(f"ffmpeg: {first_line[:50]}...")
            return True
    print_error("ffmpeg no está instalado (necesario para combinar audio/video)")
    return False

def install_yt_dlp():
    """Instala yt-dlp."""
    print_info("Instalando yt-dlp...")
    success, _, stderr = run_command("pip3 install -U yt-dlp", capture_output=False)
    if not success:
        success, _, _ = run_command("pip install -U yt-dlp", capture_output=False)
    return success

def install_curl_cffi():
    """Instala curl-cffi."""
    print_info("Instalando curl-cffi...")
    success, _, _ = run_command("pip3 install curl-cffi", capture_output=False)
    if not success:
        success, _, _ = run_command("pip install curl-cffi", capture_output=False)
    return success

def install_ffmpeg():
    """Proporciona instrucciones para instalar ffmpeg."""
    print_warning("\nffmpeg debe instalarse manualmente:")
    print(f"""
{Colors.NEON_CYAN}En Ubuntu/Debian:{Colors.ENDC}
    sudo apt update && sudo apt install ffmpeg

{Colors.NEON_CYAN}En Fedora:{Colors.ENDC}
    sudo dnf install ffmpeg

{Colors.NEON_CYAN}En Arch Linux:{Colors.ENDC}
    sudo pacman -S ffmpeg

{Colors.NEON_CYAN}En macOS (con Homebrew):{Colors.ENDC}
    brew install ffmpeg

{Colors.CYAN}En Windows:{Colors.ENDC}
    Descarga desde: https://ffmpeg.org/download.html
    O usa: choco install ffmpeg (con Chocolatey)
    O usa: winget install ffmpeg
""")
    return False

def check_dependencies():
    """Verifica todas las dependencias necesarias."""
    print_header("Verificando Dependencias")
    
    all_ok = True
    missing = []
    
    # Python
    if not check_python_version():
        print_error("No se puede continuar sin Python 3.8+")
        sys.exit(1)
    
    # pip
    if not check_pip():
        print_error("No se puede continuar sin pip")
        sys.exit(1)
    
    # yt-dlp
    if not check_yt_dlp():
        missing.append('yt-dlp')
        all_ok = False
    
    # curl-cffi
    if not check_curl_cffi():
        missing.append('curl-cffi')
        all_ok = False
    
    # ffmpeg
    if not check_ffmpeg():
        missing.append('ffmpeg')
        all_ok = False
    
    return all_ok, missing

def install_missing(missing):
    """Instala las dependencias faltantes."""
    print_header("Instalación de Dependencias")
    
    if not missing:
        print_success("Todas las dependencias están instaladas")
        return True
    
    print_warning(f"Faltan las siguientes dependencias: {', '.join(missing)}")
    
    if not ask_yes_no("¿Deseas instalarlas ahora?"):
        print_error("No se pueden descargar videos sin las dependencias necesarias")
        return False
    
    success = True
    
    if 'yt-dlp' in missing:
        if install_yt_dlp():
            print_success("yt-dlp instalado correctamente")
        else:
            print_error("Error instalando yt-dlp")
            success = False
    
    if 'curl-cffi' in missing:
        if install_curl_cffi():
            print_success("curl-cffi instalado correctamente")
        else:
            print_error("Error instalando curl-cffi")
            success = False
    
    if 'ffmpeg' in missing:
        install_ffmpeg()
        if not ask_yes_no("¿Ya instalaste ffmpeg?"):
            print_warning("Puedes continuar, pero el video final podría no combinarse correctamente")
    
    return success

def show_browser_instructions():
    """Muestra las instrucciones para obtener el hash del video."""
    print_header("Instrucciones para Obtener el Hash")
    
    print(f"""
{Colors.BOLD}Para descargar videos de Vimeo protegidos, necesitas obtener el "hash" del video.{Colors.ENDC}
{Colors.CYAN}Este hash es un código que aparece en la URL cuando el video se reproduce.{Colors.ENDC}

{Colors.YELLOW}{'─'*60}{Colors.ENDC}
""")
    
    print(f"""{Colors.BOLD}{Colors.GREEN}✨ MÉTODO MÁS FÁCIL - Ver Código Fuente:{Colors.ENDC}
{Colors.CYAN}─────────────────────────────────────────{Colors.ENDC}
1. Abre el video de Vimeo en tu navegador (ej: https://vimeo.com/1133688762)
2. Presiona {Colors.BOLD}Ctrl+U{Colors.ENDC} para ver el código fuente de la página
3. Presiona {Colors.BOLD}Ctrl+F{Colors.ENDC} para buscar
4. Busca: {Colors.BOLD}?h={Colors.ENDC}
5. Encontrarás URLs como: {Colors.CYAN}https://player.vimeo.com/video/1133688762?h={Colors.GREEN}75891db44a{Colors.ENDC}
6. Copia el valor después de {Colors.BOLD}h={Colors.ENDC}
""")

    print(f"""{Colors.BOLD}{Colors.BLUE}🔍 MÉTODO ALTERNATIVO - Inspeccionar Elemento:{Colors.ENDC}
{Colors.CYAN}──────────────────────────────────────────────{Colors.ENDC}
1. En la página del video, presiona {Colors.BOLD}F12{Colors.ENDC} (DevTools)
2. En el panel de Elements, presiona {Colors.BOLD}Ctrl+F{Colors.ENDC}
3. Busca: {Colors.BOLD}?h={Colors.ENDC} o {Colors.BOLD}embedUrl{Colors.ENDC}
4. Copia el hash que aparece después de {Colors.BOLD}h={Colors.ENDC}
""")

    print(f"""{Colors.YELLOW}{'─'*60}{Colors.ENDC}
{Colors.BOLD}EJEMPLO:{Colors.ENDC}

En el código fuente encontrarás algo como:
{Colors.CYAN}"embedUrl":"https://player.vimeo.com/video/1133688762?h={Colors.GREEN}75891db44a{Colors.CYAN}"{Colors.ENDC}
                                                            {Colors.GREEN}^^^^^^^^^^{Colors.ENDC}
                                                            {Colors.GREEN}Este es el hash{Colors.ENDC}

{Colors.BOLD}Lo que necesitas copiar es:{Colors.ENDC} {Colors.GREEN}75891db44a{Colors.ENDC}
{Colors.YELLOW}{'─'*60}{Colors.ENDC}
""")

def extract_video_id(url):
    """Extrae el ID del video de una URL de Vimeo."""
    patterns = [
        r'vimeo\.com/(\d+)',
        r'player\.vimeo\.com/video/(\d+)',
        r'^(\d+)$'  # Solo el ID
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None

def get_user_input():
    """Obtiene la información necesaria del usuario."""
    print_header("Información del Video")
    
    # URL o ID del video
    while True:
        print_info("Introduce la URL de Vimeo o el ID del video")
        print(f"  {Colors.CYAN}Ejemplos:{Colors.ENDC}")
        print(f"    - https://vimeo.com/1142702955")
        print(f"    - 1142702955")
        url = input(f"\n{Colors.YELLOW}URL o ID: {Colors.ENDC}").strip()
        
        video_id = extract_video_id(url)
        if video_id:
            print_success(f"ID del video: {video_id}")
            break
        else:
            print_error("No se pudo extraer el ID del video. Intenta de nuevo.")
    
    # Hash
    print()
    print_info("Introduce el hash del video (el valor de 'h=' que obtuviste)")
    print(f"  {Colors.CYAN}Ejemplo: ad106da4bf{Colors.ENDC}")
    
    while True:
        video_hash = input(f"\n{Colors.YELLOW}Hash (h=): {Colors.ENDC}").strip()
        # Limpiar si el usuario pegó más de lo necesario
        if 'h=' in video_hash:
            match = re.search(r'h=([a-zA-Z0-9]+)', video_hash)
            if match:
                video_hash = match.group(1)
        
        if video_hash and re.match(r'^[a-zA-Z0-9]+$', video_hash):
            print_success(f"Hash: {video_hash}")
            break
        else:
            print_error("El hash parece inválido. Debe contener solo letras y números.")
    
    # Nombre del archivo
    print()
    print_info("Nombre para el archivo de salida (sin extensión)")
    print(f"  {Colors.CYAN}Deja vacío para usar 'video_vimeo_{video_id}'{Colors.ENDC}")
    
    filename = input(f"\n{Colors.YELLOW}Nombre: {Colors.ENDC}").strip()
    if not filename:
        filename = f"video_vimeo_{video_id}"
    
    # Limpiar caracteres no válidos del nombre
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    print_success(f"Archivo: {filename}.mp4")
    
    return video_id, video_hash, filename

def download_video(video_id, video_hash, filename):
    """Descarga el video usando yt-dlp."""
    print_header("Descargando Video")
    
    player_url = f"https://player.vimeo.com/video/{video_id}?h={video_hash}"
    output_path = os.path.join(os.getcwd(), f"{filename}.%(ext)s")
    
    print_info(f"URL del player: {player_url}")
    print_info(f"Guardando en: {os.getcwd()}")
    print()
    
    command = [
        "yt-dlp",
        "--impersonate", "chrome",
        "--referer", "https://vimeo.com/",
        "-o", output_path,
        player_url
    ]
    
    print(f"{Colors.CYAN}Ejecutando: {' '.join(command)}{Colors.ENDC}\n")
    
    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        for line in process.stdout:
            print(line, end='')
        
        process.wait()
        
        if process.returncode == 0:
            final_path = os.path.join(os.getcwd(), f"{filename}.mp4")
            if os.path.exists(final_path):
                size_mb = os.path.getsize(final_path) / (1024 * 1024)
                print()
                print_success(f"¡Descarga completada!")
                print_success(f"Archivo: {final_path}")
                print_success(f"Tamaño: {size_mb:.2f} MB")
                return True
            else:
                # Buscar el archivo con cualquier extensión
                for ext in ['mp4', 'mkv', 'webm']:
                    path = os.path.join(os.getcwd(), f"{filename}.{ext}")
                    if os.path.exists(path):
                        size_mb = os.path.getsize(path) / (1024 * 1024)
                        print()
                        print_success(f"¡Descarga completada!")
                        print_success(f"Archivo: {path}")
                        print_success(f"Tamaño: {size_mb:.2f} MB")
                        return True
        
        print()
        print_error("La descarga falló")
        return False
        
    except Exception as e:
        print_error(f"Error durante la descarga: {e}")
        return False

def main():
    """Función principal."""
    print_header("Vimeo Video Downloader")
    print_credits()
    print(f"{Colors.NEON_CYAN}Herramienta para descargar videos de Vimeo protegidos{Colors.ENDC}")
    print(f"{Colors.NEON_CYAN}Versión 1.0{Colors.ENDC}")
    
    # Verificar dependencias
    all_ok, missing = check_dependencies()
    
    if not all_ok:
        if not install_missing(missing):
            print_error("No se puede continuar sin las dependencias necesarias")
            sys.exit(1)
        
        # Re-verificar
        print()
        all_ok, missing = check_dependencies()
        if missing and 'ffmpeg' not in missing:
            print_error("Algunas dependencias no se instalaron correctamente")
            sys.exit(1)
    
    # Mostrar instrucciones
    show_browser_instructions()
    
    input(f"{Colors.YELLOW}Presiona Enter cuando hayas obtenido el hash...{Colors.ENDC}")
    
    # Obtener información del usuario
    video_id, video_hash, filename = get_user_input()
    
    # Confirmar
    print()
    print_info("Resumen:")
    print(f"  • Video ID: {Colors.GREEN}{video_id}{Colors.ENDC}")
    print(f"  • Hash: {Colors.GREEN}{video_hash}{Colors.ENDC}")
    print(f"  • Archivo: {Colors.GREEN}{filename}.mp4{Colors.ENDC}")
    print(f"  • Carpeta: {Colors.GREEN}{os.getcwd()}{Colors.ENDC}")
    print()
    
    if not ask_yes_no("¿Iniciar descarga?"):
        print_warning("Descarga cancelada")
        sys.exit(0)
    
    # Descargar
    success = download_video(video_id, video_hash, filename)
    
    if success:
        print()
        print_header("¡Descarga Exitosa!")
        if ask_yes_no("¿Deseas descargar otro video?"):
            # Reiniciar el proceso de descarga
            show_browser_instructions()
            input(f"{Colors.YELLOW}Presiona Enter cuando hayas obtenido el hash...{Colors.ENDC}")
            video_id, video_hash, filename = get_user_input()
            download_video(video_id, video_hash, filename)
    else:
        print()
        print_header("Error en la Descarga")
        print_warning("Posibles soluciones:")
        print("  1. Verifica que el hash sea correcto")
        print("  2. Asegúrate de que el video sea accesible")
        print("  3. Intenta obtener el hash nuevamente")
        print("  4. Verifica tu conexión a internet")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print_warning("Operación cancelada por el usuario")
        sys.exit(0)
