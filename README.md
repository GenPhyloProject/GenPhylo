# GenPhylo: Generating Data on Phylogenetic trees

### Authors: Marta Casanellas, Martí Cortada, Adrià Diéguez

---

**GenPhylo** generates synthetic alignments on a phylogenetic tree with given branch lengths.

The user has two options depending on which arguments are chosen. But both possibilities need to take as input a tree in the Newick format (with nodes of any degree) with annotated branch lengths.

▶️ **Option 1: Generate $N$ FASTA files with alignments of length $L$ given a Newick tree**

For example, for $N = 5$ and $L = 1000$, provide a Newick tree in a ```.txt``` file, an experiment's name to save the results and the root distribution, type:

For a random root distribution:
```diff
python3 main.py <tree.txt> 5 1000 random <name_experiment>
```
For a specific root distribution (note that A,G,C,T must be values that sum up to 1)
```diff
python3 main.py <tree.txt> 5 1000 "[A,G,C,T]" <name_experiment>
```

and it generates $5$ Multiple Sequence Alignments (MSAs) of length 1000 evolving on the tree given in ```tree.txt``` under the general Markov model. The output result is a set of $5$ ```.fasta``` files.

▶️ **Option 2: Generate FASTA files with alignments of given lengths $L_1,...,L_d$ given a tree in a Newick format**

For example, for $L_1 = 500$, $L_2 = 1000$ and $L_3 = 10000$, provided also a Newick tree in a ```.txt``` file and an experiment's name to save the results; just type

```diff
python3 main.py <tree.txt> L500 L1000 L10000 <name_experiment>
```

where we can add as many lengths as alignments we want to generate. The previous command-line generates $3$ MSAs of lengths $500$, $1000$ and $10000$, respectively, all of them evolving on the tree given in ```tree.txt``` under the general Markov model. The output result is a set of $3$ ```.fasta``` files.

⚠️ Note that in this case, sequence lengths are preceeded by an $L$.




