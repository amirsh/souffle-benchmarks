import pandas as pd
import sys
import os

if len(sys.argv) < 3:
    print("Usage: python preprocess.py <in_folder_path> <out_folder_path>")
    sys.exit(1)

in_folder_path = sys.argv[1]
out_folder_path = sys.argv[2]

all_files = [
	"DirectSuperclass.csv", 
	"DirectSuperinterface.csv", 
	"MainClass.csv", 
	"Method-Modifier.csv", 
	"FormalParam.csv", 
	"Var-Type.csv", 
	"ComponentType.csv", 
	"AssignReturnValue.csv", 
	"ActualParam.csv", 
	"ClassType.csv", 
	"ArrayType.csv", 
	"InterfaceType.csv", 
	"Var-DeclaringMethod.csv", 
	"ApplicationClass.csv", 
	"ThisVar.csv", 
	"NormalHeap.csv", 
	"StringConstant.csv", 
	"AssignHeapAllocation.csv", 
	"AssignLocal.csv", 
	"AssignCast.csv", 
	"Field.csv", 
	"StaticMethodInvocation.csv", 
	"SpecialMethodInvocation.csv", 
	"VirtualMethodInvocation.csv", 
	"Method.csv", 
	"_Method_Descriptor.csv", 
	"StoreInstanceField.csv", 
	"LoadInstanceField.csv", 
	"StoreStaticField.csv", 
	"LoadStaticField.csv", 
	"StoreArrayIndex.csv", 
	"LoadArrayIndex.csv", 
	"Return.csv"
]

for in_file_name in all_files:

	input_file = os.path.join(in_folder_path, in_file_name)
	output_file = os.path.join(out_folder_path, in_file_name)

	# Read the input file (tab-separated)
	df = pd.read_csv(input_file, sep="\t", header=None, keep_default_na=False, na_values=[""])
	output_df = df.dropna().drop_duplicates()

	# Save to new CSV file (comma-separated by default)
	output_df.to_csv(output_file, sep="\t", index=False, header=False)
	print(f"{in_file_name} processed!")
