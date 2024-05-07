# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Oleh karena itu, ia membutuhkan pengetahuan seorang praktisi data untuk memberikan insight dari data yang ada dan mengidentifikasi berbagai faktor attrition. Harapannya insight ini dapat digunakan untuk mempermudah dalam mengelola karyawan agar terhindar dari tingginya Attrtion rate, serta memberikan model predict Attrition berdasarkan faktor penyebab terbesar attrition. 

### Permasalahan Bisnis
Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan, hingga mengakibatkan Tingginya Attrition rate pada perusahaan.
- Berapa total karyawan pada perusahaan Jaya Jaya Maju?
- Berapa total karyawan yang menetap pada perusahaan Jaya Jaya Maju?
- Berapa total karyawan yang keluar pada perusahaan Jaya Jaya Maju?
- Berapa total karyawan tanpa keterangan pada perusahaan Jaya Jaya Maju?
- Berapa persentase karyawan pada perusahaan Jaya Jaya Maju?
- Bagaimana distribusi tingkat atrisi diantara berbagai departemen perusahaan?
- Bagaimana korelasi antara tingkat kepuasan kerja (Job Satisfaction) dan tingkat atrisi?
- Bagaimana distribusi tingkat atrisi diantara berbagai tingkat jabatan (Job Level)?
- Bagaimana korelasi antara usia karyawan dan tingkat atrisi?
- Bagaimana korelasi antara tingkat pendidikan (Education) dan tingkat atrisi?
- Berapa besar pengaruh jarak ke kantor terhadap tingkat atrisi?
- Berapa besar pengaruh tingkat keseimbangan kerja-hidup (Work-Life Balance) terhadap tingkat atrisi?
- Berapa besar pengaruh atrisi antara karyawan yang melakukan lembur (Overtime) dan yang tidak?
- Berapa besar pengaruh tingkat gaji (Monthly Income) terhadap tingkat atrisi?
- Berapa besar pengaruh tarif bulanan (Monthly Rate) terhadap tingkat atrisi?
- Berapa besar pengaruh tarif harian (Daily Rate) terhadap tingkat atrisi?
- Berapa besar pengaruh tarif perjam (Hourly Rate) terhadap tingkat atrisi?
- Faktor terbesar penyebab attrition karyawan?

### Cakupan Proyek
 
Proyek ini akan mencakup pengidentifikasian berbagai faktor yang mempengaruhi tingginya attrition rate, pembuatan business dashboard untuk memonitori faktor tingginya attrition rate, melakukan proses EDA(Exploratory Data Analysis) dengan menerapkan random_forest untuk mendapatkan analisa model machine learning terhadap faktor terbesar Attrition. 

### Persiapan

Sumber data: Supabase URL = postgresql://postgres.jyqrgkrhrxennxlqywpl:human_resources123@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres

Setup environment:

```
pip install pandas numpy matplotlib jupyter sqlalchemy scikit-learn imbalanced-learn joblib
```

## Business Dashboard

Business dashboard Human Resources terdiri dari question type: Number, Pie, Bar dan Row.
diawali dari,
1. Total karyawan pada perusahaan Jaya Jaya Maju yaitu 1470
2. Total karyawan yang menetap pada perusahaan Jaya Jaya Maju yaitu 879
3. Total karyawan yang keluar pada perusahaan Jaya Jaya Maju yaitu 179
4. Total karyawan tanpa keterangan pada perusahaan Jaya Jaya Maju yaitu 412
5. Persentase karyawan pada perusahaan Jaya Jaya Maju (menetap sebesar 60%, keluar sebesar 12%, tanpa keterangan sebesar 28%)
6. Distribusi attrition berdasarkan dapartement perusahaan (Human Resources sebesar 3.35%, Research&Development sebesar 59.78% dan Sales sebesar 36.87%) dari total Attrition 179
7. Korelasi Job Satisfaction dan Attrition dimana disetiap tingkat mulai dari tingkat 1 sampai 4 memiliki tingkat Attrition lebih dari 32 dan tertinggi berada pada tingkat 3 yang memiliki Attrition sebanyak 62
8. Distribusi attrition berdasarkan job level tersebar di 5 level dimana tingkat attrition tertinggi berada pada level 1 sebanyak 108 attrition dan keemapat level lainnya kurang dari 32 attrition
9. Korelasi usia dan attrition dimana disetiap kelompok usia memiliki tingkat attrition lebih dari 5 dan tertinggi berada pada kelompok usia 30-35 disusul kelompok usia 25-30 yang memiliki tingkat attrition lebih dari 40
10. Korelasi education dan attrition dimana disetiap tingkat education terdapat attrition yang didominasi oleh tingkat 3 education yaitu Bachelor dan yang terendah berada pada tingkat 5 education 
11. Pengaruh jarak kantor dari rumah dimana disetiap kelompok jarak terdapat attrition yang menunjukkan faktor jarak memang berpengaruh terhadap attrition, tertinggi berada pada jarak 0-5km dan terendah berada pada 25-30km 
12. Pengaruh Work Life Balance terhadap attrition didominasi oleh level 3 yaitu Excellent sebanyak 53%, disusul oleh level 2 Good sebanyak 25%, lalu level 4 Outstanding sebanyak 12%, dan yang terendah berada pada level 1 Low sebanyak 10% 
13. Pengaruh Overtime terhadap attrition menunjukkan 55% attrition menyatakan Overtime dan 45% menyatakan tidak 
14. Pengaruh monthly income terhadap attrition didominasi oleh kelompok gaji rendah yaitu 2500-5000 memiliki attrition lebih dari 60 dan yang terendah berada pada kelompok  gaji tinggi yaitu 12500-15000
15. Pengaruh Monthly rate terhadap attrition dimana rata rata attrition 30an berada pada kelompok tarif rendah sampai kelompok sedang yaitu 0-25000 dan attrition terendah berada pada kelompok tarif tinggi yaitu 25000-30000 sebanyak 14 attrition
16. Pengaruh daily rate terhadap attrition dimana disetiap kelompok tarif terdapat attrition menunjukkan faktor daily rate memang berpengaruh terhadap attrition, yang terendah berada pada kelompok tarif tinggi yaitu 1400-1600
17. Pengaruh hourly rate terhadap attrition dimana disetiap kelompok tarif terdapat attrition menunjukkan faktor hourly rate memang berpengaruh terhadap attrition, yang terendah berada pada kelompok tarif tinggi yaitu 100-110

Dashboard Human Resources pada metabase:
username: root@mail.com
password: root123

## Conclusion

Perusahaan jaya jaya maju memiliki 1470 karyawan dimana sebanyak 12% karyawan keluar dari total keseluruhan karyawan, Tersebar pada departement Human Resources sebesar 3.35%, Research&Development sebesar 59.78% dan Sales sebesar 36.87% dari total 179 karyawan yang keluar. Attrition disebabkan oleh beberapa faktor, berdasarkan hasil analisa model machine learning random forest faktor penyebab attrition terbesar yaitu MonthlyIncome, Age, MonthlyRate, DailyRate, TotalWorkingYears, HourlyRate, dan DistanceFromHome. 

### Rekomendasi Action Items (Optional)

- Untuk mengurangi attrition rate, manajer departemen HR dapat memprioritaskan pengecekan dan perbaikan pada faktor penyebab attrition terbesar
- Manajer departemen HR dapat menggunakan model predict untuk memprediksi kemungkinan karyawan akan keluar atau menetap berdasarkan faktor penyebab attrition terbesar
