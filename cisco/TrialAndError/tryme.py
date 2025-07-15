
def hitung_luas_persegi_panjang(panjang, lebar, *, satuan="cm²"):
  luas = panjang * lebar
  print(f"Luas persegi panjang adalah {luas} {satuan}")
  print("luas persegi panjang", luas + satuan)
  
hitung_luas_persegi_panjang(5, 3, satuan="m²")