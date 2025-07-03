input_file = r"E:\Documents\Work\VSCode\PS4MR\scripts\t.md"
odd_file = r"E:\Documents\Work\VSCode\PS4MR\scripts\t.md_odd.md"
even_file = r"E:\Documents\Work\VSCode\PS4MR\scripts\t.md_even.md"

with open(input_file, "r", encoding="utf-8") as fin, \
     open(odd_file, "w", encoding="utf-8") as fodd, \
     open(even_file, "w", encoding="utf-8") as feven:
    for idx, line in enumerate(fin, 1):
        if idx % 2 == 1:
            fodd.write(line)
        else:
            feven.write(line)