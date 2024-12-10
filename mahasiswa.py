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
