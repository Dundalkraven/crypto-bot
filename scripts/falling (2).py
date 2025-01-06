import os
import pandas as pd

def analyze_csv_files(folder_path):
    """
    Analysiert alle CSV-Dateien in einem Ordner und berechnet,
    ob der Kurs gestiegen oder gefallen ist basierend auf dem 'Close'-Wert.
    
    Gibt am Ende eine Zusammenfassung der gestiegenen und gefallenen Kurse aus.
    """
    # Stelle sicher, dass der Ordner existiert
    if not os.path.exists(folder_path):
        print(f"Der Ordner {folder_path} existiert nicht.")
        return

    # Liste alle CSV-Dateien im Ordner auf
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    if not csv_files:
        print("Keine CSV-Dateien im angegebenen Ordner gefunden.")
        return

    # Zähler für gestiegene und gefallene Kurse
    risen_count = 0
    fallen_count = 0

    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        print(f"Analysiere Datei: {csv_file}")

        # Lade die CSV-Datei
        try:
            df = pd.read_csv(file_path)

            # Prüfe, ob die Spalte 'Close' vorhanden ist
            if 'Close' not in df.columns:
                print(f"Die Datei {csv_file} enthält keine 'Close'-Spalte. Überspringe.")
                continue

            # Berechne die Veränderung im Kurs
            first_close = df['Close'].iloc[0]
            last_close = df['Close'].iloc[-1]
            percent_change = ((last_close - first_close) / first_close) * 100

            # Status bestimmen
            if percent_change > 0:
                risen_count += 1
                print(f"{csv_file}: Gestiegen ({percent_change:.2f}%)")
            else:
                fallen_count += 1
                print(f"{csv_file}: Gefallen ({percent_change:.2f}%)")

        except Exception as e:
            print(f"Fehler beim Verarbeiten der Datei {csv_file}: {e}")

    # Zusammenfassung anzeigen
    print("\nZusammenfassung:")
    print(f"Gestiegene Kurse: {risen_count}")
    print(f"Gefallene Kurse: {fallen_count}")

# Hauptfunktion
if __name__ == "__main__":
    folder_path = "all_coins"  # Ändere dies auf den Pfad zu deinem Ordner mit den CSV-Dateien
    analyze_csv_files(folder_path)
