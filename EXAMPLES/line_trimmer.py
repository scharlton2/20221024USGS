
def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')  # 'yield' causes this function to return a generator object

mary_in = trimmed('../DATA/mary.txt')
print(f"next(mary_in): {next(mary_in)}")
print(f"mary_in: {mary_in}")
for trimmed_line in mary_in:  #  next(mary_in)
    print(trimmed_line)
