group_records = []

for i in range(1, 6):
    print(f"\nVoer de gegevens in voor groep {i}:")
    groupname = input("  Groepsnaam: ")
    size_of_group = int(input("  Grootte van de groep: "))
    date_of_competition = input("  Datum van de competitie (bijv. 2025-06-15): ")
    venue = input("  Locatie van de competitie: ")
    type_of_medal = input("  Type medaille (Goud/Zilver/Brons): ")
    group_tuple = (groupname, size_of_group, date_of_competition, venue, type_of_medal)
    group_records.append(group_tuple)

print("\n🎉 Overzicht van alle groepen en hun prestaties:\n")
for index, record in enumerate(group_records, start=1):
    print(f"Groep {index}:")
    print(f"  Naam         : {record[0]}")
    print(f"  Grootte      : {record[1]}")
    print(f"  Datum        : {record[2]}")
    print(f"  Locatie      : {record[3]}")
    print(f"  Medaille     : {record[4]}")
    print("-" * 40)
