import os

import yaml  # YAML-Bibliothek korrekt importiert

# Definiere den Pfad zum Verzeichnis mit den Markdown-Dateien
verzeichnis_pfad = (
    "/home/florian/Git/webapps/pferdezuchtfeigl/archive/assets/profiles/mares"
)
# Definiere den Pfad zur SQL-Datei
sql_datei_pfad = "/home/florian/Git/webapps/pferdezuchtfeigl/archive/assets/profiles/mares/migration.sql"

# Öffne die SQL-Datei im Schreibmodus
with open(sql_datei_pfad, "a") as sql_datei:  # Korrekt verwenden
    # Iteriere über alle Dateien im Verzeichnis
    for datei_name in os.listdir(verzeichnis_pfad):
        if datei_name.endswith(".md"):
            # Vollständiger Pfad zur Markdown-Datei
            md_datei_pfad = os.path.join(verzeichnis_pfad, datei_name)
            # Lese den Inhalt der Markdown-Datei
            with open(md_datei_pfad, "r") as md_datei:
                inhalte = md_datei.read()
                # Extrahiere den YAML-Header
                yaml_inhalt = inhalte.split("---")[1]  # Korrekte Extraktion des Headers

                # Filtere den YAML-Inhalt
                gefilterte_zeilen = []
                for zeile in yaml_inhalt.split("\n"):
                    if (
                        not zeile.startswith("zucht")
                        and not zeile.startswith(" ")
                        and not zeile.startswith("\t")
                        and not zeile.startswith("profilbild")
                        and not zeile.startswith("eigenleistung")
                    ):
                        gefilterte_zeilen.append(zeile)
                gefilterter_yaml = "\n".join(
                    gefilterte_zeilen
                )  # Korrektes Zusammenfügen

                # Parse den YAML-Header zu einem Python-Dict
                daten = yaml.safe_load(
                    gefilterter_yaml
                )  # Korrekt parse den gefilterten Inhalt

                # Extrahiere die gewünschten Parameter
                name = daten.get("name", None)
                sex = daten.get("sex", "M")
                birth = daten.get("geburtsjahr", None)
                color = daten.get("farbe", None)
                region = daten.get("zuchtgebiet", None)
                owner_id = daten.get("besiter", None)
                breeder_id = daten.get("zuechter", None)
                status = daten.get("status", "active")
                horsetelex = daten.get("horsetelex", None)

                # Erstelle das INSERT INTO-Statement
                insert_statement = f"INSERT INTO horses (name, sex, birth, color, region, owner_id, breeder_id, status, horsetelex) VALUES ('{name}', '{sex}', '{birth}', '{color}', '{region}', '{owner_id}', '{breeder_id}', '{status}', '{horsetelex}');\n"

                # Schreibe das INSERT INTO-Statement in die SQL-Datei
                sql_datei.write(insert_statement)  # Korrektes Schreiben in die Datei
