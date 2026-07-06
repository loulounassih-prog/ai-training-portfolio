# AI Training Portfolio — Math & Coding Evaluation

This repository contains short technical examples of AI response evaluation in mathematics and coding.

Each example includes a prompt or task, a plausible flawed model answer, an evaluation of that answer, a correct reference solution, and a scoring rubric.

## Repository Structure

    math_reasoning/
    ├── 01_positive_definite_matrix/
    ├── 02_uncorrelated_vs_independent/
    └── 03_convex_optimization_condition/

    coding_evals/
    └── 01_binary_search_edge_cases/

## Example Format

Math examples use the following structure:

    prompt.md
    model_answer.md
    evaluation.md
    reference_solution.md
    rubric.md

Coding examples use the following structure:

    task.md
    model_answer.py
    evaluation.md
    corrected_solution.py
    test_binary_search.py
    rubric.md

## Current Examples

### Positive Definite Matrix

Evaluates a flawed proof claiming that positive definite matrices must have positive entries.

Main issue: positive definiteness is a condition on the quadratic form, not on individual matrix entries.

### Uncorrelated vs Independent

Evaluates the common mistake of assuming that zero covariance implies independence.

Main issue: independence implies zero covariance under suitable assumptions, but the converse is false in general.

### Convex Optimization Condition

Evaluates the claim that a zero gradient always implies a global minimum.

Main issue: a stationary point is not necessarily a global minimizer without additional assumptions such as convexity.

### Binary Search Edge Cases

Evaluates a binary search implementation that fails on boundary cases.

Main issue: the loop condition misses the final candidate position in some cases.

## Running Tests

Install dependencies:

    pip install -r requirements.txt

Run tests:

    pytest

## Notes

All examples are original portfolio samples.

No confidential assessment material or platform-specific guidelines are included.