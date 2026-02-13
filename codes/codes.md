# 🔧 **Codes**

**Übersicht der Python‑Programme** *(src/ Ordner)*. Vollständige Dateien siehe src/.

---

## 🎥 **main_torerkennung.py**
- **Funktion**: Lichtschrankenmessung.  
- **Ablauf**: Lichtschranke überprüft ob es eine Lichtänderung gab -> Tor erkannt
- **Ausgabe**: Tor‑Event triggert eine PIN-Ausgabe für die Toranzeige.

## 💡 **main_toranzeige.py**
- **Funktion**: Steuert **Pimoroni  RGB‑Matrix**.  
- **Ablauf**: Empfängt Tor‑Signal via PIN → Score zählt → LEDs Matrix setzt Score vom jeweiligen Spieler hoch.  

## 🔢 **font_toranzeige.py**
- **Funktion**: Rendert Zahlen **0‑9** als LED‑Pattern.  
- **Ablauf**: Zahl input → **Pixel‑Map** → Matrix ansteuern.

---

**🔗 Integration**: torerkennung → toranzeige → font. **🧪 Testbar** per README.
Projekten gezeigt
