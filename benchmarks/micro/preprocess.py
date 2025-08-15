import pandas as pd
import sys
import os

if len(sys.argv) < 3:
    print("Usage: python preprocess.py <folder_path> <1|2>")
    sys.exit(1)

folder_path = sys.argv[1]
phase = sys.argv[2]
if phase == "1":
	input_file = os.path.join(folder_path, "Method.csv")
	output_file = os.path.join(folder_path, "_Method_Descriptor.csv")

	# Read the input file (tab-separated)
	df = pd.read_csv(input_file, sep="\t", header=None)

	output_df = pd.DataFrame({
	    0: df.iloc[:, 0],  # first column
	    1: df.iloc[:, 4].astype(str) + "(" + df.iloc[:, 2].astype(str) + ")"  # concatenated columns
	})

	# Save to new CSV file (comma-separated by default)
	output_df.to_csv(output_file, sep="\t", index=False, header=False)
else:
	input_file = "All_Strings.csv"
	output_file = os.path.join(folder_path, "Global_String_Dictionary.csv")

	# Read the input file (tab-separated)
	df = pd.read_csv(input_file, sep="\t", header=None)

	output_df = pd.DataFrame({
	    0: df.iloc[:, 0],       # first column (original data)
	    1: df.index             # second column (row index)
	})

	# Save to new CSV file (comma-separated by default)
	output_df.to_csv(output_file, sep="\t", index=False, header=False)