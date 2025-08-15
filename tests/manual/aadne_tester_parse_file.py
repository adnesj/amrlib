import amrlib
import os

# --- Configuration ---
# Set the paths for your input file, output file, and the model you want to use.

# Path to the file containing the sentences you want to parse.
# Each sentence should be on a new line.
input_file_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/smatch/nno_gold.txt'

# Path to the file where the generated AMR graphs will be saved.
output_file_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/smatch/test_output_nor.txt'

# Path to the directory containing your fine-tuned PARSING model.
# This must be a 'stog' (sentence-to-graph) model.
# Ensure you are using the correct path to a parsing model checkpoint.
# The uncommented path is an example, replace it with your model path.
# model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/nor_model_parse_xfm/checkpoint-750'
model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/nor1000_model_parse_xfm/checkpoint-1008'


# --- Main Script Functionality ---

def parse_and_save_sentences():
    """
    Loads a parsing model, reads sentences from a file, parses them,
    and saves the resulting AMR graphs to a new file in PENMAN format.
    """
    # 1. Validate that the input file and model path exist
    if not os.path.exists(input_file_path):
        print(f"Error: Input file '{input_file_path}' not found.")
        return
    if not os.path.exists(model_path):
        print(f"Error: Model path '{model_path}' not found.")
        return

    # 2. Load the sentence-to-graph (stog) model
    # Note: This loads a parsing model. Do not use a generation model here.
    print(f"Loading AMR parsing model from '{model_path}'...")
    try:
        stog = amrlib.load_stog_model(model_dir=model_path)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Failed to load model. Check the path and file integrity. Error: {e}")
        return

    # 3. Read sentences from the input file
    print(f"Reading sentences from '{input_file_path}'...")
    sents = []
    with open(input_file_path, 'r', encoding='utf-8') as f:
        sents = [line.strip() for line in f if line.strip()]

    if not sents:
        print("No sentences found in the input file. Exiting.")
        return

    # 4. Parse the sentences in batches
    print(f"Parsing {len(sents)} sentences...")
    graphs = stog.parse_sents(sents)

    # 5. Write the results to the output file
    print(f"Saving results to '{output_file_path}'...")
    with open(output_file_path, 'w', encoding='utf-8') as f_out:
        for i, (sent, graph) in enumerate(zip(sents, graphs)):
            # Add the original sentence as a comment in the output file for context
            f_out.write(f"# ::id sentence_{i+1}\n")
            f_out.write(f"# ::snt {sent}\n")
            f_out.write(f"{graph}\n\n")

    print("Process complete.")


if __name__ == '__main__':
    parse_and_save_sentences()
