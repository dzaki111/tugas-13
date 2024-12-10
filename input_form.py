class InputForm:
    @staticmethod
    def input_mahasiswa():
        print("\n=== Form Input Mahasiswa ===")
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")
        return nim, nama, jurusan
