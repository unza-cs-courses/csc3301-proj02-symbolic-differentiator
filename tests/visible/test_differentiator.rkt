#lang racket
;;; Visible Tests for Symbolic Differentiator
;;; CSC3301 Programming Language Paradigms - Project 2
;;;
;;; These tests verify basic differentiation functionality.
;;; Additional tests may be generated based on your variant configuration.

(require rackunit)
(require rackunit/text-ui)
(require "../../src/differentiator.rkt")

;;; ============================================================
;;; Basic Derivative Tests
;;; ============================================================
(define basic-tests
  (test-suite
   "Basic Derivatives"

   (test-case "Constant derivative is zero"
     (check-equal? (deriv 5 'x) 0
                   "d/dx[5] = 0"))

   (test-case "Constant derivative - different constant"
     (check-equal? (deriv 42 'x) 0
                   "d/dx[42] = 0"))

   (test-case "Variable derivative - same variable"
     (check-equal? (deriv 'x 'x) 1
                   "d/dx[x] = 1"))

   (test-case "Variable derivative - different variable"
     (check-equal? (deriv 'y 'x) 0
                   "d/dx[y] = 0"))

   (test-case "Variable derivative - another variable"
     (check-equal? (deriv 'z 'x) 0
                   "d/dx[z] = 0"))))

;;; ============================================================
;;; Sum Rule Tests: d/dx[u + v] = du/dx + dv/dx
;;; ============================================================
(define sum-tests
  (test-suite
   "Sum Rule"

   (test-case "Sum with constant"
     (check-not-false (deriv '(+ x 3) 'x)
                      "d/dx[x + 3] should return a result"))

   (test-case "Sum of two variables"
     (check-not-false (deriv '(+ x y) 'x)
                      "d/dx[x + y] should return a result"))

   (test-case "Sum with zero should simplify"
     (check-not-false (deriv '(+ x 0) 'x)
                      "d/dx[x + 0] should return a result"))))

;;; ============================================================
;;; Product Rule Tests: d/dx[u * v] = u'v + uv'
;;; ============================================================
(define product-tests
  (test-suite
   "Product Rule"

   (test-case "Simple product with constant"
     (check-not-false (deriv '(* 2 x) 'x)
                      "d/dx[2x] should return a result"))

   (test-case "Product of two variables"
     (check-not-false (deriv '(* x y) 'x)
                      "d/dx[xy] should return a result"))

   (test-case "Product with one"
     (check-not-false (deriv '(* 1 x) 'x)
                      "d/dx[1*x] should return a result"))))

;;; ============================================================
;;; Power Rule Tests: d/dx[x^n] = n * x^(n-1)
;;; ============================================================
(define power-tests
  (test-suite
   "Power Rule"

   (test-case "Square function"
     (check-not-false (deriv '(^ x 2) 'x)
                      "d/dx[x^2] should return a result"))

   (test-case "Cube function"
     (check-not-false (deriv '(^ x 3) 'x)
                      "d/dx[x^3] should return a result"))

   (test-case "Fourth power"
     (check-not-false (deriv '(^ x 4) 'x)
                      "d/dx[x^4] should return a result"))))

;;; ============================================================
;;; Run All Visible Tests
;;; ============================================================
(module+ test
  (run-tests basic-tests)
  (run-tests sum-tests)
  (run-tests product-tests)
  (run-tests power-tests))

(module+ main
  (displayln "")
  (displayln "==============================================")
  (displayln "  Symbolic Differentiator - Visible Tests")
  (displayln "==============================================")
  (displayln "")
  (run-tests basic-tests)
  (run-tests sum-tests)
  (run-tests product-tests)
  (run-tests power-tests)
  (displayln "")
  (displayln "Note: Hidden tests will evaluate trigonometric")
  (displayln "      functions based on your variant config."))
