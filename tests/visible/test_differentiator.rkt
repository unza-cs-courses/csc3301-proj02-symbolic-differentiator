#lang racket
;;; Visible Tests for Symbolic Differentiator
;;; Generated for variant: differentiator
;;;
;;; Required trigonometric functions: cos, sin, tan

(require rackunit)
(require "../../src/differentiator.rkt")

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

;;; Sum rule tests — assert actual derivative values
(define sum-tests
  (test-suite
   "Sum Rule"

   (test-case "Simple sum d/dx[x + 3] = 1"
     (let ([result (deriv '(+ x 3) 'x)])
       ;; d/dx[x+3] = 1+0 = 1  (may be simplified or unsimplified)
       (check-true (or (equal? result 1)
                       (equal? result '(+ 1 0)))
                   "d/dx[x + 3] should be 1 or (+ 1 0)")))))

;;; Product rule tests — assert actual derivative values
(define product-tests
  (test-suite
   "Product Rule"

   (test-case "Simple product d/dx[2x] = 2"
     (let ([result (deriv '(* 2 x) 'x)])
       ;; d/dx[2*x] = 2*1 + x*0 = 2 (may be simplified or unsimplified)
       (check-true (or (equal? result 2)
                       (equal? result '(+ (* 2 1) (* 0 x)))
                       (equal? result '(+ (* 0 x) (* 2 1))))
                   "d/dx[2x] should be 2 or product rule expansion")))))

;;; Power rule tests — assert actual derivative values
(define power-tests
  (test-suite
   "Power Rule"

   (test-case "Power function d/dx[x^2] = 2x"
     (let ([result (deriv '(** x 2) 'x)])
       ;; d/dx[x^2] = 2*x^1 = 2x (may be simplified or unsimplified)
       (check-true (or (equal? result '(* 2 x))
                       (equal? result '(* 2 (** x 1))))
                   "d/dx[x^2] should be (* 2 x) or (* 2 (** x 1))")))))

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
