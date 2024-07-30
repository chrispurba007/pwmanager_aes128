import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        # Label dan entri untuk kata sandi
        self.label_password = tk.Label(master, text="Kata Sandi:")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack(pady=5)

        # Label untuk menampilkan kata sandi dekripsi
        self.label_display_password = tk.Label(master, text="Kata Sandi Dekripsi:")
        self.label_display_password.pack(pady=5)
        self.display_password = tk.Label(master, text="")  # Label kosong untuk menampilkan kata sandi
        self.display_password.pack(pady=5)

        # Tombol untuk generate, simpan, load key, simpan, dan ambil kata sandi
        self.generate_button = tk.Button(master, text="Generate Key", command=self.generate_key_iv)
        self.generate_button.pack(pady=10)
        self.save_key_button = tk.Button(master, text="Simpan Key", command=self.save_key_iv)
        self.save_key_button.pack(pady=10)
        self.load_key_button = tk.Button(master, text="Load Key", command=self.load_key_iv)
        self.load_key_button.pack(pady=10)
        self.save_password_button = tk.Button(master, text="Simpan Kata Sandi", command=self.save_password)
        self.save_password_button.pack(pady=10)
        self.load_password_button = tk.Button(master, text="Ambil Kata Sandi", command=self.load_password)
        self.load_password_button.pack(pady=10)

        # Variabel untuk menyimpan kunci AES dan IV
        self.key = None
        self.iv = None

    def generate_key_iv(self):
        # Generate kunci dan IV (Initialization Vector) AES
        self.key = os.urandom(16)  # 16 byte untuk AES-128
        self.iv = os.urandom(16)   # 16 byte untuk IV
        messagebox.showinfo("Sukses", "Key dan IV berhasil digenerate!")

    def save_key_iv(self):
        if not self.key or not self.iv:
            messagebox.showerror("Error", "Generate key dan IV terlebih dahulu.")
            return

        # Simpan kunci dan IV ke file
        file_path = filedialog.asksaveasfilename(defaultextension=".key", filetypes=[("Key files", "*.key")])
        if file_path:
            with open(file_path, 'wb') as file:
                file.write(self.key + self.iv)

            messagebox.showinfo("Sukses", "Key dan IV berhasil disimpan!")

    def load_key_iv(self):
        # Pilih file untuk memuat kunci dan IV
        file_path = filedialog.askopenfilename(filetypes=[("Key files", "*.key")])
        if not file_path:
            return

        # Baca kunci dan IV dari file
        with open(file_path, 'rb') as file:
            data = file.read()

        self.key = data[:16]  # 16 byte pertama adalah kunci
        self.iv = data[16:32]  # 16 byte berikutnya adalah IV

        messagebox.showinfo("Sukses", "Key dan IV berhasil diambil!")

    def save_password(self):
        # Ambil kata sandi dari entri
        password = self.entry_password.get()
        if not password:
            messagebox.showerror("Error", "Kata sandi tidak boleh kosong.")
            return

        # Pastikan kunci dan IV sudah di-generate atau di-load
        if not self.key or not self.iv:
            messagebox.showerror("Error", "Generate atau load key dan IV terlebih dahulu.")
            return

        # Enkripsi kata sandi
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padded_password = password.encode() + b"\0" * (16 - len(password) % 16)  # Padding
        encrypted_password = encryptor.update(padded_password) + encryptor.finalize()

        # Simpan kata sandi terenkripsi ke file
        file_path = filedialog.asksaveasfilename(defaultextension=".enc", filetypes=[("Encrypted files", "*.enc")])
        if file_path:
            with open(file_path, 'wb') as file:
                file.write(encrypted_password)

            messagebox.showinfo("Sukses", "Kata sandi berhasil disimpan!")

    def load_password(self):
        # Pilih file untuk memuat kata sandi terenkripsi
        file_path = filedialog.askopenfilename(filetypes=[("Encrypted files", "*.enc")])
        if not file_path:
            return

        # Pastikan kunci dan IV sudah di-load
        if not self.key or not self.iv:
            messagebox.showerror("Error", "Load key dan IV terlebih dahulu.")
            return

        # Baca kata sandi terenkripsi dari file
        with open(file_path, 'rb') as file:
            encrypted_password = file.read()

        # Dekripsi kata sandi
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_password = decryptor.update(encrypted_password) + decryptor.finalize()
        decrypted_password = decrypted_password.rstrip(b"\0").decode()  # Hapus padding dan dekode

        # Tampilkan kata sandi di entri teks
        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(0, "*" * len(decrypted_password))  # Menampilkan sebagai ***** di entri
        self.display_password.config(text=decrypted_password)  # Menampilkan kata sandi sebenarnya di label
        messagebox.showinfo("Sukses", "Kata sandi berhasil diambil!")

# Jalankan aplikasi
root = tk.Tk()
password_manager = PasswordManager(root)
root.mainloop()
