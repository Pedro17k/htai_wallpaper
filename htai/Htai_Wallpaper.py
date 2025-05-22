import os 
import requests 
import ctypes
import subprocess
import platform

def download_image(url, save_path):

    try:
        response = requests.get(url)
        response.raise_for_status()
            # os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Imagem salva em {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Falha ao baixar a imagem: {e}")

def set_wallpaper_windows(save_path):

    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, save_path, 3)
        print("Papel de parede definido no Windows")
    except Exception as e:
        print(f"Falha ao definir o papel de parede no Windows: {e}")
"""""

def set_wallpaper_linux(save_path):

    try:
        command = f"gsettings set org.gnome.desktop.background picture-uri file://{save_path}"
        subprocess.run(command, shell=True, check=True)
        print(f"Papel de parede defino no Linux")
    except subprocess.CalledProcessError as e:
        print(f"Falha ao definir o papel de parede no linux: {e}")
"""""


def set_wallpaper_kalilinux(save_path):

    try:
        command = f"xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s {save_path}"
        subprocess.run(command, shell=True, check=True)
        print("Papel de parede definido no linux (XFCE)")
    except subprocess.CalledProcessError as e:
        print(f"Falha ao definir o papel de parede do linux: {e}")
        print("Saida do comando: ", e.output)
        print("Erro do comando : ", e.stderr)

"""
def set_wallpaper_kalilinux(save_path):

    try:
        command = f"feh --bg-scale {save_path}"
        subprocess.run(command, shell=True, check=True)
        print("Papel de parede definido no linux (XFCE) usando feh")
    except subprocess.CalledProcessError as e:
        print(f"Falha ao definir o papel de parede do linux: {e}")
"""

def main():

    image_url = 'https://i.pinimg.com/736x/d8/aa/cb/d8aacbedc7d4d36059c53fd63e4ec72a.jpg'
    if platform.system() == "Windows":
        save_path = os.path.join(os.getenv('USERPROFILE'), 'Downloads', 'anime_wallpaper.jpg')
    else:
        save_path = os.path.join(os.getenv('HOME'), 'Pictures', 'anime_wallpaper.jpg')

    download_image(image_url, save_path)

    if platform.system() == "Windows":
        set_wallpaper_windows(save_path)
    else:
        set_wallpaper_kalilinux(save_path)

if __name__ == "__main__":
    main()
