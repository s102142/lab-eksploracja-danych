Sprawozdanie z Laboratorium 3: Wersjonowanie kodu - Git i GitHub
Karol Ziomek

Wykaz i opis commitów w branchu:
W ramach ćwiczenia skonfigurowałem lokalne środowisko Git, utworzyłem gałąź funkcjonalną lab-03-git oraz wykonałem commity zawierające rozwijany skrypt Python:
- Skrypt wczytujący plik CSV: utworzyłem strukturę folderu lab-03/, dodałem plik skrypt.py zawierający podstawowe wczytanie ramki danych oraz wypisanie liczby wierszy.
- Wypisanie nazw kolumn: zaktualizowałem skrypt o funkcjonalność wyświetlania listy nazw kolumn danych.
- Sprawdzanie braków danych: rozbudowałem skrypt o weryfikację występujących braków danych w poszczególnych kolumnach.

Następnie wypchnąłem brancha na platformę GitHub, utworzyłem Pull Request, sprawdziłem zmiany i zmergowałem z Mainem.

Opis zadań samodzielnych

Zadanie 1:
Przetestowałem proces powstawania oraz rozwiązywania konfliktów scalania. Utworzyłem dwie osobne gałęzie (konflikt-a oraz konflikt-b) z poziomu tego samego commitu początkowego, na których zmodyfikowałem tę samą linię w pliku README.md. Podczas próby wykonania git merge konflikt-b na gałęzi konflikt-a, Git poprawnie zgłosił konflikt.
Otworzyłem plik, ręcznie usunąłem znaczniki konfliktu, wybrałem docelową wersję nagłówka i zatwierdziłem scalenie nowym commitem.

Zadanie 2:
Skonfigurowałem plik .gitignore w katalogu głównym repozytorium, dodając do niego reguły wykluczające pliki dzienników (*.log), pamięć podręczną Pythona (pycache/) oraz punkty kontrolne notebooków (.ipynb_checkpoints/). Utworzyłem plik lab-03/debug.log i zweryfikowałem poleceniem git status, że jest ignorowany przez system kontroli wersji. Dodatkowo zmodyfikowałem plik lab-03/skrypt.py i przeanalizowałem wprowadzone różnice w kodzie za pomocą polecenia git diff.

Zadanie 3:
Przetestowałem dwa mechanizmy cofania zmian. Najpierw wypróbowałem polecenie git restore do odrzucenia niestagowanych zmian w pliku roboczym. Następnie wprowadziłem do pliku skrypt.py celowo błędną linię kodu i zatwierdziłem ją commitem. Aby bezpiecznie cofnąć zmianę bez usuwania historii projektu, wykonałem polecenie git revert HEAD. Utworzyło ono nowy commit odwracający błąd, co zweryfikowałem wyświetlając historię zmian za pomocą git log --oneline --graph.
