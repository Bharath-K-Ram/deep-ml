import math
from collections import Counter

def calculate_entropy(labels: list) -> float:
    """Calculate the entropy of a list of labels."""
    N = len(labels)
    entropy = 0.0
    for count in Counter(labels).values():
        p = count / N
        entropy -= p * math.log2(p)
    return entropy

def calculate_information_gain(examples: list[dict], attr: str, target_attr: str) -> float:
    """Calculate the information gain of splitting on attr."""
    N = len(examples)
    base_entropy = calculate_entropy([ex[target_attr] for ex in examples])

    subsets = {}
    for example in examples:
        k = example[attr]
        v = example[target_attr]
        if k in subsets:
            subsets[k].append(v)
        else:
            subsets[k] = [v]

    weighted_entropy = sum(
        (len(labels) / N) * calculate_entropy(labels)
        for labels in subsets.values()
    )
    return base_entropy - weighted_entropy

def majority_class(examples: list[dict], target_attr: str) -> str:
    """Return the majority class. Break ties alphabetically."""
    counts = Counter(ex[target_attr] for ex in examples)
    max_value = max(counts.values())
    tied = [label for label, count in counts.items() if count == max_value]
    return sorted(tied)[0]

def learn_decision_tree(examples: list[dict], attributes: list[str], target_attr: str) -> dict:
    """Build a decision tree using the ID3 algorithm."""
    if not examples:
        return None

    labels = [ex[target_attr] for ex in examples]

    # Base case 1: pure node
    if len(set(labels)) == 1:
        return labels[0]

    # Base case 2: no attributes left to split on
    if not attributes:
        return majority_class(examples, target_attr)

    # Choose best attribute (strict '>' keeps the first one on ties)
    best_attr, best_gain = None, -1.0
    for attr in attributes:
        gain = calculate_information_gain(examples, attr, target_attr)
        if gain > best_gain:
            best_attr, best_gain = attr, gain

    tree = {best_attr: {}}
    remaining = [a for a in attributes if a != best_attr]

    # Group rows by best_attr value in one pass
    groups = {}
    for ex in examples:
        groups.setdefault(ex[best_attr], []).append(ex)

    # Build one subtree per value, in sorted order
    for value in sorted(groups):
        tree[best_attr][value] = learn_decision_tree(groups[value], remaining, target_attr)

    return tree