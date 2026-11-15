Sprawozdanie z Laboratorium 4: Ochrona danych i algorytmów

Karol Ziomek

1.
Analiza wybranego zbioru danych
Nazwa zbioru: Credit Card Fraud Detection
Źródło: https://www.kaggle.com/datasets/joebeachcapital/credit-card-fraud
Licencja: Open Database License (ODbL) / Database Contents License (DbCL)

Analiza pod kątem danych osobowych i wrażliwych:
Zbiór zawiera 284 807 transakcji kartami kredytowymi dokonanych przez europejskich posiadaczy kart we wrześniu 2013 roku (w tym 492 oszustwa). Ze względu na poufność oraz ochronę prywatności klientów, oryginalne cechy transakcyjne zostały poddane nieodwracalnej transformacji PCA (główne składowe oznaczone jako zmienne numeryczne od V1 do V28). Jedynymi nieprzekształconymi zmiennymi są czas (Time), kwota transakcji (Amount) oraz klasa docelowa (Class). Dzięki zastosowaniu transformacji PCA oraz całkowitemu usunięciu imion, nazwisk, numerów kart i lokalizacji, dane te zostały skutecznie zanonimizowane i nie zawierają bezpośrednich ani pośrednich danych osobowych ani wrażliwych.

Środki ochrony przed użyciem:
Mimo że dane są już zanonimizowane przez autorów, przed ich użyciem w projekcie zastosuję zasadę minimalizacji danych (wybiorę tylko zmienne niezbędne do treningu modelu), ograniczę dostęp do pobranego pliku wyłącznie do lokalnego środowiska roboczego oraz zadbam o poprawne cytowanie autorów badania zgodnie z wymogami licencji.

2.
Checklista ochrony danych

| Pytanie | Odpowiedź |
| --- | --- |
| Czy dane są zanonimizowane lub spseudonimizowane? | Tak, dane są zanonimizowane za pomocą transformacji PCA (zmienne V1–V28), usunięto wszystkie dane identyfikujące posiadaczy kart. |
| Jaka jest licencja zbioru? | Open Database License (ODbL) / Database Contents License (DbCL). |
| Czy licencja pozwala na użycie komercyjne? | Tak, licencja ODbL dopuszcza użycie komercyjne pod warunkiem uznania autorstwa i udostępnienia zmian na tych samych zasadach (Share-Alike). |
| Czy zbiór zawiera dane wrażliwe (zdrowie, religia, orientacja)? | Nie, zbiór zawiera wyłącznie przekształcone numerycznie parametry transakcji finansowych. |
| Czy znam źródło danych i mogę je opisać w dokumentacji? | Tak, zbiór pochodzi z badań naukowych grupy MLG-ULB (Université Libre de Bruxelles) i Worldline z 2015 roku, udostępnionych w repozytorium OpenML oraz Kaggle. |

Ocena bezpieczeństwa użycia zbioru w projekcie komercyjnym: 5/5.
Zbiór jest w pełni bezpieczny pod kątem RODO dzięki nieodwracalnej redukcji wymiarowości (PCA) i brakowi danych osobowych. W projekcie komercyjnym należy jednak pamiętać o wymogu Share-Alike wynikającym z licencji ODbL w przypadku udostępniania zmodyfikowanej bazy danych oraz o obowiązku cytowania autorów.

3.
Zadanie samodzielne 1: Porównanie licencji na Kaggle

Porównałem wybrany wcześniej zbiór z drugim zbiorem o tej samej tematyce wykrywania oszustw kartowych (Credit Card Fraud autorstwa Incribo: https://www.kaggle.com/datasets/teamincribo/credit-card-fraud, który zawiera 8000 syntetycznych rekordów transakcji (m.in. imię posiadacza, zahaszowany numer karty, adres IP, lokalizację) i jest udostępniony na licencji Apache 2.0.
| Zbiór danych | Licencja | Użycie komercyjne | Wymagania licencyjne |
| --- | --- | --- | --- |
| Credit Card Fraud (joebeachcapital / ULB) | Open Database License (ODbL) | Tak | Uznanie autorstwa (cytowanie publikacji naukowej) oraz udostępnianie opracowań bazy na tych samych zasadach (Share-Alike). |
| Credit Card Fraud (teamincribo) | Apache 2.0 | Tak | Zachowanie informacji o prawach autorskich i treści licencji; brak wymogu udostępniania zmian na tej samej licencji (brak Share-Alike). |

Uzasadnienie wyboru do projektu komercyjnego:
W projekcie komercyjnym bezpieczniej pod względem prawnym i biznesowym jest użyć drugiego zbioru (teamincribo) na licencji Apache 2.0. Licencja ta jest permisywna, nie narzuca klauzuli Share-Alike (nie zmusza firmy do udostępniania zmodyfikowanych struktur danych na otwartej licencji), a ponadto wprost udziela licencji patentowej. Dodatkowo dane w tym zbiorze są w pełni syntetyczne, co eliminuje ryzyko naruszenia RODO mimo obecności pól wyglądających jak dane osobowe.

4.
Zadanie samodzielne 2: Pseudonimizacja i anonimizacja

Tabela oryginalna (dane fikcyjne):
Kolumny bezpośrednio identyfikujące osobę to Imię i nazwisko. Kolumny, które w połączeniu mogą pozwolić na pośrednią identyfikację osoby, to Data urodzenia, Kod pocztowy oraz Płeć.

| Imię i nazwisko | Data urodzenia | Kod pocztowy | Płeć | Diagnoza |
| --- | --- | --- | --- | --- |
| Jan Kowalski | 1985-03-12 | 20-001 | Mężczyzna | Nadciśnienie tętnicze |
| Anna Nowak | 1992-11-24 | 20-601 | Kobieta | Cukrzyca typu 1 |
| Piotr Wiśniewski | 1978-07-05 | 21-040 | Mężczyzna | Astma oskrzelowa |

Wersja spseudonimizowana (zastąpienie bezpośrednich identyfikatorów kodem):

| ID Pacjenta | Data urodzenia | Kod pocztowy | Płeć | Diagnoza |
| --- | --- | --- | --- | --- |
| PAC-001 | 1985-03-12 | 20-001 | Mężczyzna | Nadciśnienie tętnicze |
| PAC-002 | 1992-11-24 | 20-601 | Kobieta | Cukrzyca typu 1 |
| PAC-003 | 1978-07-05 | 21-040 | Mężczyzna | Astma oskrzelowa |

Tabela kluczy (przechowywana w osobnym, zabezpieczonym miejscu):

| ID Pacjenta | Imię i nazwisko |
| --- | --- |
| PAC-001 | Jan Kowalski |
| PAC-002 | Anna Nowak |
| PAC-003 | Piotr Wiśniewski |

Wersja zanonimizowana (usunięcie identyfikatorów i uogólnienie quasi-identyfikatorów):

| Przedział wiekowy | Region | Płeć | Diagnoza |
| --- | --- | --- | --- |
| Lata 1980–1989 | Woj. lubelskie | Mężczyzna | Nadciśnienie tętnicze |
| Lata 1990–1999 | Woj. lubelskie | Kobieta | Cukrzyca typu 1 |
| Lata 1970–1979 | Woj. lubelskie | Mężczyzna | Astma oskrzelowa |

Analiza ryzyka po anonimizacji:
Mimo usunięcia imion, nazwisk i klucza oraz uogólnienia daty urodzenia do dekady i kodu pocztowego do województwa, minimalne ryzyko ponownej identyfikacji nadal istnieje w przypadku bardzo rzadkich chorób lub połączenia tego zbioru z innymi publicznymi bazami danych. W zaprezentowanym przykładzie choroby są jednak powszechne, a grupy odpowiednio szerokie, co skutecznie minimalizuje ryzyko wskazania konkretnej osoby.

5. Zadanie samodzielne 3: Licencje bibliotek programistycznych

| Biblioteka | Licencja | Typ licencji | Użycie w projekcie komercyjnym |
| --- | --- | --- | --- |
| scikit-learn | BSD 3-Clause License | Permisywna | Tak |
| pandas | BSD 3-Clause License | Permisywna | Tak |
| PyTorch | BSD-Style License (BSD 3-Clause) | Permisywna | Tak |

Analiza wymogów licencyjnych:
Żadna z powyższych trzech bibliotek nie wymaga udostępnienia kodu źródłowego mojej własnej aplikacji, ponieważ wszystkie opierają się na permisywnej licencji BSD 3-Clause (wymagają jedynie zachowania oryginalnej noty o prawach autorskich i treści licencji w dystrybucji).

Gdyby jednak którakolwiek z użytych bibliotek była objęta licencją typu copyleft (np. GNU GPL), a ja rozpowszechniałbym zbudowaną na niej aplikację na zewnątrz (np. sprzedawał ją klientom), musiałbym udostępnić cały kod źródłowy mojej aplikacji na tej samej licencji GPL.
