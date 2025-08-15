import amrlib

# Path to the directory containing your fine-tuned model's checkpoint.
# This directory should contain 'model.safetensors' and 'amrlib_meta.json'.
#model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/nor_model_parse_xfm/checkpoint-750'
#model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/model_stog'
model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/nor1000_model_parse_xfm/checkpoint-1008'
#model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/nor1000_model_generate_xfm/checkpoint-1008'

# Load your fine-tuned AMR-to-text model
print("Loading fine-tuned model...")
stog = amrlib.load_stog_model(model_dir=model_path)
gtos = amrlib.load_gtos_model(model_dir=model_path)
print("Model loaded successfully.")

# Define sentences to parse.
# You can try a Norwegian sentence and, for comparison, an English one.
sents = [
    "Vanligvis kjøper jeg ikke noe på internett .",
    "Vanlegvis kjøper eg ikkje noko på internett ."
    ]

# Parse the sentences and get the AMR graphs
print("\nParsing sentences...")
graphs = stog.parse_sents(sents)

# Print the resulting AMR graphs
print("\n--- Results ---")
for graph in graphs:
    print(graph)
    print("-" * 20)