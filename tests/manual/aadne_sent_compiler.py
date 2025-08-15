import amrlib
import os

# --- Configuration ---

# Path to the file with English and Norwegian sentence pairs
#input_file = '/home/adne/Documents/Python/24WS_SemPars/amrlib/tests/manual/tatoeba_sents_20.txt'
input_file = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/smatch/unique_nno_sents.txt'

# Path to the file where the generated AMR graphs will be saved
#output_file = '/home/adne/Documents/Python/24WS_SemPars/amrlib/tests/manual/tatoeba_sents_20_nno-amr.txt'
output_file = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/smatch/nno_test_output_nob.txt'

# Path to the AMR model you want to use for parsing.
#model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/model_stog'
model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/nor1000_model_parse_xfm/checkpoint-1008'
#model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/nor_model_parse_xfm/checkpoint-750'

# Number of sentences to process in each batch
batch_size = 50

# --- Script ---

def generate_amr_dataset_batched():
    """
    Reads English-Norwegian sentence pairs, generates AMRs in batches,
    and saves the output incrementally to the file.
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    # Load the AMR-to-graph model once
    print("Loading AMR model...")
    stog = amrlib.load_stog_model(model_dir=model_path)
    print("Model loaded successfully.")

    # Read all sentences from the input file into memory
    print(f"Reading sentences from '{input_file}'...")
    eng_sents = []
    nor_sents = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    eng, nor = line.split('\t', 1)
                    eng_sents.append(eng.strip())
                    nor_sents.append(nor.strip())
                except ValueError:
                    print(f"Skipping malformed line: '{line}'")

    if not eng_sents:
        print("No sentences found in the input file. Exiting.")
        return

    # Process sentences in batches and save incrementally
    total_sentences = len(eng_sents)
    print(f"\nParsing a total of {total_sentences} English sentences in batches of {batch_size}...")

    # Open the output file once in write mode to clear it for a fresh run
    with open(output_file, 'w', encoding='utf-8') as f_out:
        
        # Loop through the sentences in batches
        for i in range(0, total_sentences, batch_size):
            start_index = i
            end_index = min(i + batch_size, total_sentences)
            
            print(f"  > Processing sentences {start_index + 1} to {end_index}...")

            # Get the current batch of sentences
            eng_batch = eng_sents[start_index:end_index]
            nor_batch = nor_sents[start_index:end_index]
            
            # Parse the batch
            graphs = stog.parse_sents(eng_batch)

            # Write the results of this batch to the file
            for j, (eng, nor, graph) in enumerate(zip(eng_batch, nor_batch, graphs)):
                # Calculate the unique ID for this sentence
                sentence_id = start_index + j + 1
                
                f_out.write(f"# ::id tatoeba_nor.{sentence_id} ::eng {eng}\n")
                #f_out.write(f"# ::snt {nor}\n")
                f_out.write(f"{graph}\n\n")

    print(f"\nProcess complete. The full dataset has been saved to '{output_file}'.")

if __name__ == '__main__':
    generate_amr_dataset_batched()