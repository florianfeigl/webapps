import os

# Definieren Sie den Pfad zum Zielverzeichnis
verzeichnis_pfad = (
    "/home/florian/Git/webapps/pferdezuchtfeigl/archive/assets/profiles/mares"
)

# Definieren Sie die Anzahl der Leerzeichen, die einen Tab ersetzen sollen
leerzeichen_pro_tab = 4

# Iterieren Sie über alle Dateien im angegebenen Verzeichnis
for datei_name in os.listdir(verzeichnis_pfad):
    # Vollständiger Pfad zur aktuellen Datei
    datei_pfad = os.path.join(verzeichnis_pfad, datei_name)

    # Überprüfen, ob es sich um eine Datei handelt (und nicht um ein Verzeichnis)
    if os.path.isfile(datei_pfad):
        # Lesen Sie den Inhalt der Datei
        with open(datei_pfad, "r") as datei:
            inhalt = datei.read()

        # Ersetzen Sie Tabs durch Leerzeichen
        geänderter_inhalt = inhalt.replace("\t", " " * leerzeichen_pro_tab)

        # Schreiben Sie den geänderten Inhalt zurück in die Datei
        with open(datei_pfad, "w") as datei:
            datei.write(geänderter_inhalt)

print("Alle Tabs wurden erfolgreich durch Leerzeichen ersetzt.")
