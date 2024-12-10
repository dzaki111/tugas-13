# tugas-13

# Proyek Mahasiswa - Sistem Informasi Mahasiswa

Ini adalah contoh proyek Python yang menggunakan konsep Object-Oriented Programming (OOP) untuk mengelola data mahasiswa.

## Struktur Folder

Berikut adalah struktur folder proyek ini:

```
├── view/
│   ├── mahasiswa.py  # Menampilkan data mahasiswa
│   ├── __init__.py   # Inisialisasi folder view sebagai package
├── data/
│   ├── mahasiswa.py  # Menyimpan data mahasiswa dan definisi class Mahasiswa
│   ├── __init__.py   # Inisialisasi folder data sebagai package
├── main.py  # Program utama untuk menampilkan menu utama
├── __init__.py  # Inisialisasi folder proyek sebagai package
```

## Deskripsi File

### 1. `data/mahasiswa.py`
File ini berisi model data mahasiswa dengan definisi kelas `Mahasiswa` dan `DataMahasiswa`. Kelas `Mahasiswa` berfungsi untuk mendefinisikan informasi mahasiswa seperti ID, nama, dan jurusan. Kelas `DataMahasiswa` digunakan untuk mengelola data mahasiswa (misalnya, menambah, menghapus, atau memperbarui data).
```python
class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}"

class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_data(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus_data(self, nim):
        self.data = [m for m in self.data if m.nim != nim]

    def ubah_data(self, nim, nama_baru, jurusan_baru):
        for m in self.data:
            if m.nim == nim:
                m.nama = nama_baru
                m.jurusan = jurusan_baru

    def cari_data(self, nim):
        for m in self.data:
            if m.nim == nim:
                return m
        return None

    def tampilkan_semua_data(self):
        return self.data

````
### 2. `view/mahasiswa.py`
File ini berisi kelas `ViewMahasiswa`, yang memiliki metode untuk menampilkan daftar mahasiswa dan detail mahasiswa.

- `tampilkan_list(data_mahasiswa)` : Menampilkan daftar semua mahasiswa.
- `tampilkan_detail(mahasiswa)` : Menampilkan detail informasi mahasiswa.
```python
class ViewMahasiswa:
    @staticmethod
    def tampilkan_list(data_mahasiswa):
        if not data_mahasiswa:
            print("Tidak ada data mahasiswa.")
        else:
            print("\n=== Daftar Mahasiswa ===")
            for mahasiswa in data_mahasiswa:
                print(mahasiswa)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print("\n=== Detail Mahasiswa ===")
            print(mahasiswa)
        else:
            print("\nMahasiswa tidak ditemukan.")

````
### 3. `main.py`
File ini adalah program utama yang menjalankan aplikasi dan menampilkan menu untuk berinteraksi dengan data mahasiswa.
```python
from data.mahasiswa import Mahasiswa, DataMahasiswa
from View.input_form import InputForm
from View.mahasiswa import ViewMahasiswa

def main():
    data_mahasiswa = DataMahasiswa()

    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Hapus Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Cari Data Mahasiswa")
        print("5. Tampilkan Semua Data")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_mahasiswa()
            mahasiswa = Mahasiswa(nim, nama, jurusan)
            data_mahasiswa.tambah_data(mahasiswa)
            print("Data berhasil ditambahkan.")
        elif pilihan == "2":
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            data_mahasiswa.hapus_data(nim)
            print("Data berhasil dihapus.")
        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
            nama_baru = input("Masukkan Nama baru: ")
            jurusan_baru = input("Masukkan Jurusan baru: ")
            data_mahasiswa.ubah_data(nim, nama_baru, jurusan_baru)
            print("Data berhasil diubah.")
        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang akan dicari: ")
            mahasiswa = data_mahasiswa.cari_data(nim)
            ViewMahasiswa.tampilkan_detail(mahasiswa)
        elif pilihan == "5":
            semua_data = data_mahasiswa.tampilkan_semua_data()
            ViewMahasiswa.tampilkan_list(semua_data)
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()

````
## Langkah-langkah Menggunakan Proyek

1. **Menjalankan Program**:
   Anda bisa menjalankan program utama dengan perintah berikut pada terminal atau command prompt:
   
   ```
   python main.py
   ```

2. **Menambah Data Mahasiswa**:
   Anda bisa menambah data mahasiswa melalui input yang ada di dalam kode atau menambahkannya secara langsung pada list `data_mahasiswa` di dalam `main.py`.

3. **Menampilkan Data Mahasiswa**:
   Program akan menampilkan daftar mahasiswa dan detail mahasiswa sesuai dengan yang diminta.

## Persyaratan Sistem

Pastikan Anda telah menginstal Python versi 3.x pada sistem Anda.

Untuk menginstal dependensi proyek ini (jika ada), Anda dapat menggunakan `pip`:

```
pip install -r requirements.txt
```

Namun, proyek ini tidak membutuhkan dependensi eksternal.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, Anda bisa membuat pull request atau menghubungi saya langsung.

Terima kasih telah menggunakan proyek ini!
