# Day 2 — Functions, Lists & Dictionaries

## Overview

In this day, I learned how to use **functions**, **lists**, and **dictionaries** in Python. These are very important concepts and are used in almost every real-world project.

---

# Concepts Learned

## Functions

Functions are reusable blocks of code. They take input, process it, and return output.

**Why use functions?**

* Avoid repeating code
* Make code clean and readable

---

## Lists

A list is used to store multiple items in a specific order.

```python
numbers = [10, 20, 30]
```

**Use when:**

* You have multiple values
* Order matters

---

## Dictionaries

A dictionary stores data in key-value pairs.

```python
student = {"name": "Ali", "age": 20}
```

**Use when:**

* Data has labels (like name, age)
* You want fast access using keys

---

# Difference Between List and Dictionary

| List                  | Dictionary                     |
| --------------------- | ------------------------------ |
| Stores items in order | Stores data as key-value pairs |
| Access using index    | Access using key               |
| Example: `[10, 20]`   | Example: `{"name": "Ali"}`     |

---

# Exercise 1 — Word Frequency Counter

## Goal

Count how many times each word appears in a paragraph.

## What I did:

* Converted text to lowercase
* Removed punctuation
* Split text into words
* Counted each word using a dictionary
* Sorted and printed top 5 words

## Key Learning:

* Dictionary is perfect for counting
* Loop + condition helps build logic
* Sorting using `sorted()` and `lambda`

---

# Exercise 2 — Grade Book System

## Goal

Create a system to manage student grades.

## What I did:

* Stored students in a list of dictionaries
* Each student has name, scores, subject
* Created functions:

  * `calculate_average(scores)`
  * `get_grade(avg)`
  * `class_topper(students)`
* Printed formatted report
* Highlighted topper
* Sorted students by average (without changing original list)

## Key Learning:

* Real-world data structure (list of dicts)
* Function reuse
* Sorting with custom logic
* Clean formatted output

---

# Conclusion

Today I learned:

* How to write functions confidently
* How to use lists and dictionaries in real problems
* How to structure and process real-world data

These concepts are very important and will be used daily in development.

---

# GitHub

**Commit Message:**

```
day-2: functions + list/dict exercises
```

---
