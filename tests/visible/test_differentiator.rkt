#lang racket
;;; Visible Tests for Symbolic Differentiator
;;; Generated for variant: differentiator
;;;
;;; Required trigonometric functions: cos, sin, tan

(require rackunit)
(require "../src/differentiator.rkt")

;;; Basic derivative tests
(define basic-tests
  (test-suite
   "Basic Derivatives"

   (test-case "Constant derivative"
     (check-equal? (deriv 5 'x) 0 "d/dx[5] = 0"))

   (test-case "Variable derivative - same variable"
     (check-equal? (deriv 'x 'x) 1 "d/dx[x] = 1"))

   (test-case "Variable derivative - different variable"
     (check-equal? (deriv 'y 'x) 0 "d/dx[y] = 0"))))

;;; Sum rule tests
(define sum-tests
  (test-suite
   "Sum Rule"

   (test-case "Simple sum"
     (check-not-false (deriv '(+ x 3) 'x) "d/dx[x + 3] should return a result"))))

;;; Product rule tests
(define product-tests
  (test-suite
   "Product Rule"

   (test-case "Simple product"
     (check-not-false (deriv '(* 2 x) 'x) "d/dx[2x] should return a result"))))

;;; Power rule tests
(define power-tests
  (test-suite
   "Power Rule"

   (test-case "Power function"
     (check-not-false (deriv '(^ x 2) 'x)
                      "d/dx[x^2] should return a result"))))

;;; Run all visible tests
(module+ test
  (require rackunit/text-ui)
  (run-tests basic-tests)
  (run-tests sum-tests)
  (run-tests product-tests)
  (run-tests power-tests))

;;; Direct test execution
(module+ main
  (require rackunit/text-ui)
  (displayln "Running Visible Tests for Symbolic Differentiator")
  (displayln "================================================")
  (run-tests basic-tests)
  (run-tests sum-tests)
  (run-tests product-tests)
  (run-tests power-tests))
