# Python Data Types & Core Structures Practice

This repository contains a structured set of exercises focused on exploring and manipulating Python's built-in data types. The project covers foundational concepts required for data analysis, focusing on casting, indexing, string formatting, and dynamic data structures.

---

## 📌 Project Features

The codebase handles operations across essential Python types:
* **Numeric Casting:** Interconverting between `int` and `float`, handling numeric truncation.
* **String Parsing & Formatting:** Extracting sub-strings, character indices, using `.replace()`, and leveraging precision layout (`:.2f`) via `f-strings`.
* **Dynamic Sequences:** Mutating data arrays, alphabetical sorting, element extraction via `.pop()`, and list-to-string conversions using `.join()`.
* **Key-Value Pairs & Sets:** Manipulating dictionary lists, managing immutable tuples through mutable type-casting, and utilizing unique property handling in sets.

---

## 💻 Code Structure & Examples

Here is a quick look at how the code is structured and implemented using core features from the project:

### 1. Dictionary Iteration & Aggregation
Using loop structures to dynamically target value elements stored inside dictionaries:
```python
# Summing up numerical data stored inside dictionary values using loops
prices = {"apple": 5, "banana": 3}
total_revenue = 0

for price in prices.values():
    total_revenue += price
