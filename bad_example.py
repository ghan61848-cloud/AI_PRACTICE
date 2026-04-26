def average_age(records):
    # NAPRAWIONO BŁĄD: ZeroDivisionError (dzielenie przez zero)
    # Wyjaśnienie: Zapobiega awarii w przypadku, gdy przekazana lista `records` jest całkowicie pusta [].
    if not records:
        return 0
        
    total = 0
    valid_records_count = 0
    
    for record in records:
        # NAPRAWIONO BŁĄD: KeyError (brak klucza)
        # Wyjaśnienie: Zapobiega przerwaniu programu, gdy w słowniku w ogóle nie ma wpisanego klucza 'age' (np. {'name': 'Krzysztof'}).
        if 'age' in record:
            try:
                # NAPRAWIONO BŁĄD: TypeError (zły typ danych)
                # Wyjaśnienie: Zapobiega błędowi dodawania liczby do tekstu (gdy wiek to np. '20'). Funkcja float() zamienia go w liczbę.
                age = float(record['age'])
                total += age
                valid_records_count += 1
            except (ValueError, TypeError):
                # NAPRAWIONO BŁĄD: ValueError (zła wartość)
                # Wyjaśnienie: Zapobiega awarii, gdy wiek to tekst, którego nie da się zamienić na cyfry (np. 'nieznany'). Błędny rekord jest po prostu ignorowany (continue).
                continue
                
    # NAPRAWIONO BŁĄD: ZeroDivisionError (dzielenie przez zero po filtracji)
    # Wyjaśnienie: Zapobiega awarii w przypadku, gdy lista zawierała słowniki, ale ŻADEN z nich nie miał poprawnego wieku (wtedy valid_records_count zostałoby na poziomie 0).
    if valid_records_count == 0:
        return 0
        
    # NAPRAWIONO GŁÓWNY BŁĄD: Zły wynik matematyczny (dzielenie przez zmienną `record`)
    # Wyjaśnienie: Wcześniej było `len(record)`, co dzieliło wynik przez liczbę kluczy (np. 2). 
    # Teraz dzielimy przez `valid_records_count`, czyli liczbę osób, których wiek poprawnie zsumowaliśmy.
    return total / valid_records_count


if __name__ == '__main__':
    # Rozszerzona lista testowa, by udowodnić, że zabezpieczenia działają
    sample = [
        {'name': 'Anna', 'age': 21},
        {'name': 'Piotr', 'age': 23},
        {'name': 'Maria', 'age': 25},
        {'name': 'Krzysztof'},               # Brak klucza 'age'
        {'name': 'Zofia', 'age': '20'},      # 'age' to string
        {'name': 'Jan', 'age': 'nieznany'},  # 'age' to string bez cyfr
    ]
    
    print(average_age(sample))
