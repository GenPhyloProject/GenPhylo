# GenPhylo: Generating heterogeneous data on gene trees

### Authors: Marta Casanellas, Martí Cortada, Adrià Diéguez

---

We introduce **GenPhylo**, an open-source Python module for simulating genetic data along a phylogeny avoiding the restriction of continuous-time Markov processes.

### **Installation and requirements.**

```diff
pip install genphylo
```
GenPhylo has several dependencies, please ensure you run

```diff
pip install -r requirements.txt
```

### **1️⃣ You can obtain the results by cloning this repository and using the command line to run the required scripts.**

The user has two options depending on which arguments are chosen. Both of them need to take as input a tree in the Newick format (with nodes of any degree) with annotated branch lengths.

▶️ **Option 1: Generate $N$ FASTA files with alignments of length $L$ given a Newick tree**

The program generates a set of transition matrices according to the input tree <tree.txt> and its branch lengths. From these matrices, $N$ different alignments of length $L$ are simulated
A root distribution input parameter also needs to be passed: we can impose a random distribution or a specific one. 
The outputs (a .txt file with the transition matrices and a .tar with the .FASTA files corresponding to the simulated alignments) can be named using the <experiment_name> input parameter and  are saved in the output_files directory 

An example with $N = 5$ and $L=1000$:

Using a random root distribution:
```diff
python3 GenPhylo.py <tree.txt> 5 1000 random <experiment_name>
```
Using a specific root distribution (note that A,G,C,T must be values that sum up to 1)
```diff
python3 GenPhylo.py <tree.txt> 5 1000 "[A,G,C,T]" <experiment_name>
```

▶️ **Option 2: Generate FASTA files with alignments of given lengths $L_1,...,L_d$ given a Newick tree**

Working very similarly as the first option, the second one allows to generate aligments of different length. The program generates a set of transition matrices according to the input tree <tree.txt> and its branch lengths and from these matrices, alignments of length  $L_1,...,L_d$ are generated (we can add as many lengths as alignments we want to generate. ). The outputs are saved the same way as described for Option 1.

An example, for $L_1 = 500$, $L_2 = 1000$ and $L_3 = 10000$

Using a random root distribution:
```diff
python3 GenPhylo.py <tree.txt> L500 L1000 L10000 random <experiment_name>
```
Using a specific root distribution (note that A,G,C,T must be values that sum up to 1)
```diff
python3 GenPhylo.py <tree.txt> L500 L1000 L10000 "[A,G,C,T]" <experiment_name>
```
⚠️ Note that in this case, sequence lengths are preceeded by an $L$.

---

This repository includes the file IQ-TREE_analysis.pdf that describes how we verified the precision of our alignments simulator by using the phylogenetic software IQ-TREE.

---

### **2️⃣ You can obtain the results by installing our Python package.**

```diff
pip install genphylo
```

⚠️ Make sure you are using the latest version.

The following code produces the same outputs as the previous options:
```python
# Import our package
from GenPhylo.utils.alignments_generation import *

tree =           # path of your Newick file
L =              # length
N =              # number of different alignments
root_distr =     # root distribution ("random" or specified by the user)
name =           # name for the experiment

# Calling a package function that generates the N alignments
get_N_alignments(tree, L, N, root_distr, name)

lengths =        # list of lengths
root_distr =     # root distribution ("random" or specified by the user, e.g. [0.3, 0.2, 0.15, 0.35])
name =           # name for the experiment

# Calling a package function that generates the alignments given the lengths
get_alignments_by_lengths(tree, lengths, root_distr, name)
```

---

⚙️ This software is developped under de GNU General Public License v3.

---

If you use our code, either for your experiments or to develop future research, please cite it:
```
TO BE FILLED!
```



