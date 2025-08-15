import amrlib

# Path to the directory containing your fine-tuned model's checkpoint.
# This directory should contain 'model.safetensors' and 'amrlib_meta.json'.
#model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/nor_model_parse_xfm/checkpoint-750'
model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/model_gtos'
#model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/nor1000_model_parse_xfm/checkpoint-1008'
#model_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/nor1000_model_generate_xfm/checkpoint-1008'

# Load your fine-tuned AMR-to-text model
print("Loading fine-tuned model...")
stog = amrlib.load_stog_model(model_dir=model_path)
gtos = amrlib.load_gtos_model(model_dir=model_path)
print("Model loaded successfully.")

# Define sentences to parse.
# You can try a Norwegian sentence and, for comparison, an English one.
graphs = [
    '# ::snt Vanlegvis kjøper eg ikkje noko på internett .\n(p / possible-01\n      :ARG1 (d / do-02\n            :ARG0 (ii / i)\n:ARG1 (t / that)\n            :time (d2 / day\n                  :mod (n / next)))\n      :ARG1-of (c / cause-01\n            :ARG0 (a / amr-unknown)))\n'
    '# ::snt Vanligvis kjøper jeg ikke noe på internett .\n(p / possible-01\n      :polarity -\n      :ARG1 (g / go-02\n            :ARG0 (ii / i)\n            :ARG4 (h / house\n                  :poss ii)))'
]

# Parse the sentences and get the AMR graphs
print("\nGenerating sentences from graphs...")
sents, _ = gtos.generate(graphs)

# Print the resulting sentences
print("\n--- Generated Sentences ---")
for sent in sents:
    print(sent)
    print("-" * 20)