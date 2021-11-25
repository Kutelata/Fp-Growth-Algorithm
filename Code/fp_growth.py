import pyfpgrowth
import csv

transactions = []
dataset = "E:\STUDY\Khai_Pha_Du_Lieu\FP-Growth\Code\kaggle.csv"
with open(dataset) as file_name:
    file_read = csv.reader(file_name)
    for row in file_read: 
        row = list(filter(None, row))
        transactions.append(row)

patterns = pyfpgrowth.find_frequent_patterns(transactions,1000)
rules = pyfpgrowth.generate_association_rules(patterns,0.4)

print("Frequent Pattern :")
print(patterns)
print("\nAssociation Rules :")
print(rules)  
# print(len(transactions))
# print(transactions)
