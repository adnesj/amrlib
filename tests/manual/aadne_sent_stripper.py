import os

# --- Configuration ---
# Set the paths for your input file and the output file.

# Path to the file containing the AMR data in PENMAN format.
input_file_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/smatch/unique_nno_final.txt'

# Path to the file where the extracted sentences will be saved.
output_file_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/smatch/unique_nno_sentss.txt'

# --- Main Script Functionality ---

def extract_sentences_from_amr_file():
    """
    Reads a file containing AMR graphs in PENMAN format and extracts the
    sentences from the "# ::snt" comment lines, saving them to a new file.
    """
    # 1. Validate that the input file exists
    if not os.path.exists(input_file_path):
        print(f"Error: Input file '{input_file_path}' not found.")
        return

    # 2. Open the input and output files
    print(f"Reading AMR data from '{input_file_path}'...")
    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile, \
             open(output_file_path, 'w', encoding='utf-8') as outfile:

            # 3. Process the file line by line
            for line in infile:
                line = line.strip()

                # Check if the line starts with the sentence tag
                if line.startswith("# ::snt "):
                    # Extract the sentence by slicing the string
                    sentence = line[len("# ::snt "):]
                    sentence = sentence + "\t" + sentence
                    # Write the extracted sentence to the output file, followed by a newline
                    outfile.write(sentence + "\n")

        print(f"Sentences successfully extracted and saved to '{output_file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    extract_sentences_from_amr_file()
