#Numpy Bölümü
import numpy as np
matris = np.random.randint(0, 101, size=(5, 5))
print("Oluşturulan Matris:")
print(matris)

ortalama = matris.mean()
standart_sapma = matris.std()
varyans = matris.var()

print("\nMatrisin İstatistikleri:")
print(f"Ortalama: {ortalama:.2f}")
print(f"Standart Sapma: {standart_sapma:.2f}")
print(f"Varyans: {varyans:.2f}")

en_buyuk_deger = matris.max()
en_kucuk_deger = matris.min()

print(f"\nEn Büyük Değer: {en_buyuk_deger}")
print(f"En Küçük Değer: {en_kucuk_deger}")

kosegen_toplami = np.trace(matris)
print(f"\nKöşegen Elemanlarinin Toplami: {kosegen_toplami}")

puanlar = np.random.normal(loc=70, scale=15, size=1000)
puanlar = np.clip(puanlar, 0, 100)
ortalama_puan = np.mean(puanlar)
medyan_puan = np.median(puanlar)
standart_sapma_puan = np.std(puanlar)

print("\nSimüle Edilen Puanlarin İstatistikleri:")
print(f"Ortalama: {ortalama_puan:.2f}")
print(f"Medyan: {medyan_puan:.2f}")
print(f"Standart Sapma: {standart_sapma_puan:.2f}")

dusuk_puanlar = puanlar < 50
dusuk_puan_sayisi = np.sum(dusuk_puanlar)
print(f"\n50'den düşük alan öğrenci sayısı: {dusuk_puan_sayisi}")



#Pandas Bölümü
import pandas as pd

veri = {
    'Öğrenci': ['Ali', 'Ayşe', 'Mehmet', 'Zeynep', 'Ahmet'],
    'Yaş': [20, 21, 19, 22, 20],
    'Bölüm': ['Bilgisayar', 'Fizik', 'Kimya', 'Bilgisayar', 'Fizik'],
    'Matematik': [70, 60, 80, 90, 55],
    'Fizik': [65, 75, 70, 85, 60],
    'Kimya': [80, 85, 65, 95, 70]
}

df = pd.DataFrame(veri)

print("Oluşturulan DataFrame:")
print(df)

ortalama_matematik = df['Matematik'].mean()
ortalama_fizik = df['Fizik'].mean()
ortalama_kimya = df['Kimya'].mean()

print("\nDerslere Göre Ortalama Puanlar:")
print(f"Matematik Ortalaması: {ortalama_matematik:.2f}")
print(f"Fizik Ortalamasi: {ortalama_fizik:.2f}")
print(f"Kimya Ortalamas: {ortalama_kimya:.2f}")
en_yuksek_mat_notu = df['Matematik'].max()
en_yuksek_mat_ogrenci = df[df['Matematik'] == en_yuksek_mat_notu]

print("\nEn Yüksek Matematik Notunu Alan Öğrenci:")
print(en_yuksek_mat_ogrenci)
df['Not_Ortalaması'] = df[['Matematik', 'Fizik', 'Kimya']].mean(axis=1)

print("\nOrtalama Not Sütunu Eklenmiş DataFrame:")
print(df)
bolum_basarilari = df.groupby('Bölüm')[['Matematik', 'Fizik', 'Kimya', 'Not_Ortalaması']].mean()

print("\nBölümlere Göre Ortalama Başarılar:")
print(bolum_basarilari)
yuksek_notlu_ogrenciler = df[df['Not_Ortalaması'] >= 70]

print("\nOrtalaması 70 ve Üzeri Olan Öğrenciler:")
print(yuksek_notlu_ogrenciler)