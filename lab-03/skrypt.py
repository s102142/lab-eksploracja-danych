import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print("Liczba wierszy:", len(df))
print("Nazwy kolumn:", df.columns)
print("Braki danych:", df.isnull().sum())
print("Modyfikacja na potrzeby zadania 2")
