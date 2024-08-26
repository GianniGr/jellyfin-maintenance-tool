import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pytubefix import YouTube

class FileRenamerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")

        # Variables for folder renaming
        self.folder_path = tk.StringVar()

        # Variables for MP3 renaming
        self.mp3_folder_path = tk.StringVar()
        self.new_mp3_name = tk.StringVar()

        # Variables for folder creation
        self.base_path = tk.StringVar()
        self.new_folder_name = tk.StringVar()
        self.number_of_subfolders = tk.IntVar()

        # Variables for YouTube to MP3 downloader
        self.youtube_link = tk.StringVar()
        self.download_path = tk.StringVar()
        self.youtube_mp3_name = tk.StringVar(value="theme")  # Default name is "theme"

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Side menu
        side_menu = tk.Frame(main_frame, bg="lightgray", width=150)
        side_menu.pack(side=tk.LEFT, fill=tk.Y)

        folder_rename_button = tk.Button(side_menu, text="Folder Renamer", command=self.show_folder_rename)
        folder_rename_button.pack(pady=10)

        mp3_rename_button = tk.Button(side_menu, text="MP3 Renamer", command=self.show_mp3_rename)
        mp3_rename_button.pack(pady=10)

        folder_creator_button = tk.Button(side_menu, text="Folder Creator", command=self.show_folder_creator)
        folder_creator_button.pack(pady=10)

        youtube_downloader_button = tk.Button(side_menu, text="YouTube to MP3", command=self.show_youtube_downloader)
        youtube_downloader_button.pack(pady=10)

        # Content frame
        self.content_frame = tk.Frame(main_frame)
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Folder rename tab
        self.folder_rename_tab = tk.Frame(self.content_frame)
        folder_title_label = tk.Label(self.folder_rename_tab, text="Folder Renamer", font=("Arial", 14, "bold"))
        folder_title_label.grid(row=0, column=0, columnspan=3, pady=10)

        folder_label = tk.Label(self.folder_rename_tab, text="Folder Path:")
        folder_label.grid(row=1, column=0, sticky=tk.W)

        folder_entry = tk.Entry(self.folder_rename_tab, textvariable=self.folder_path, width=50)
        folder_entry.grid(row=1, column=1, padx=5, pady=5)

        browse_button = tk.Button(self.folder_rename_tab, text="Browse...", command=self.select_folder)
        browse_button.grid(row=1, column=2, padx=5, pady=5)

        rename_button = tk.Button(self.folder_rename_tab, text="Rename Files", command=self.rename_files)
        rename_button.grid(row=2, column=0, columnspan=3, pady=10)

        # MP3 rename tab
        self.mp3_rename_tab = tk.Frame(self.content_frame)
        mp3_title_label = tk.Label(self.mp3_rename_tab, text="MP3 Renamer", font=("Arial", 14, "bold"))
        mp3_title_label.grid(row=0, column=0, columnspan=3, pady=10)

        mp3_folder_label = tk.Label(self.mp3_rename_tab, text="Folder Path:")
        mp3_folder_label.grid(row=1, column=0, sticky=tk.W)

        mp3_folder_entry = tk.Entry(self.mp3_rename_tab, textvariable=self.mp3_folder_path, width=50)
        mp3_folder_entry.grid(row=1, column=1, padx=5, pady=5)

        mp3_browse_button = tk.Button(self.mp3_rename_tab, text="Browse...", command=self.select_mp3_folder)
        mp3_browse_button.grid(row=1, column=2, padx=5, pady=5)

        new_name_label = tk.Label(self.mp3_rename_tab, text="New Name:")
        new_name_label.grid(row=2, column=0, sticky=tk.W)

        new_name_entry = tk.Entry(self.mp3_rename_tab, textvariable=self.new_mp3_name, width=30)
        new_name_entry.insert(0, "theme")  # Set default value
        new_name_entry.grid(row=2, column=1, padx=5, pady=5)

        rename_mp3_button = tk.Button(self.mp3_rename_tab, text="Rename MP3 Files", command=self.rename_mp3_to_theme)
        rename_mp3_button.grid(row=3, column=0, columnspan=3, pady=10)

        # Folder creator tab
        self.folder_creator_tab = tk.Frame(self.content_frame)
        creator_title_label = tk.Label(self.folder_creator_tab, text="Folder Creator", font=("Arial", 14, "bold"))
        creator_title_label.grid(row=0, column=0, columnspan=3, pady=10)

        base_path_label = tk.Label(self.folder_creator_tab, text="Base Path:")
        base_path_label.grid(row=1, column=0, sticky=tk.W)

        base_path_entry = tk.Entry(self.folder_creator_tab, textvariable=self.base_path, width=50)
        base_path_entry.grid(row=1, column=1, padx=5, pady=5)

        base_browse_button = tk.Button(self.folder_creator_tab, text="Browse...", command=self.select_base_path)
        base_browse_button.grid(row=1, column=2, padx=5, pady=5)

        new_folder_name_label = tk.Label(self.folder_creator_tab, text="New Folder Name:")
        new_folder_name_label.grid(row=2, column=0, sticky=tk.W)

        new_folder_name_entry = tk.Entry(self.folder_creator_tab, textvariable=self.new_folder_name, width=30)
        new_folder_name_entry.grid(row=2, column=1, padx=5, pady=5)

        number_of_subfolders_label = tk.Label(self.folder_creator_tab, text="Number of Subfolders:")
        number_of_subfolders_label.grid(row=3, column=0, sticky=tk.W)

        number_of_subfolders_entry = tk.Entry(self.folder_creator_tab, textvariable=self.number_of_subfolders, width=10)
        number_of_subfolders_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        create_button = tk.Button(self.folder_creator_tab, text="Create Folders", command=self.create_folders)
        create_button.grid(row=4, column=0, columnspan=3, pady=10)

        # YouTube to MP3 downloader tab
        self.youtube_downloader_tab = tk.Frame(self.content_frame)
        downloader_title_label = tk.Label(self.youtube_downloader_tab, text="YouTube to MP3 Downloader", font=("Arial", 14, "bold"))
        downloader_title_label.grid(row=0, column=0, columnspan=3, pady=10)

        youtube_link_label = tk.Label(self.youtube_downloader_tab, text="YouTube Link:")
        youtube_link_label.grid(row=1, column=0, sticky=tk.W)

        youtube_link_entry = tk.Entry(self.youtube_downloader_tab, textvariable=self.youtube_link, width=50)
        youtube_link_entry.grid(row=1, column=1, padx=5, pady=5)

        download_path_label = tk.Label(self.youtube_downloader_tab, text="Download Path:")
        download_path_label.grid(row=2, column=0, sticky=tk.W)

        download_path_entry = tk.Entry(self.youtube_downloader_tab, textvariable=self.download_path, width=50)
        download_path_entry.grid(row=2, column=1, padx=5, pady=5)

        browse_button = tk.Button(self.youtube_downloader_tab, text="Browse...", command=self.select_download_path)
        browse_button.grid(row=2, column=2, padx=5, pady=5)

        mp3_name_label = tk.Label(self.youtube_downloader_tab, text="MP3 Name:")
        mp3_name_label.grid(row=3, column=0, sticky=tk.W)

        mp3_name_entry = tk.Entry(self.youtube_downloader_tab, textvariable=self.youtube_mp3_name, width=30)
        mp3_name_entry.grid(row=3, column=1, padx=5, pady=5)

        download_button = tk.Button(self.youtube_downloader_tab, text="Download MP3", command=self.download_song_from_youtube)
        download_button.grid(row=4, column=0, columnspan=3, pady=10)

        # Show folder rename tab by default
        self.show_folder_rename()

    def show_folder_rename(self):
        self.folder_rename_tab.pack(fill=tk.BOTH, expand=True)
        self.mp3_rename_tab.pack_forget()
        self.folder_creator_tab.pack_forget()
        self.youtube_downloader_tab.pack_forget()

    def show_mp3_rename(self):
        self.mp3_rename_tab.pack(fill=tk.BOTH, expand=True)
        self.folder_rename_tab.pack_forget()
        self.folder_creator_tab.pack_forget()
        self.youtube_downloader_tab.pack_forget()

    def show_folder_creator(self):
        self.folder_creator_tab.pack(fill=tk.BOTH, expand=True)
        self.folder_rename_tab.pack_forget()
        self.mp3_rename_tab.pack_forget()
        self.youtube_downloader_tab.pack_forget()

    def show_youtube_downloader(self):
        self.youtube_downloader_tab.pack(fill=tk.BOTH, expand=True)
        self.folder_rename_tab.pack_forget()
        self.mp3_rename_tab.pack_forget()
        self.folder_creator_tab.pack_forget()

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)

    def rename_files(self):
        if self.folder_path.get():
            self.rename_files_in_folder(self.folder_path.get())
            messagebox.showinfo("Success", "Files renamed successfully!")
        else:
            messagebox.showwarning("Warning", "Please select a folder first.")

    def rename_files_in_folder(self, folder_path):
        if not os.path.isdir(folder_path):
            print(f"{folder_path} is not a valid directory.")
            return

        for root, _, files in os.walk(folder_path):
            for file_name in files:
                base_name, extension = os.path.splitext(file_name)
                new_base_name = base_name.replace('.', ' ')
                new_file_name = new_base_name + extension
                old_file_path = os.path.join(root, file_name)
                new_file_path = os.path.join(root, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")

    def select_mp3_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.mp3_folder_path.set(folder_selected)

    def rename_mp3_to_theme(self):
        folder_path = self.mp3_folder_path.get()
        new_name = self.new_mp3_name.get().strip()
        if not folder_path or not new_name:
            messagebox.showwarning("Warning", "Please provide folder path and new name.")
            return

        if not os.path.isdir(folder_path):
            messagebox.showwarning("Warning", "Invalid folder path.")
            return

        for root, _, files in os.walk(folder_path):
            for file_name in files:
                if file_name.endswith('.mp3'):
                    old_file_path = os.path.join(root, file_name)
                    new_file_name = new_name + '.mp3'
                    new_file_path = os.path.join(root, new_file_name)
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {old_file_path} -> {new_file_path}")
        messagebox.showinfo("Success", "MP3 files renamed successfully!")

    def select_base_path(self):
        path_selected = filedialog.askdirectory()
        if path_selected:
            self.base_path.set(path_selected)

    def create_folders(self):
        base_path = self.base_path.get()
        new_folder_name = self.new_folder_name.get().strip()
        number_of_subfolders = self.number_of_subfolders.get()

        if not base_path or not new_folder_name or not number_of_subfolders:
            messagebox.showwarning("Warning", "Please fill in all fields.")
            return

        new_folder_path = os.path.join(base_path, new_folder_name)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        for i in range(1, number_of_subfolders + 1):
            subfolder_name = f"Season {i:02}"
            subfolder_path = os.path.join(new_folder_path, subfolder_name)
            os.makedirs(subfolder_path)

        messagebox.showinfo("Success", "Folders created successfully!")

    def select_download_path(self):
        path_selected = filedialog.askdirectory()
        if path_selected:
            self.download_path.set(path_selected)

    def download_song_from_youtube(self):
        youtube_link = self.youtube_link.get().strip()
        download_path = self.download_path.get().strip()
        mp3_name = self.youtube_mp3_name.get().strip()

        if not youtube_link or not download_path or not mp3_name:
            messagebox.showwarning("Warning", "Please provide a YouTube link, download path, and MP3 name.")
            return

        try:
            yt = YouTube(youtube_link)
            audio_stream = yt.streams.filter(only_audio=True).first()
            output_file = audio_stream.download(output_path=download_path)
            new_file = os.path.join(download_path, mp3_name + '.mp3')
            os.rename(output_file, new_file)
            messagebox.showinfo("Success", "MP3 downloaded and saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download MP3: {e}")

# Main entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamerGUI(root)
    root.mainloop()
