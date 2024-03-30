from tkinter import Tk, Listbox
from tkinter.ttk import Label, Progressbar, Button
from requests import get

Ilist = [
    "KeiwiCat",
    "KeiwiCat/KeiwiCat.exe",
    "KeiwiCat/Data/idle.png",
    "KeiwiCat/Data/sitting.png",
    "KeiwiCat/backup/Kedito_idle.png",
    "KeiwiCat/backup/Kedito_sitting.png",
    "KeiwiCat/backup/sitting.png",
]

def populate_file_list():
    for item in Ilist:
        file_list.insert("end", item)

def start_download():
    def get_github_contents(owner, repo, path):
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
        response = get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Hata:", response.status_code)
            return None

    owner = "murat725178252"
    repo = "Cat-Keiwi"
    path = "EN"
    # https://github.com/murat725178252/Cat-Keiwi/
    contents = get_github_contents(owner, repo, path)
    if contents:
        for item in contents:
            print(item["name"])

def ui():
    global download, file_list, progressbar
    download = Tk()
    download.geometry("400x300")
    progressbar = Progressbar(download, orient="horizontal", length=350, mode="determinate")
    status = Label(download, text="Downloading Keiwi Cat")
    file_list = Listbox(download)

    populate_file_list()

    progressbar.pack(pady=5)
    status.pack(pady=5)
    file_list.pack(pady=5)
    start_button = Button(download, text="Start Download", command=start_download)
    start_button.pack(pady=5)

    download.mainloop()


if __name__ == "__main__":
    ui()
