# 🧠 WNEURA v1.2: Multi-Dimensional Cognitive Simulation Platform

**Status:** Phase 2 (Bridge System Ready) 🌉  
**Field:** Computational Neuroscience / Bio-Inspired AI  
**Integration:** Optimized for WSharp (C#) & External Control  

WNEURA, biyolojik beyin gelişimini ve karar verme süreçlerini dijital bir ortamda, çok boyutlu ve çok etkenli (multi-factorial) olarak simüle etmeyi hedefleyen nöroloji odaklı bir platformdur.

**v1.2 Sürümü**, sistemin dış yazılımlarla (özellikle WSharp) konuşabilmesi için **"Headless" (Arayüzsüz)** motor yapısına ve **JSON** veri protokolüne geçiş yapmıştır.

---

## 🛠️ Core Engine Architecture (Motor Mimarisi)

Platform, üç temel biyolojik mekanizmanın matematiksel entegrasyonu ile çalışır:

| Mekanizma | Karşılığı | İşlev |
| :--- | :--- | :--- |
| **Amygdala** | Stres Motoru | Beklenti hatalarından (Surprise) Kortizol üretir. |
| **Agency ($W$)** | İrade Ağırlığı | Eylem ve sonuç arasındaki nedensellik inancını yönetir. |
| **Striatum** | Öğrenme Kapısı | İrade düşükse ödül gelse bile öğrenmeyi durdurur (Freeze). |

---

## 🏗️ Technical Architecture: The Bridge System

WNEURA, "Mimar (C#) ve İnşaatçı (Python)" modeline göre tasarlanmıştır. Görsel arayüz açmak yerine, arka planda hesaplama yapar ve sonucu raporlar.

| Bileşen | Görev | Dosya |
| :--- | :--- | :--- |
| **Engine (Motor)** | Nörolojik hesaplamaları yapar (Agency, Cortisol). | `wneura/brain.py` |
| **Runner (Köprü)** | Dış dünyadan gelen emirleri (CLI) uygular. | `runner.py` |
| **Protocol** | Veri alışverişi formatı. | `JSON` |

---

## 🔌 Integration & Usage (Nasıl Kullanılır?)

WNEURA motorunu dışarıdan (Terminal veya WSharp içinden) çağırmak için `runner.py` kullanılır.

### 1. Komut Satırı (CLI) Komutu

```powershell
py runner.py --steps 100 --erosion 0.05 --stress_threshold 0.7 --output result.json
2. ParametrelerArgümanVarsayılanAçıklama--steps100Simülasyonun kaç adım süreceği.--erosion0.05İradenin zamanla aşınma hızı (Entropy).--repair0.01Başarılı eylem sonrası irade tamiri.--stress_threshold0.6Kortizolün tetiklendiği eşik.--outputresult.jsonSonucun yazılacağı dosya yolu.
```

📊 Output Protocol (JSON Çıktısı)Motor işini bitirdiğinde, entegre olduğu sisteme (WSharp) şu formatta bir rapor sunar:
```
{
    "status": "success",
    "final_stats": {
        "final_agency": 0.0,
        "final_cortisol": 1.0
    },
    "timeline": {
        "cortisol": [0.2, 0.5, 0.8, 1.0],
        "agency": [1.0, 0.8, 0.4, 0.0],
        "action": [1, 1, 0, 0]
    }
```
Agency 0.0: Öğrenilmiş çaresizlik (Pes etme).
Action 0: Donma tepkisi (Freezing)

.🔬 Validation Experiments (Bilimsel Kanıtlar)
Modelin biyolojik doğruluğu aşağıdaki üç deneyle kanıtlanmıştır
1. Hysteresis Proof (Kalıcı Hasar)Stres (Kortizol) ortadan kalksa bile, Agency (İrade) seviyesinin kendiliğinden düzelmediği kanıtlanmıştır.
```
        Gözlem: Travma sonrası sistem "Çaresizlik" modunda kilitli kalır
```
2. Uncertainty vs. Helplessness (Ayrışma)Kaotik bir ortamda bile sağlıklı bir beyin öğrenmeye devam ederken, çaresiz bir beynin stabil ortamda bile "Donma" (Freezing) yaşadığı izlenmiştir.

3. Contingency Switch (Fırsat Körlüğü)En kritik deneydir. Ortama devasa bir ödül (+10) eklendiğinde bile, çaresiz ajanın bu fırsatı fark edip motivasyonunu güncelleyemediği (Outcome Insensitivity) görülmüştür

 4. Therapy & Rehabilitation (Terapi Simülasyonu)
Travma sonrası iyileşme sürecinin (Recovery) dinamikleri `therapy.py` ile test edilmiştir.
> **Gözlem:** İradesi sıfırlanmış (Agency=0) bir ajana sürekli ödül verilse dahi, standart onarım hızında (Repair Rate: 0.01) iyileşme görülmemiştir. Ancak dış destekle onarım hızı artırıldığında (0.05) sistemin yavaşça tepki verdiği kanıtlanmıştır.

.📈 Experimental Results (Grafikler)
Deney sonuçları results/ klasöründe yer almaktadır.
```
Deney	      | Görsel Referans                      |	Durum
Hysteresis    | results/figure_01_hysteresis.png     |  Başarılı ✅
Dissociation  | results/figure_02_dissociation.png   |  Başarılı ✅
Contingency   | results/figure_03_contingency.png    |  Başarılı ✅
Therapy       | therapy.py (Terminal Log)            |  Başarılı ✅
```
 Future Roadmap (Vizyon)
 [x] Phase 1: Core Engine & Validation (Tamamlandı)
 [x] Phase 2: Headless Architecture & JSON Bridge (Tamamlandı)
 [ ] Phase 3: WSharp (C#) tam entegrasyonu ve Arayüz.
 [ ] Phase 4: Çoklu ajan etkileşimi (Sosyal Çaresizlik).
 [ ] Phase 5: Gerçek zamanlı borsa/veri akışları ile stres testi.
 
 🛡️ LicenseBu proje MIT License ile korunmaktadır. Bilimsel amaçlarla kullanılabilir ve geliştirilebilir.
Developer: [Efeatagul]
