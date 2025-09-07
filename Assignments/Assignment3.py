#Question1
grades = [85, 92, 76, 92, 100, 76, 85, 92]
unique = list(set(grades))
highest = max(grades)
lowest = min(grades)
sorted_grades = sorted(unique)
print("Unique:", unique)
print("Highest:", highest)
print("Lowest:", lowest)
print("Sorted:", sorted_grades)


#Question2 
def is_armstrong(num):
    digits = str(num)
    total = sum(int(d)**3 for d in digits)
    return total == num
print(153, "Armstrong?", is_armstrong(153))
print(370, "Armstrong?", is_armstrong(370))
print(123, "Armstrong?", is_armstrong(123))


#Question3
A = {"Python", "R", "SQL", "Java"}
B = {"C++", "Python", "JavaScript", "SQL"}
common = A & B
only_A = A - B
union = sorted(A | B)
print("Common:", common)
print("Only in A:", only_A)
print("Union:", union)


#Question4
import random
import statistics
numbers = [random.randint(1, 100) for _ in range(10)]
mean = statistics.mean(numbers)
stdDev = statistics.stdev(numbers)
print("Numbers:", numbers)
print("Mean:", mean)
print("Standard Deviation:", stdDev)


#Question5
def wordCounter(text):
    words = text.split()
    total = len(words)
    longest = max(words, key=len)
    mostCommon = max(set(words), key=words.count)
    return total, longest, mostCommon
text = "python data science"
print(wordCounter(text))


#Question6
numbers = [5, 12, 7, 18, 24, 3, 16]
evens = list(filter(lambda x: x % 2 == 0, numbers))
squares = list(map(lambda x: x**2, evens))
sorted_squares = sorted(squares, reverse=True)
print("Evens:", evens)
print("Squares:", squares)
print("Descending:", sorted_squares)


#Question7
words = ["data", "science", "analysis", "artificialintelligence", "python"]
sortedWords = sorted(words, key=lambda x: len(x))
print("Sorted:", sortedWords)


#Question8
def digitSum(text):
    digits = [int(ch) for ch in text if ch.isdigit()]
    return sum(digits)
print(digitSum("abc12def3"))


#Question9
import numpy as np
arr = np.random.randint(0, 51, 10)
mean = np.mean(arr)
std_dev = np.std(arr)
maximum = np.max(arr)
print("Array:", arr)
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Max Value:", maximum)


#Question10
matrix = np.random.rand(5, 5)
colMeans = np.mean(matrix, axis=0)
binaryMatrix = (matrix > 0.5).astype(int)
print("Matrix:\n", matrix)
print("\nColumn Means:", colMeans)
print("\nBinary Matrix:\n", binaryMatrix)


#Project
import statistics
import random
kitaplar = [
    {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
    {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 2020},
    {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
    {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
    {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
    {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, "yil": 2021},
    {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]
def en_cok_satan(kitaplar):
    return max(kitaplar, key=lambda x: x["satis"])

def yazar_satislari(kitaplar):
    sozluk = {}
    for k in kitaplar:
        sozluk[k["yazar"]] = sozluk.get(k["yazar"], 0) + k["satis"]
    return sozluk

turler = {k["tur"] for k in kitaplar}
bin_ustu = [k["isim"] for k in kitaplar if k["satis"] > 1000]

sonrasi_2020 = list(filter(lambda x: x["yil"] > 2020, kitaplar))
artisli_satis = list(map(lambda x: x["satis"] * 1.1, kitaplar))
sirali = sorted(kitaplar, key=lambda x: x["satis"], reverse=True)

satislar = [k["satis"] for k in kitaplar]
ortalama = statistics.mean(satislar)
standart_sapma = statistics.stdev(satislar)

tur_satislari = {}
for k in kitaplar:
    tur_satislari[k["tur"]] = tur_satislari.get(k["tur"], 0) + k["satis"]
en_cok_tur = max(tur_satislari, key=tur_satislari.get)

train_size = int(len(kitaplar) * 0.7)
train = random.sample(kitaplar, train_size)
test = [k for k in kitaplar if k not in train]

train_satislar = [k["satis"] for k in train]
train_ortalama = statistics.mean(train_satislar)

test_ustu = [k["isim"] for k in test if k["satis"] > train_ortalama]

print("En çok satan kitap:", en_cok_satan(kitaplar)["isim"])
print("Yazar satışları:", yazar_satislari(kitaplar))
print("Türler:", turler)
print("1000’den fazla satan kitaplar:", bin_ustu)
print("2020’den sonra çıkan kitaplar:", [k["isim"] for k in sonrasi_2020])
print("Satış +%10:", [round(x) for x in artisli_satis])
print("Satışa göre sıralı:", [k["isim"] for k in sirali])
print("Ortalama satış:", round(ortalama, 2))
print("Standart sapma:", round(standart_sapma, 2))
print("En çok satış yapan tür:", en_cok_tur)
print("\n--- Train/Test Simülasyonu ---")
print("Train set ortalama satış:", round(train_ortalama, 2))
print("Test set kitapları:", [k["isim"] for k in test])
print("Train ortalamasının üstünde satan test kitapları:", test_ustu)