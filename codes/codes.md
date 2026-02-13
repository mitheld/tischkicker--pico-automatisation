# 🔧 **Codes**

**Übersicht der Python‑Programme** *(src/ Ordner)*. Vollständige Dateien siehe src/.

---

## 🎥 **main_torerkennung.py**
- **Funktion**: Echtzeit‑Videoanalyse mit **OpenCV**.  
- **Ablauf**: Kamera liest Frame → **HSV‑Filter** → Konturen prüft Tore (**grün/rot**).  
- **Ausgabe**: Tor‑Event triggert LED‑Update.

## 💡 **main_toranzeige.py**
- **Funktion**: Steuert **WS2812B RGB‑Matrix**.  
- **Ablauf**: Tor‑Signal empfängt → Score zählt → LEDs färbt (**grün/rot**).  
- **Hardware**: Pi **GPIO Pin 18**.

## 🔢 **font_toranzeige.py**
- **Funktion**: Rendert Zahlen **0‑9** als LED‑Pattern.  
- **Ablauf**: Zahl input → **Pixel‑Map** → Matrix ansteuern.

---

**🔗 Integration**: torerkennung → toranzeige → font. **🧪 Testbar** per README.
Projekten gezeigt
