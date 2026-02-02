# Project 2: Symbolic Differentiator - Your Assignment

**CSC3301 Programming Language Paradigms**
**Student ID:** differentiator
**Weight:** 5.5% | **Language:** Scheme (Racket)

---

## Your Variant Configuration

Your assignment has been customized based on your student ID. You must implement the following:

### Required Trigonometric Functions

You must implement differentiation for these trigonometric functions:

- **cos** (derivative of cos)
- **sin** (derivative of sin)
- **tan** (derivative of tan)

### Derivative Rules to Implement

- `d/dx[cos(u)] = -sin(u) * u'`
- `d/dx[sin(u)] = cos(u) * u'`
- `d/dx[tan(u)] = sec^2(u) * u'`

---

## Overview

Implement a symbolic differentiation system in Scheme/Racket that computes derivatives of mathematical expressions symbolically (not numerically) and simplifies the results.

## Expression Representation

Expressions are represented as S-expressions (nested lists):

```scheme
'(+ x 3)           ; x + 3
'(* 2 x)           ; 2 * x
'(^ x 3)           ; x^3
'(sin x)           ; sin(x)
'(cos (* 2 x))     ; cos(2x)
```

## Requirements

### Part 1: Basic Derivatives (Milestone 1 - 25%)

Implement `deriv` function for:
- Constants: `d/dx[c] = 0`
- Variables: `d/dx[x] = 1`, `d/dx[y] = 0`
- Sum rule: `d/dx[u + v] = du/dx + dv/dx`
- Product rule: `d/dx[u * v] = u'v + uv'`

### Part 2: Advanced Functions (Milestone 2 - 35%)

Implement derivatives for:
- Power rule: `d/dx[x^n] = n * x^(n-1)`
- Chain rule for composite functions
- **Your required trigonometric functions** (see above)

### Part 3: Simplification (Milestone 3 - 25%)

Implement `simplify` function:
- Zero elimination: `0 + x = x`, `0 * x = 0`
- Identity simplification: `1 * x = x`
- Constant folding: `2 + 3 = 5`

### Part 4: Complete Implementation (Final - 15%)

- All tests passing
- Clean, documented code
- Additional simplification rules

---

## Your Test Expressions

Based on your variant, these expressions will be used in testing:

- `'(+ (* 7 (^ x 2)) (* 4 x) 5)` (7x^2 + 4x + 5) - Type: polynomial
- `'(^ x 2)` (x^2) - Type: power
- `'(* 3 (^ x 2))` (3 * x^2) - Type: product
- `'(cos x)` (cos(x)) - Type: trigonometric
- `'(sin x)` (sin(x)) - Type: trigonometric
- `'(tan (* 3 x))` (tan(3x)) - Type: chain_rule

---

## Example Usage

```scheme
;;; Basic derivatives
(deriv 5 'x)           ; => 0
(deriv 'x 'x)          ; => 1
(deriv '(+ x 3) 'x)    ; => (+ 1 0) or simplified: 1

;;; Power rule
(deriv '(^ x 3) 'x)    ; => (* 3 (^ x 2))

;;; Product rule
(deriv '(* x x) 'x)    ; => (+ (* 1 x) (* x 1)) or simplified: (* 2 x)

;;; Chain rule with trig
(deriv '(sin (* 2 x)) 'x)  ; => (* (cos (* 2 x)) 2)
```

---

## Submission

1. Complete `src/differentiator.rkt`
2. Ensure all visible tests pass
3. Push your code before the deadline
4. Hidden tests will evaluate your trigonometric implementations

## Grading

| Component | Weight |
|-----------|--------|
| Basic derivatives | 25% |
| Advanced functions + chain rule | 35% |
| Simplification | 25% |
| Code quality and documentation | 15% |

---

**Note:** Your implementation will be tested against hidden tests that specifically check your required trigonometric functions. Make sure to implement all functions listed in your variant configuration.
