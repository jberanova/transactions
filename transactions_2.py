import csv

def analyze_transactions(soubor_tr):
    transactions = []
    celkem_tr = 0
    hodnota_jed = 0

    with open(soubor_tr, 'r') as file:
        precist = csv.reader(file)
        next(precist) 
        for row in precist:
            transactions.append(row)
            celkem_tr += 1
            if row[0].startswith('1'):
                hodnota_jed += 1
    procenta = (hodnota_jed / celkem_tr) * 100
    
    print(f"{celkem_tr} - celkový počet")
    print(f"{hodnota_jed} - transakce které začínají hodnotou 1")
    print(f"{procenta:.2f}% - procento transakcí k celkovému počtu")

soubor_tr = 'transactions.csv'
analyze_transactions(soubor_tr)


