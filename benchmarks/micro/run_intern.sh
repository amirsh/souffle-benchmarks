echo $1
# souffle micro_intern_pre0.dl -F$1         
# mv _Method_Des*.csv $1
souffle micro_intern_pre1.dl -F$1         
python3 preprocess.py $1 2
souffle micro_intern_pre2.dl -F$1         
mv *_interned.csv $1
time souffle micro_interned.dl -F$1