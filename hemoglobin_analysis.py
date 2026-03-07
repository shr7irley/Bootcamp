import json

# Leer la secuencia
with open("hemoglobin_clean.txt") as f:
    sequence = f.read().strip()

# Información básica
print("Protein: Human Hemoglobin Beta")
print("Sequence length:", len(sequence))

# Lista de aminoácidos
amino_acids = [
"A","R","N","D","C","Q","E","G","H",
"I","L","K","M","F","P","S","T","W","Y","V" 
]

# Contar aminoácidos
counts = {}

for aa in amino_acids:
    counts[aa] = sequence.count(aa)

print("\nAmino acid composition:")
for aa, count in counts.items():
    print(aa, ":", count)

# Pesos moleculares
weights = {
"A":89.1,"R":174.2,"N":132.1,"D":133.1,"C":121.2,
"Q":146.1,"E":147.1,"G":75.1,"H":155.2,"I":131.2,
"L":131.2,"K":146.2,"M":149.2,"F":165.2,"P":115.1,
"S":105.1,"T":119.1,"W":204.2,"Y":181.2,"V":117.1
}

# Función para calcular peso molecular
def molecular_weight(seq):

    total = 0

    for aa in seq:
        total += weights.get(aa,0)

    return total

mw = molecular_weight(sequence)

print("\nMolecular Weight:", mw)

# Aminoácidos hidrofóbicos
hydrophobic = ["A","V","I","L","M","F","W","Y"]

hydro_count = 0

for aa in sequence:
    if aa in hydrophobic:
        hydro_count += 1

percentage = (hydro_count / len(sequence)) * 100

print("\nHydrophobic amino acids %:", percentage)

# Guardar resultados
results = {
"protein":"Human Hemoglobin Beta",
"length":len(sequence),
"amino_acid_counts":counts,
"molecular_weight":mw,
"hydrophobic_percentage":percentage
}

with open("hemoglobin_results.json","w") as f:
    json.dump(results,f,indent=4)

