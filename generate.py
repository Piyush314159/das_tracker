#!/usr/bin/env python3
"""
Run this script from your repo root whenever you add a new .py file:
    python generate.py

It scans all topic folders and writes problems.json automatically.
"""

import os
import json

TOPICS = [
    # Sorting
    {"folder": "sorting-selection",           "title": "Selection Sort"},
    {"folder": "sorting-bubble",              "title": "Bubble Sort"},
    {"folder": "sorting-insertion",           "title": "Insertion Sort"},
    {"folder": "sorting-recursive-bubble",    "title": "Recursive Bubble Sort"},
    {"folder": "sorting-recursive-insertion", "title": "Recursive Insertion Sort"},
    {"folder": "sorting-merge",               "title": "Merge Sort"},
    {"folder": "sorting-quick",               "title": "Quick Sort"},
    # DSA
    {"folder": "binary-search",        "title": "Binary Search"},
    {"folder": "strings",              "title": "Strings"},
    {"folder": "linked-list",          "title": "Linked List"},
    {"folder": "recursion",            "title": "Recursion"},
    {"folder": "bit-manipulation",     "title": "Bit Manipulation"},
    {"folder": "stack-queue",          "title": "Stack & Queue"},
    {"folder": "two-pointers",         "title": "Two Pointers"},
    {"folder": "heaps",                "title": "Heaps"},
    {"folder": "greedy",               "title": "Greedy Algorithms"},
    {"folder": "binary-tree",          "title": "Binary Tree"},
    {"folder": "binary-search-tree",   "title": "Binary Search Tree"},
    {"folder": "graphs",               "title": "Graphs"},
    {"folder": "dynamic-programming",  "title": "Dynamic Programming"},
    {"folder": "tries",                "title": "Tries"},
    {"folder": "strings-advanced",     "title": "Strings – Advanced"},
]

def parse_filename(filename):
    base = filename.replace(".py", "")
    parts = base.split("_")
    diff_words = {"easy", "medium", "hard"}
    diff = "medium"
    name_parts = parts
    if parts and parts[-1].lower() in diff_words:
        diff = parts[-1].lower()
        name_parts = parts[:-1]
    display = " ".join(w.capitalize() for w in name_parts)
    return {"filename": filename, "display": display, "diff": diff}

result = {}
total = 0

for topic in TOPICS:
    folder = topic["folder"]
    problems = []
    if os.path.isdir(folder):
        for fname in sorted(os.listdir(folder)):
            if fname.endswith(".py") and not fname.startswith("__"):
                problems.append(parse_filename(fname))
                total += 1
    result[folder] = problems

with open("problems.json", "w") as f:
    json.dump(result, f, indent=2)

print(f"✅ problems.json updated — {total} problems across {len(TOPICS)} topics")
