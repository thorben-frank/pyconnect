```
python ../../rundisconnect.py
```
loads the specifications from `dinfo`. It essentially loads the data from the `min_dha.data` file which contains all 
unique minima and from `ts_dha.data` which contains information about the sequence of visited minima and the transition
state in-between. The indices in `ts_dha.data` in the 4-th and 5-th column correspond to the index of the start and the 
end minima. The first column denotes the energy of the transition state. The minima indices are defined implicitly by the 
row number in the `min_dha.data` (starting from 1 not from 0). More details also in the repository `readme`.    

