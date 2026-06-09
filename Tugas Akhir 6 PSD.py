class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.kode_buku = None
        self.nomor_rak = None
        self.state = SlotState.EMPTY


class Perpustakaan:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, kode_buku):
        return (kode_buku % self.SIZE + self.SIZE) % self.SIZE

    def tambah_buku(self, kode_buku, nomor_rak):
        idx = self.hash_function(kode_buku)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].kode_buku == kode_buku:
                    self.table[i].nomor_rak = nomor_rak
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].kode_buku = kode_buku
                self.table[i].nomor_rak = nomor_rak
                self.table[i].state = SlotState.OCCUPIED
                return True
        return False

    def cari(self, kode_buku):
        idx = self.hash_function(kode_buku)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if (self.table[i].state == SlotState.OCCUPIED and
                    self.table[i].kode_buku == kode_buku):
                return self.table[i]

        return None

    def hapus(self, kode_buku):
        buku = self.cari(kode_buku)

        if buku is None:
            return False

        buku.state = SlotState.DELETED
        return True

    def tampilkan(self):
        print("\nDaftar Penyimpanan Buku:")

        for i in range(self.SIZE):
            print(f"{i}: ", end="")

            if self.table[i].state == SlotState.EMPTY:
                print("Kosong")

            elif self.table[i].state == SlotState.DELETED:
                print("Data Dihapus")

            else:
                print(f"Kode Buku {self.table[i].kode_buku} -> Rak {self.table[i].nomor_rak}")


def main():
    perpustakaan = Perpustakaan()

    perpustakaan.tambah_buku(101, "Rak A1")
    perpustakaan.tambah_buku(111, "Rak B2")
    perpustakaan.tambah_buku(121, "Rak C3")
    perpustakaan.tambah_buku(102, "Rak D1")
    perpustakaan.tampilkan()
    hasil = perpustakaan.cari(111)

    perpustakaan.hapus(101)
    print("\nSetelah menghapus key 11:")
    perpustakaan.tampilkan()

    hasil = perpustakaan.cari(102)
    if hasil is not None:
        print(f"\nBuku {hasil.kode_buku} ditemukan di {hasil.nomor_rak}")
    else:
        print("\nBuku tidak ditemukan:")


if __name__ == "__main__":
    main()