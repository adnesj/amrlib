import os

# --- Configuration ---
# Update these file paths to match your local setup.

# The primary file from which you want to find unique AMR graphs.
file1_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/smatch/unique_nno_start.txt'

# The reference file to check against.
file2_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/smatch/unique_nno_compare.txt'

# The file where the unique AMR graphs from file1 will be saved.
output_file_path = 'unique_nno_final.txt'


def get_amr_graphs(file_path):
    """
    Reads an AMR file and returns a list of cleaned AMR graph strings,
    ignoring comment lines and normalizing whitespace.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        # Read the entire file content
        content = f.read()

    # Split the file into individual AMR entries based on blank lines
    entries = content.strip().split('\n\n')

    graphs = []
    for entry in entries:
        lines = entry.strip().split('\n')
        # Filter out comment lines starting with '#'
        graph_lines = [line for line in lines if not line.startswith('#')]
        
        # Join the graph lines back together and normalize whitespace
        graph_str = ' '.join(graph_lines).strip()
        
        if graph_str:
            graphs.append(graph_str)
            
    return graphs


def get_amr_entries(file_path):
    """
    Reads an AMR file and returns a list of full AMR entries, including comments.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split the file into individual AMR entries based on blank lines
    entries = content.strip().split('\n\n')
    return [entry for entry in entries if entry.strip()]


def find_unique_amr_graphs():
    """
    Compares two AMR files and saves the unique graphs from the first file
    to a new output file.
    """
    print(f"Reading graphs from reference file: {file2_path}...")
    # Get a set of graph strings from file2 for efficient lookup
    graphs_in_file2 = set(get_amr_graphs(file2_path))

    if not graphs_in_file2:
        print("Warning: No AMR graphs found in the reference file. All graphs from file1 will be considered unique.")

    print(f"Reading graphs from primary file: {file1_path}...")
    # Get the full entries from file1 to preserve comments
    entries_in_file1 = get_amr_entries(file1_path)

    unique_entries = []
    for entry in entries_in_file1:
        # Extract the graph part of the current entry
        lines = entry.strip().split('\n')
        graph_lines = [line for line in lines if not line.startswith('#')]
        graph_str = ' '.join(graph_lines).strip()
        
        # Check if the cleaned graph string is in the set of graphs from file2
        if graph_str and graph_str not in graphs_in_file2:
            unique_entries.append(entry)

    if unique_entries:
        print(f"\nFound {len(unique_entries)} unique AMR graphs.")
        print(f"Saving unique graphs to {output_file_path}...")
        with open(output_file_path, 'w', encoding='utf-8') as f_out:
            f_out.write('\n\n'.join(unique_entries) + '\n\n')
        print("Done.")
    else:
        print("\nNo unique AMR graphs found in file1.")


if __name__ == '__main__':
    find_unique_amr_graphs()