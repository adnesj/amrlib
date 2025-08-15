import smatch_enhanced

# Replace 'nob_test.txt' and 'nob_gold.txt' with your actual filenames
test_file_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/smatch/nno_test_output_nob.txt'
gold_file_path = '/home/adne/Documents/Python/24WS_SemPars/amrlib/amrlib/data/smatch/unique_nno_final.txt'

print(f"--- Computing scores for {test_file_path} against {gold_file_path} ---")
smatch_enhanced.compute_scores(test_file_path, gold_file_path)

# You would repeat this for your other datasets
# print(f"\n--- Computing scores for nynorsk ---")
# smatch_enhanced.compute_scores('nno_test.txt', 'nno_gold.txt')
#
# print(f"\n--- Computing scores for English ---")
# smatch_enhanced.compute_scores('eng_test.txt', 'eng_gold.txt')