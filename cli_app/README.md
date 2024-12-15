# Executing GenPhylo from the CLI

To get started, simply clone this directory into your local space, which allows you to work with the files directly without needing to install the package.

There are two options available: one replicates the behavior of `get_N_alignments()`, while the other performs the functionality of `get_alignments_by_lengths()`.

▶️ **Option 1: Generate $N$ FASTA files with alignments of length $L$ given a Newick tree**

This option is equivalent to `get_N_alignments()`. The program generates a set of transition matrices according to the input tree <tree.txt> and its branch lengths. From these matrices, $N$ different alignments of length $L$ are simulated. A root distribution input parameter also needs to be passed: we can impose a random distribution or a specific one. 

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

This option is equivalent to `get_alignments_by_lengths()`. Working very similarly as the first option, the second one allows to generate aligments of different lengths. The program generates a set of transition matrices according to the input tree <tree.txt> and its branch lengths and from these matrices, alignments of length  $L_1,...,L_d$ are generated (we can add as many lengths as alignments we want to generate. ). The outputs are saved the same way as described for Option 1.

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

▶️ To get a quick overview of how to use GenPhylo, simply run the following command:

```diff
python3 GenPhylo.py --help
```

or

```diff
python3 GenPhylo.py -h
```

This will display a brief description of the program, including its features, available command-line arguments, and usage examples.
