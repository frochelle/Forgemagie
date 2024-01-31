import pandas as pd
from item import Item
from app import App


# Runes in database csv file
runes = pd.read_csv('Database/database.csv', sep=';')

# Item examples
caracoiffe = Item('Caracoiffe', {'PA': 1, 'Vitalite': 80})

# Launch app
app = App([caracoiffe])
