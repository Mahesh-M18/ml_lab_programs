import csv

def loadCsv(filename):
    with open(filename, "r") as file:
        lines = csv.reader(file)
        header = next(lines)            
        dataset = list(lines)           
    return header, dataset

filename = "Weather.csv"  
attributes, dataset = loadCsv(filename)

num_attributes = len(attributes) - 1    

print("Attributes:", attributes[:-1])   
print("\nDataset:")
for row in dataset:
    print(row)


target = [row[-1] for row in dataset]
print("\nTarget values:", target)

hypothesis = ['0'] * num_attributes
print("\nInitial Hypothesis:", hypothesis)

print("\nSteps of Hypothesis Update:")
for i in range(len(dataset)):
    if target[i] == 'Yes':
        for j in range(num_attributes):
            if hypothesis[j] == '0':
                hypothesis[j] = dataset[i][j]
            elif hypothesis[j] != dataset[i][j]:
                hypothesis[j] = '?'
        print(f"Step {i+1}: {hypothesis}")
    else:
        print(f"Step {i+1}: {hypothesis}")

print("\nFinal Hypothesis:")
print(hypothesis)
