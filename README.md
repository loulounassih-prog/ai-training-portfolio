# AI Training Portfolio — Math & Coding Evaluation

This repository contains original examples of math reasoning evaluation, coding review, and model-output assessment.

The purpose of this repository is to present clear, reproducible examples of how technical answers can be reviewed for correctness, reasoning quality, edge cases, and consistency with a given task.

## Contents

The repository is organized into four parts:

    math_reasoning/
        Mathematical problems, rigorous solutions, and reviews of incorrect reasoning.

    coding_evals/
        Python code review examples, corrected implementations, and unit tests.

    model_evaluation/
        Pairwise evaluations of candidate model answers using explicit criteria.

    rubrics/
        General rubrics for evaluating math reasoning and coding responses.

## Evaluation Principles

The examples focus on evaluating whether an answer is correct, justified, complete, and aligned with the original prompt.

A technical answer is not considered correct only because it is fluent or convincing. The reasoning must be checked step by step.

The main evaluation criteria are:

- correctness of the final answer;
- validity of the reasoning;
- presence of hidden assumptions;
- treatment of edge cases;
- clarity of explanation;
- consistency with the task;
- usefulness of the feedback.

## Math Reasoning Examples

The math examples include:

- a problem statement;
- a rigorous solution;
- a review of a plausible but incorrect solution.

The reviews focus on identifying the exact point where the reasoning fails, explaining why it fails, and providing a corrected argument when needed.

## Coding Evaluation Examples

The coding examples include:

- an incorrect or incomplete implementation;
- a corrected implementation;
- unit tests;
- a short review explaining the bug and the correction.

The reviews focus on correctness, boundary cases, input handling, and test coverage.

## Model Evaluation Examples

The model evaluation examples compare two candidate answers to the same task.

Each comparison uses explicit criteria to separate different aspects of answer quality, such as correctness, reasoning, completeness, and clarity.

The objective is not only to select the better answer, but also to explain why it is better.

## Running Tests

Install the required dependency:

    pip install -r requirements.txt

Run the tests with:

    pytest

## Scope

This is a small portfolio repository, not a large software project.

The examples are intentionally focused and self-contained. They are designed to make the evaluation process easy to inspect.

## Notes

All examples are original portfolio samples.

No private assessment material, confidential platform content, or proprietary guidelines are included.