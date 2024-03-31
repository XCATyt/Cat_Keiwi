import os
import requests
import tkinter as tk
from tkinter import filedialog
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def download_files():
    # GitHub URL'si
    url = "https://github.com/murat725178252/Cat-Keiwi/tree/main/EN/"

    # Hedef dizin seç
    target_dir = filedialog.askdirectory()
    if not target_dir:
        return

    # Eğer hedef dizin yoksa oluştur
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Sayfayı indir ve parse et
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Tüm dosya linklerini bul
    file_links = [urljoin(url, link["href"]) for link in soup.select("a[href$='.']")]

    # Dosyaları indir
    for file_link in file_links:
        # Dosya adını al
        filename = os.path.basename(file_link)
        # Dosyayı indir
        response = requests.get(file_link)
        # Dosyayı kaydet
        with open(os.path.join(target_dir, filename), "wb") as f:
            f.write(response.content)

    print("Dosyalar başarıyla indirildi.")

# Ana pencere oluştur
root = tk.Tk()
root.title("GitHub Dosya İndirme Aracı")

# Yükle butonunu ekle
download_button = tk.Button(root, text="Dosyaları İndir", command=download_files)
download_button.pack(pady=10)

# Pencereyi göster
root.mainloop()
