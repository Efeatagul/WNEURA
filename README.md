#  WNEURA v1.1: Multi-Dimensional Cognitive Simulation Platform

**Status:** Phase 1 (Steel Core) Validated  
**Field:** Computational Neuroscience / Bio-Inspired AI  

WNEURA, biyolojik beyin gelişimini ve karar verme süreçlerini dijital bir ortamda, çok boyutlu ve çok etkenli (multi-factorial) olarak simüle etmeyi hedefleyen nöroloji odaklı bir platformdur. 

v1.1 "Steel Core" aşaması, irade çöküşü (**Learned Helplessness**) ve stres dinamikleri (HPA-Axis) üzerine kurulmuştur.

---

## 🛠️ Core Engine Architecture (Motor Mimarisi)

Platform, üç temel biyolojik mekanizmanın matematiksel entegrasyonu ile çalışır:

| Mekanizma | Karşılığı | İşlev |
| :--- | :--- | :--- |
| **Amygdala** | Stres Motoru | Beklenti hatalarından (Surprise) Kortizol üretir. |
| **Agency ($W$)** | İrade Ağırlığı | Eylem ve sonuç arasındaki nedensellik inancını yönetir. |
| **Striatum** | Öğrenme Kapısı | İrade düşükse ödül gelse bile öğrenmeyi durdurur (Freeze). |

---

##  Validation Experiments (Bilimsel Kanıtlar)

Modelin biyolojik doğruluğu aşağıdaki üç deneyle kanıtlanmıştır:

### 1. Hysteresis Proof (Kalıcı Hasar)
Stres (Kortizol) ortadan kalksa bile, Agency (İrade) seviyesinin kendiliğinden düzelmediği kanıtlanmıştır. 
> **Gözlem:** Travma sonrası sistem "Çaresizlik" modunda kilitli kalır.

### 2. Uncertainty vs. Helplessness (Ayrışma)
Kaotik bir ortamda bile sağlıklı bir beyin öğrenmeye devam ederken, çaresiz bir beynin stabil ortamda bile "Donma" (Freezing) yaşadığı izlenmiştir.

### 3. Contingency Switch (Fırsat Körlüğü)
En kritik deneydir. Ortama devasa bir ödül (+10) eklendiğinde bile, çaresiz ajanın bu fırsatı fark edip motivasyonunu güncelleyemediği (Outcome Insensitivity) görülmüştür.

---

## Experimental Results (Grafikler)

Deney sonuçları `results/` klasöründe yer almaktadır. 

| Deney | Görsel Referans | Durum |
| :--- | :--- | :--- |
| **Hysteresis** | `results/figure_01_hysteresis.png` |  Başarılı |
| **Dissociation** | `results/figure_02_dissociation.png` |  Başarılı |
| **Contingency** | `results/figure_03_contingency.png` |  Başarılı |

---

##  Future Roadmap (Vizyon)

- [ ] **Phase 2:** Çoklu ajan etkileşimi (Sosyal Çaresizlik).
- [ ] **Phase 3:** Prefrontal Korteks simülasyonu (Üst Düzey Planlama).
- [ ] **Phase 4:** Gerçek zamanlı borsa ve veri akışları ile stres testi.

---

## 🛡️ License
Bu proje **MIT License** ile korunmaktadır. Bilimsel amaçlarla kullanılabilir ve geliştirilebilir.

**Developer:** [Efeatagul]
