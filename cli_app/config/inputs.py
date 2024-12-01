import sys
import os

def print_help():
    """
    Prints the help message with usage instructions for the CLI.
    """
    help_message = """
Usage: python script.py <tree_file> [options]

Options:
  Case 1: Single alignment length and number of alignments
    python script.py <tree_file> T L <root_distr> <output_name>

    Arguments:
      <tree_file>     Path to the Newick tree file.
      T               Number of alignments to generate.
      L               Alignment length.
      <root_distr>    Root distribution (e.g., 'random').
      <output_name>   Output name for the results.

  Case 2: Multiple alignment lengths
    python script.py <tree_file> L<length1> L<length2> ... <root_distr> <output_name>

    Arguments:
      <tree_file>     Path to the Newick tree file.
      L<length>       Alignment lengths, prefixed with 'L' (e.g., L1000).
      <root_distr>    Root distribution (e.g., 'random').
      <output_name>   Output name for the results.

General Options:
  -h, --help         Show this help message and exit.

Examples:
  python script.py tree4_01.txt 100 1000 random output1
  python script.py tree4_01.txt L1000 L10000 random output2
"""
    print(help_message)
    sys.exit(0)

def reading():
    """
    Reads and parses the command-line arguments.
    """
    # Check for help flag
    if '-h' in sys.argv or '--help' in sys.argv:
        print_help()

    # GenGM options
    output_dir = './output_files'
    # Check if the directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    tree = sys.argv[1]
    case = 1
    num_lengths = len(sys.argv)
    lengths = []
    name = None
    root_distr = None

    # Determine case based on argument structure
    if sys.argv[-3].startswith("L"):
        # Case 2: Multiple alignment lengths
        for i in range(2, num_lengths - 2):
            lengths.append(int(sys.argv[i][1:]))
            case = 2
        name = sys.argv[-1]
        root_distr = sys.argv[-2]
        return tree, case, lengths, None, root_distr, name
    else:
        # Case 1: Single alignment length and number of alignments
        t = int(sys.argv[2])
        L = int(sys.argv[3])
        name = sys.argv[-1]
        root_distr = sys.argv[-2]
        return tree, case, t, L, root_distr, name
