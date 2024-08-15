Here's a project spec and starter code for your workshop on Git & GitHub, themed around math/matrices. The idea is to build a Python package for basic matrix operations. The project is designed to introduce participants to key Git and GitHub concepts like branching, pull requests (PRs), merge conflicts, and collaborative coding.

### Project Spec: Matrix Operations Python Package

#### Overview
In this project, you will collaborate to build a Python package that performs basic matrix operations. The project is split into tasks, each assigned to a specific team member. By the end of the workshop, you will have a working package and practical experience with Git & GitHub.

#### Objectives
- Learn how to create and structure a Python package.
- Understand Git workflow: cloning, branching, committing, and pushing.
- Gain experience with GitHub: pull requests, code reviews, and resolving merge conflicts.
- Implement matrix operations in Python.

#### Prerequisites
- Basic knowledge of Python.
- Familiarity with matrices and basic linear algebra concepts.
- A GitHub account.

#### Tasks
Each task is assigned to one or more team members. You'll need to work on your assigned functions, write tests, and handle documentation.

1. **Matrix Initialization**
    - **Task**: Implement a `Matrix` class that can store and display a matrix.
    - **Assigned to**: Person 1

2. **Matrix Addition**
    - **Task**: Implement the `__add__` method for matrix addition.
    - **Assigned to**: Person 2

3. **Matrix Multiplication**
    - **Task**: Implement the `__mul__` method for matrix multiplication.
    - **Assigned to**: Person 3

4. **Matrix Transposition**
    - **Task**: Implement the `transpose` method to return the transpose of a matrix.
    - **Assigned to**: Person 4

5. **Determinant Calculation**
    - **Task**: Implement a method to calculate the determinant of a matrix.
    - **Assigned to**: Person 1 & Person 3

6. **Inverse Calculation**
    - **Task**: Implement a method to calculate the inverse of a matrix (if it exists).
    - **Assigned to**: Person 2 & Person 4

7. **Testing**
    - **Task**: Write unit tests for each of the matrix operations.
    - **Assigned to**: All

8. **Documentation**
    - **Task**: Write docstrings for each method and class. Create a README file for the package.
    - **Assigned to**: All

### Project Setup

#### Repository Structure
```
matrix_operations/
│
├── matrix_operations/
│   ├── __init__.py
│   ├── matrix.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_matrix.py
│   └── test_utils.py
│
├── README.md
└── setup.py
```

#### Getting Started
1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/matrix-operations.git
    cd matrix-operations
    ```

2. **Create a Branch**
    ```bash
    git checkout -b feature/matrix-initialization
    ```

3. **Start Coding!**

4. **Commit Your Changes**
    ```bash
    git add .
    git commit -m "Implement Matrix class"
    ```

5. **Push and Create a PR**
    ```bash
    git push origin feature/matrix-initialization
    ```

6. **Review PRs and Resolve Conflicts**