# AI Training Portfolio — Mathematics and Python Evaluation

[![Tests](https://github.com/loulounassih-prog/ai-training-portfolio/actions/workflows/tests.yml/badge.svg)](https://github.com/loulounassih-prog/ai-training-portfolio/actions/workflows/tests.yml)

This repository contains original examples of AI-response evaluation in mathematics and Python. Each case presents a technical task, a plausible but flawed model answer, a criterion-based evaluation, a calibrated score, a rigorous reference or corrected solution, and executable tests when code is involved.

The portfolio demonstrates the ability to:

- locate the first invalid step in otherwise plausible reasoning;
- distinguish a correct conclusion from a valid proof;
- grade against an explicit 10-point rubric;
- accept mathematically or algorithmically equivalent valid methods;
- write concise technical feedback and reference solutions;
- design tests that separate plausible code from correct code.

## Evaluation Cases

| Case | Domain | Error evaluated |
|---|---|---|
| [Positive Definite Matrix](math_reasoning/01_positive_definite_matrix/) | Linear algebra | Confusing positive definiteness with entrywise positivity |
| [Uncorrelated vs Independent](math_reasoning/02_uncorrelated_vs_independent/) | Probability | Treating one moment identity as independence |
| [Convex Optimization Condition](math_reasoning/03_convex_optimization_condition/) | Optimization | Treating stationarity as global optimality without convexity |
| [Uniform Convergence and Derivatives](math_reasoning/04_uniform_convergence_and_derivatives/) | Real analysis | Interchanging differentiation and a limit without sufficient hypotheses |
| [Binary Search Edge Cases](coding_evals/case_01_binary_search_edge_cases/) | Algorithms | Using an exclusive loop condition with inclusive search bounds |
| [Dependency Resolution and Cycle Detection](coding_evals/case_02_dependency_resolution_cycles/) | Graph algorithms | Using one DFS state and therefore failing to detect cycles |

## Standard Case Structure

Mathematics cases contain:

```text
prompt.md
model_answer.md
evaluation.md
reference_solution.md
rubric.md
```

Coding cases contain:

```text
task.md
model_answer.py
evaluation.md
corrected_solution.py
test_model_answer.py
test_corrected_solution.py
rubric.md
```

The tests for a flawed model answer document expected failures with strict `xfail` markers. Tests for corrected solutions contain no expected failures. A green test run therefore means that the corrected implementations pass and that each documented defect in a model answer still fails for the intended reason.

## Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── tests.yml
├── coding_evals/
│   ├── __init__.py
│   ├── case_01_binary_search_edge_cases/
│   │   ├── __init__.py
│   │   ├── corrected_solution.py
│   │   ├── evaluation.md
│   │   ├── model_answer.py
│   │   ├── rubric.md
│   │   ├── task.md
│   │   ├── test_corrected_solution.py
│   │   └── test_model_answer.py
│   └── case_02_dependency_resolution_cycles/
│       ├── __init__.py
│       ├── corrected_solution.py
│       ├── evaluation.md
│       ├── model_answer.py
│       ├── rubric.md
│       ├── task.md
│       ├── test_corrected_solution.py
│       └── test_model_answer.py
├── math_reasoning/
│   ├── 01_positive_definite_matrix/
│   ├── 02_uncorrelated_vs_independent/
│   ├── 03_convex_optimization_condition/
│   └── 04_uniform_convergence_and_derivatives/
├── .gitignore
├── LICENSE
├── pytest.ini
├── README.md
└── requirements.txt
```

Each mathematics directory contains the five standard mathematics files listed above.

## Requirements

- Python 3.11 or later
- `pytest`

Install the test dependency:

```bash
python -m pip install -r requirements.txt
```

Run the complete suite from the repository root:

```bash
python -m pytest -q
```

## Evaluation Methodology

Every evaluation begins with the task requirements rather than the reference solution's wording. The score is computed criterion by criterion from the accompanying rubric, whose maximum is exactly 10 points. Major logical or algorithmic defects receive substantially larger deductions than presentation issues. Equivalent rigorous proofs, valid counterexamples, and valid topological orders receive full credit for the relevant criteria.

## Originality and Confidentiality

All examples in this repository are original portfolio samples. They do not reproduce confidential assessment material, private company instructions, or platform-specific evaluation content.