# Variabel global
initial_population = 1  # Jumlah bakteri awal
growth_rate = 2         # Faktor pertumbuhan (setiap generasi jumlahnya menjadi dua)
generations = 5         # Jumlah generasi

# Fungsi rekursif untuk menghitung populasi
def calculate_population(generations):
    if generations == 0:
        return initial_population
    else:
        return growth_rate * calculate_population(generations - 1)

# Fungsi untuk mengklasifikasikan bakteri berdasarkan jenis
def classify_bacteria(bacteria_type):
    bacteria_classes = {
        "E. coli": "Bakteri Gram-negatif",
        "Staphylococcus": "Bakteri Gram-positif",
        "Lactobacillus": "Bakteri Asam Laktat",
        "Bacillus": "Bakteri Spora",
    }
    # Menggunakan lambda untuk mencari jenis bakteri
    classify = lambda x: bacteria_classes.get(x, "Jenis bakteri tidak dikenal")
    return classify(bacteria_type)

# Fungsi utama
def main():
    # Menghitung populasi bakteri
    total_population = calculate_population(generations)
    print(f"Jumlah bakteri setelah {generations} generasi: {total_population}")

    # Mengklasifikasikan bakteri
    bacteria_input = input("Masukkan nama bakteri untuk klasifikasi (E. coli, Staphylococcus, Lactobacillus, Bacillus): ")
    classification = classify_bacteria(bacteria_input)
    print(f"Klasifikasi untuk {bacteria_input}: {classification}")

# Menjalankan program utama
if __name__ == "__main__":
    main()
