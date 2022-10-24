
file_path = "DATA/presidents.txt"
president_info = []
with open(file_path) as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip() # remove \n
        term, last_name, first_name, dob, dod, bplace, bstate, took, left, party = line.split(':')
        president_info.append((first_name, last_name, dob, party))

for president in sorted(president_info, key=lambda p: p[2]):
    print(president)
