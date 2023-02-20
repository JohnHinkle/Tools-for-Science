# PURPOSES OF THIS PROGRAM
# Counts the total number of sequences in a .txt file
# Counts the times a probe occurs in a .txt file
# Saves data to a .csv file to the current working directory of this program


def main():
    import os
    import csv

    folder_path = "folder_path"
    # replace with the path to your folder

    # PROBES
    # This is an ANME-1 probe
    probe_1 = "agttttcgcgcctgatgc"

    # This is an ANME-2 probe
    probe_2 = "ggctaccactcgggccgc"

    # COMMON SEQUENCE IDENTIFIER
    # for this program to work, each sequence name must have something in common (ex. "@m64")
    sequence_start = "@m64"

    search_strings = [probe_1, probe_2, sequence_start]

    # This step sorts the files in numerical order
    filenames = sorted([filename for filename in os.listdir(folder_path) if filename.endswith('.hifi_reads.txt')])

    with open('sequence_count.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Filename'] + [f'Count of "{string}"' for string in search_strings])

        for filename in filenames:
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as f:
                contents = f.read()
                # these two lines are needed for the probe search to work
                # remove spaces and convert all letters to lowercase
                contents = contents.replace(' ', '').lower()
                counts = [contents.count(string.lower().replace(' ', '')) for string in search_strings]
                writer.writerow([filename] + counts)

    print('Probes and sequences counted! ʕ•ᴥ•ʔ')


main()
