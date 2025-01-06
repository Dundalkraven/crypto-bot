from scipy.stats import binomtest

def binomial_test_greater_than_50(successes, trials):
    # Nullhypothese: p <= 0.5
    # Alternativhypothese: p > 0.5
    p_value = binomtest(successes, trials, p=0.5, alternative='greater').pvalue
    return p_value

if __name__ == "__main__":
    # Beispielwerte: Anzahl der Erfolge und Versuche
    erfolge = 64
    versuche = 82
    
    # Berechnung des p-Werts
    p_wert = binomial_test_greater_than_50(erfolge, versuche)
    print(f"Der p-Wert des Tests beträgt: {p_wert}")

    # Interpretation
    alpha = 0.05
    if p_wert < alpha:
        print("Das Ergebnis ist statistisch signifikant. Die Erfolgswahrscheinlichkeit ist wahrscheinlich größer als 50%.")
    else:
        print("Das Ergebnis ist nicht statistisch signifikant. Wir können keine Aussage über eine Erfolgswahrscheinlichkeit größer als 50% treffen.")
