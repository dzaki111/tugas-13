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
