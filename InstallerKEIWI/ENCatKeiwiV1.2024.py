from tkinter import Tk
from tkinter.ttk import Label, Progressbar, Button
from requests import get
from os.path import expanduser, join

Ilist = [
    "https://github.com/murat725178252/Cat-Keiwi/raw/main/EN/CatKeiwi.exe",
    "https://github.com/murat725178252/Cat-Keiwi/raw/main/EN/Data/idle.png",
    "https://github.com/murat725178252/Cat-Keiwi/raw/main/EN/Data/sitting.png",
]

def download_file(url, save_path):
    response = get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)
    print("Dosya başarıyla indirildi:", save_path)

def start_download():
    for i in range(len(Ilist)):
        url = Ilist[i]
        file_name = url.split("/")[-1]  # URL'den dosya adını al
        save_path = join(expanduser("~"), "Desktop", file_name)
        download_file(url, save_path)

def ui():
    global download, progressbar
    download = Tk()
    download.geometry("400x200")
    progressbar = Progressbar(download, orient="horizontal", length=350, mode="determinate")
    status = Label(download, text="Downloading Keiwi Cat")
    start_button = Button(download, text="Start Download", command=start_download)

    progressbar.pack(pady=10)
    status.pack(pady=5)
    start_button.pack(pady=5)

    download.mainloop()

if __name__ == "__main__":
    ui()
