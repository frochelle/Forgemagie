import pandas as pd
from item import Item


# Runes in database csv file
runes = pd.read_csv('Database/database.csv', sep=';')

# Item examples
caracoiffe = Item({'PA': 1, 'Vitalite': 80})
