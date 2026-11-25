# Module 01 – Introduction to AI & Python

**Internship:** Codomax Digital Solutions  
**Role:** AI & ML Intern  
**Level:** Beginner

---

## 1. Introduction to Artificial Intelligence

### What is Artificial Intelligence?
Artificial Intelligence (AI) is a field of technology that enables computers and machines to perform tasks that normally require human intelligence. Examples of these tasks include understanding language, recognising images, learning patterns, solving problems and making predictions.

### Examples
- A navigation app suggesting a route based on traffic.
- An email service identifying possible spam.
- A chatbot answering questions.
- A shopping application recommending products.

### How an AI system commonly works
1. **Data collection:** Information such as text, images or numbers is collected.
2. **Training:** A model learns patterns from examples.
3. **Processing:** The trained model receives new information.
4. **Output:** The system produces an answer, prediction or classification.

### Broad categories often introduced in AI
- **Narrow AI:** Designed to perform a specific task. Most AI applications in use today fit this category.
- **Artificial General Intelligence (AGI):** A proposed form of AI with broad, human-like ability across many tasks; it has not been achieved.
- **Artificial Superintelligence (ASI):** A hypothetical form of AI that would exceed human intelligence.

### Advantages
- Automates repetitive tasks.
- Can process large amounts of data quickly.
- Can support decision-making.
- Can operate continuously.

### Limitations and concerns
- Can produce incorrect results.
- Can reflect bias in its data or design.
- Can create privacy concerns.
- Can require significant computing resources.
- Can change the skills required for some jobs.

---

## 2. AI, Machine Learning and Deep Learning

### Artificial Intelligence (AI)
The broad field of building systems that perform tasks associated with human intelligence.

### Machine Learning (ML)
A subset of AI in which systems learn patterns from data and use those patterns to make predictions or decisions.

**Example:** A spam filter learns from examples of spam and non-spam messages.

### Deep Learning (DL)
A subset of machine learning that uses neural networks with multiple layers to learn complex patterns.

**Example:** A system that recognises objects in images.

### Relationship
Deep Learning is part of Machine Learning, and Machine Learning is part of Artificial Intelligence.

| Feature | AI | ML | Deep Learning |
|---|---|---|---|
| Scope | Broad field | Subset of AI | Subset of ML |
| Main idea | Intelligent behaviour | Learning patterns from data | Learning complex patterns with multi-layer neural networks |
| Example | A rule-based or learning-based assistant | Spam classification | Image recognition |

Note: Real products may combine several techniques, so examples are simplified.

---

## 3. Real-world applications of AI

1. **Healthcare:** Helps analyse medical images and supports clinical workflows.
2. **Education:** Supports personalised learning, tutoring and feedback.
3. **Banking:** Helps monitor transactions and identify unusual patterns.
4. **Agriculture:** Can support crop monitoring and analysis.
5. **Transportation:** Helps with traffic prediction, route planning and driver assistance.
6. **E-commerce:** Recommends products based on user activity and preferences.

AI outputs should be checked, especially when decisions affect people's health, finances or safety.

---

## 4. Python programming fundamentals

### What is Python?
Python is a high-level, general-purpose programming language known for readable syntax. It is used in AI, machine learning, data science, automation, web development and general software development.

### First program
```python
print("Hello, World!")
```
`print()` displays output.

### Variables
A variable is a name that refers to a value.
```python
name = "Anitha"
age = 18
course = "CSE"

print(name)
print(age)
print(course)
```

### Common data types
| Type | Meaning | Example |
|---|---|---|
| `int` | Whole number | `10` |
| `float` | Decimal number | `10.5` |
| `str` | Text | `"Python"` |
| `bool` | True or False | `True` |
| `list` | Ordered collection | `[10, 20, 30]` |

Check a value's type using `type()`:
```python
value = 10.5
print(type(value))
```

### Input
`input()` reads text entered by the user.
```python
name = input("Enter your name: ")
print("Welcome", name)
```
Convert input when a number is required:
```python
age = int(input("Enter your age: "))
```

### Operators
| Operator | Purpose | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `%` | Remainder | `10 % 3` |
| `//` | Floor division | `10 // 3` |
| `**` | Exponentiation | `2 ** 3` |

### Conditional statements
Conditions allow a program to choose which block to execute.
```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```
Python uses indentation to define code blocks.

### Loops
A `for` loop iterates over a sequence or range:
```python
for number in range(1, 6):
    print(number)
```

A `while` loop repeats while its condition is true:
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

### Functions
A function is a reusable block of code.
```python
def add(first, second):
    return first + second

answer = add(10, 20)
print(answer)
```
- `def` starts a function definition.
- `first` and `second` are parameters.
- `return` sends a result back to the caller.

### Lists
A list stores multiple values in an ordered collection. Indexing starts at zero.
```python
numbers = [10, 20, 30]
print(numbers[0])  # 10

numbers.append(40)
numbers.remove(20)
print(numbers)
print(len(numbers))
```

---

## 5. Beginner Python programs

The accompanying `programs/` folder contains runnable examples:
1. Print a welcome message.
2. Display variables and data types.
3. Add two user-entered numbers.
4. Check even or odd.
5. Find the largest of three numbers.
6. Check whether a number is prime.
7. Calculate factorial.
8. Reverse a non-negative integer.
9. Generate a Fibonacci sequence.
10. Calculate the sum of list elements.




## 6. Learning outcome

After studying this module, I can:
- Explain the basic meaning and applications of AI.
- Describe the relationship between AI, ML and Deep Learning.
- Identify common real-world AI applications.
- Write simple Python programs.
- Use variables, data types, operators, conditions, loops, functions and lists.

**Note:** This document is a beginner study guide prepared from the Module 01 objectives shown in the internship dashboard. Follow any additional instructions or formats provided by the internship coordinator.
