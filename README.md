# Project 2: Symbolic Differentiator

**CSC3301 Programming Language Paradigms**  
**Weight:** 5.5% | **Language:** Scheme (Racket)

## Overview
Implement a symbolic differentiation system in Scheme that computes derivatives of mathematical expressions symbolically (not numerically) and simplifies the results.

## Requirements
1. Differentiate polynomials, sums, products, quotients
2. Handle exponentials (e^x) and logarithms
3. Differentiate trigonometric functions from your variant
4. Apply chain rule for composite functions
5. Simplify results

## Milestones
| M1 | Basic derivatives | 25% |
| M2 | Advanced functions + chain rule | 35% |
| M3 | Simplification | 25% |
| Final | Complete with tests | 15% |

## Expression Representation
```scheme
'(+ x 3)           ; x + 3
'(* 2 x)           ; 2 * x
'(^ x 3)           ; x^3
'(sin (* 2 x))     ; sin(2x)
```

## Example
```scheme
(deriv '(^ x 3) 'x)  ; Returns '(* 3 (^ x 2))
```
