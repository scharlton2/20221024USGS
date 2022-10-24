
file_path = "DATA/presidents.txt"
last_names = []
with open(file_path) as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip() # remove \n
        term, last_name, first_name, dob, dod, bplace, bstate, took, left, party = line.split(':')
        last_names.append(last_name)
print(f"last_names: {last_names}")

last_names_upper = [n.upper() for n in last_names]
for last_name in last_names_upper:
    print(last_name)
