"""Assignment 2: Modelling CS Education research paper data

=== CSC148 Winter 2019 ===
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2019 Bogdan Simion, David Liu, Diane Horton, Jacqueline Smith

=== Module Description ===
This module contains a new class, PaperTree, which is used to model data on
publications in a particular area of Computer Science Education research.
This data is adapted from a dataset presented at SIGCSE 2019.
You can find the full dataset here: https://www.brettbecker.com/sigcse2019/

Although this data is very different from filesystem data, it is still
hierarchical. This means we are able to model it using a TMTree subclass,
and we can then run it through our treemap visualisation tool to get a nice
interactive graphical representation of this data.

Recommended steps:
1. Start by reviewing the provided dataset in cs1_papers.csv. You can assume
   that any data used to generate this tree has this format,
   i.e., a csv file with the same columns (same column names, same order).
   The categories are all in one column, separated by colons (':').
   However, you should not make assumptions about what the categories are, how
   many categories there are, the maximum number of categories a paper can have,
   or the number of lines in the file.

2. Read through all the docstrings in this file once. There is a lot to take in,
   so don't feel like you need to understand it all the first time.
   Draw some pictures!
   We have provided the headers of the initializer as well as of some helper
   functions we suggest you implement. Note that we will not test any
   private top-level functions, so you can choose not to implement these
   functions, and you can add others if you want to for your solution.
   For this task, we will be testing that you are building the correct tree,
   not that you are doing it in a particular way. We will access your class
   in the same way as in the client code in the visualizer.

3. Plan out what you'll need to do to implement the PaperTree initializer.
   In particular, think about how to use the boolean parameters to do different
   things in setting up the tree. You may also find it helpful to review the
   Python documentation about the csv module, which you are permitted and
   encouraged to use. You should have a good plan, including what your subtasks
   are, before you begin writing any code.

4. Write the code for the PaperTree initializer and any helper functions you
   want to use in your design. You should not make any changes to the public
   interface of this module, or of the PaperTree class, but you can add private
   attributes and helpers as needed.

5. Tidy and test your code, and try it with the visualizer client code. Make
   sure you have documented any new private attributes, and that PyTA passes
   on your code.
"""
import csv
from typing import List, Dict, Tuple
from tm_trees import TMTree

# Filename for the dataset
DATA_FILE = 'cs1_papers.csv'


class PaperTree(TMTree):
    """A tree representation of Computer Science Education research paper data.

    === Private Attributes ===
    _authors:
        The author(s) of the paper.
    _doi:
        The Url of the paper.

    These should store information about this paper's <authors> and <doi>.

    === Inherited Attributes ===
    rect:
        The pygame rectangle representing this node in the treemap
        visualization.
    data_size:
        The size of the data represented by this tree.
    _colour:
        The RGB colour value of the root of this tree.
    _name:
        The root value of this tree, or None if this tree is empty.
    _subtrees:
        The subtrees of this tree.
    _parent_tree:
        The parent tree of this tree; i.e., the tree that contains this tree
        as a subtree, or None if this tree is not part of a larger tree.
    _expanded:
        Whether or not this tree is considered expanded for visualization.

    === Representation Invariants ===
    - All TMTree RIs are inherited.
    """
    _authors: str
    _doi: str

    def __init__(self, name: str, subtrees: List[TMTree], authors: str = '',
                 doi: str = '', citations: int = 0, by_year: bool = True,
                 all_papers: bool = False) -> None:
        """Initialize a new PaperTree with the given <name> and <subtrees>,
        <authors> and <doi>, and with <citations> as the size of the data.

        If <all_papers> is True, then this tree is to be the root of the paper
        tree. In that case, load data about papers from DATA_FILE to build the
        tree.

        If <all_papers> is False, Do NOT load new data.

        <by_year> indicates whether or not the first level of subtrees should be
        the years, followed by each category, subcategory, and so on. If
        <by_year> is False, then the year in the dataset is simply ignored.
        """

        self._authors = authors
        self._doi = doi
        # self._by_year = by_year
        if not all_papers:
            TMTree.__init__(self, name, subtrees, citations)
        else:
            d = _load_papers_to_dict(by_year)
            subtrees.extend(_build_tree_from_dict(d))
            TMTree.__init__(self, name, subtrees, citations)

    def get_separator(self) -> str:
        """Return the string used to separate names in the string
        representation of a path from the tree root to this tree.
        """
        return ': '

    def get_suffix(self) -> str:
        """Return the string used at the end of the string representation of
        a path from the tree root to this tree.
        """
        if len(self._subtrees) == 0:
            return ' (paper)'
        else:
            return ' (category)'


def _load_papers_to_dict(by_year: bool = True) -> Tuple[Dict, List]:
    """Return a nested dictionary of the data read from the papers dataset file.

    If <by_year>, then use years as the roots of the subtrees of the root of
    the whole tree. Otherwise, ignore years and use categories only.
    """
    with open(DATA_FILE, newline='') as f:
        reader = csv.DictReader(f)
        if by_year:
            d = ({}, [])
            for row in reader:
                year = row['Year']
                category = row['Category'].split(':')
                for i in range(len(category)):
                    category[i] = category[i].strip()
                d_2 = d[0]
                if year in d_2:
                    d_2 = d_2[year][0]
                else:
                    d_2[year] = ({}, [])
                    d_2 = d_2[year][0]
                for i in range(len(category)):
                    if category[i] in d_2:
                        if i != len(category) - 1:
                            d_2 = d_2[category[i]][0]
                    else:
                        d_2[category[i]] = ({}, [])
                        if i != len(category) - 1:
                            d_2 = d_2[category[i]][0]
                d_2[category[-1]][1].append(row)
            return d

        else:
            d = ({}, [])
            for row in reader:
                # category = [x.strip() for x in row['Category'].split(':')]
                category = row['Category'].split(':')
                for i in range(len(category)):
                    category[i] = category[i].strip()
                d_2 = d[0]
                for i in range(len(category)):
                    if category[i] in d_2:
                        if i != len(category) - 1:
                            d_2 = d_2[category[i]][0]
                    else:
                        d_2[category[i]] = ({}, [])
                        if i != len(category) - 1:
                            d_2 = d_2[category[i]][0]
                d_2[category[-1]][1].append(row)
            return d


def _build_tree_from_dict(nested_dict: Tuple[Dict, List]) -> List[PaperTree]:
    """Return a list of trees from the nested dictionary <nested_dict>.
    """
    tree = []
    d = nested_dict
    for d_2 in d[1]:
        name = d_2['Title']
        author = d_2['Author']
        doi = d_2['Url']
        citation = int(d_2['Citations'])
        tree.append(PaperTree(name, [], author, doi, citation))

    for sub in d[0]:
        paper = PaperTree(sub, _build_tree_from_dict(d[0][sub]))
        tree.append(paper)

    return tree


if __name__ == '__main__':
    # pass
    import python_ta
    python_ta.check_all(config={
        'allowed-import-modules': ['python_ta', 'typing', 'csv', 'tm_trees'],
        'allowed-io': ['_load_papers_to_dict'],
        'max-args': 8
    })
    # print(_load_papers_to_dict(True))
    # print(_build_tree_from_dict(({'FLP': ({'other': ({}, [])}, [])}, [])))
