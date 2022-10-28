"""
President Info
"""
FILE_PATH = "DATA/presidents.txt"

def main():
    """
    Program entry point
    """
    pres_info = get_president_info()
    output_president_info(pres_info)

def output_president_info(info):
    """
    Display POTUS info to screen
    """
    for president in sorted(info, key=lambda p: p[2]):
        print(president)

def get_president_info():
    """
    Read POTUS data from file
    """
    president_info = []
    with open(FILE_PATH) as pres_in:
        for raw_line in pres_in:
            line = raw_line.rstrip() # remove \n
            _, last_name, first_name, dob, *_, party = line.split(':')
            president_info.append((first_name, last_name, dob, party))
    return president_info

if __name__ == '__main__':
    main()
