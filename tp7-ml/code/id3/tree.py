import numpy as np
import pandas as pd
from collections import deque

class Node:
    def __init__(self, label=None, value=None, children=None, parentLabel = None):
        self.label = label
        self.parentLabel = parentLabel
        self.value = value
        self.children = children if children is not None else []


def plurality_value(examples):
    play_values = examples["play"].values
    unique, counts = np.unique(play_values, return_counts=True)
    index = np.argmax(counts)
    return unique[index]

def b(q):
    return -(q*np.log2(q) + (1-q)*np.log2(1-q))

def remainder(play,att):
    possible_values = play[att].unique()
    res = 0
    for v in possible_values:
        ex = play[play[att] == v]
        pk = len(ex[ex["play"] == "yes"])
        nk = len(ex[ex["play"] == "no"])

        res += (pk + nk)/len(play) * b(pk/len(play))
        
    return res

def information_gain(examples, attribute):
    positive_class = len(examples[examples["play"] == "yes"])
    negative_class = len(examples[examples["play"] == "no"])
    r = b(positive_class/(positive_class + negative_class)) - remainder(examples, attribute)
    return r


def learn_tree(examples, attributes, parent_examples, previous_attribute):
    if examples.empty:
        return Node(label=previous_attribute, value=plurality_value(parent_examples))
    elif examples["play"].nunique() == 1:
        return Node(label=examples[previous_attribute].values[0], value=examples["play"].values[0])
    elif attributes == []:
        return Node(label=previous_attribute, value=plurality_value(examples))
    else:
        arg = np.argmax([information_gain(examples, a) for a in attributes])
        tree = Node(label=attributes[arg], parentLabel="nose")

        for v in examples[attributes[arg]].unique():
            e = examples[examples[attributes[arg]] == v]
            root = Node(parentLabel=attributes[arg], value=v)
            subtree = learn_tree(e, attributes[:arg] + attributes[arg+1:], examples, attributes[arg])
            root.children.append(subtree)
            tree.children.append(root)

        return tree
        
def print_bfs_tree(tree):
    if tree is None:
        return

    queue = deque()
    queue.append(tree)

    while queue:
        node = queue.popleft()

        # Print the node's information based on your custom structure
        if node.label != None:
            print("Attribute:", node.label)

        if node.value != None:
            print("Value:", node.value)

        if node.parentLabel != None:
            print("Parent:", node.parentLabel)
        
        print("--")

        for child in node.children:
            queue.append(child)

if __name__ == "__main__":
    ds = pd.read_csv("tp7-ml/code/id3/tennis.csv")
    print(plurality_value(ds))

    print("Starting decision tree")

    tree = learn_tree(ds, ["outlook", "temp", "humidity", "windy"], None, None)
    print_bfs_tree(tree)
    

