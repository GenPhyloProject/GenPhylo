# GenPhylo: Generating heterogeneous data on gene trees

### Authors: Marta Casanellas, Martí Cortada, Adrià Diéguez

---

We introduce **GenPhylo**, an open-source Python module for simulating genetic data along a phylogeny avoiding the restriction of continuous-time Markov processes. **GenPhylo** uses directly a general Markov model and therefore naturally incorporates heterogeneity across lineages. 

The module has been developed in Python3 and provides an algorithm that can be incorporated in other simulation software. 

### **Installation and requirements.**

Current version of **GenPhylo** is 1.0.0. You can install the package using pip

```diff
pip install GenPhylo
```
**GenPhylo** has several dependencies, please ensure you run

```diff
pip install -r requirements.txt
```
---

### **Using GenPhylo**

Given a tree topology, the branch lengths and the alignment lengths, **GenPhylo** generates GMM parameters and the corresponding alignments, saved in separated output files. Our package includes different options for generating the alignments, such as get_N_alignments(), which generates N alignments of a fixed length, or get_alignments_by_lengths(), which generates alignments of different lengths. Below we provide examples of how to use both functions.

**get_N_alignments()**

```python
# Import GenPhylo package
from GenPhylo.utils.alignments_generation import *

tree = 'tree.txt'       # path of your Newick file
L = 1000                # Alignment length
N = 50                  # Number of alignments
root_distr = 'random'   # root distribution (can also be specified by the user, e.g. root_distr = [0.22, 0.24, 0.28, 0.26])
name = 'experiment1'    # output name

# Calling the function that generates the N alignments
get_N_alignments(tree, L, N, root_distr, name)
```
**get_alignments_by_lengths()**

```python
# Import GenPhylo package
from GenPhylo.utils.alignments_generation import *

tree = 'tree.txt'               # path of your Newick file
lengths = [500, 1000, 10000]    # list of alignment lengths
root_distr = 'random'           # root distribution (can also be specified by the user, e.g. root_distr = [0.22, 0.24, 0.28, 0.26])
name = 'experiment2'            # output name

# Calling the function that generates the alignments given the lengths
get_alignments_by_lengths(tree, lengths, root_distr, name)
```
In each case, the outputs (a .txt file with the transition matrices and a .tar with the .FASTA files corresponding to the simulated alignments) are named using the <experiment_name>  parameter and are saved in a directory called output_files (if the folder does not already exist, the package will automatically create it).

▶️ **Option 1: Generate $N$ FASTA files with alignments of length $L$ given a Newick tree**

The program generates a set of transition matrices according to the input tree <tree.txt> and its branch lengths. From these matrices, $N$ different alignments of length $L$ are simulated
A root distribution input parameter also needs to be passed: we can impose a random distribution or a specific one. 


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
---

⚙️ This software is developped under de GNU General Public License v3.

---

If you use our code, either for your experiments or to develop future research, please cite it:
```
TO BE FILLED!
```
