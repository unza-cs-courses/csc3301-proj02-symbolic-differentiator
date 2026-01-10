#lang racket
(provide deriv simplify)

;;; Expression predicates
(define (variable? e) (symbol? e))
(define (same-variable? v1 v2) (and (variable? v1) (variable? v2) (eq? v1 v2)))
(define (sum? e) (and (pair? e) (eq? (car e) '+)))
(define (product? e) (and (pair? e) (eq? (car e) '*)))
(define (power? e) (and (pair? e) (eq? (car e) '^)))

;;; Selectors
(define (addend e) (cadr e))
(define (augend e) (caddr e))
(define (multiplier e) (cadr e))
(define (multiplicand e) (caddr e))

;;; Constructors with simplification - YOUR CODE HERE
(define (make-sum a1 a2)
  ; Simplify: 0+x=x, x+0=x, num+num=sum
  (list '+ a1 a2)) ; Replace with simplifying version

(define (make-product m1 m2)
  ; Simplify: 0*x=0, 1*x=x, num*num=product
  (list '* m1 m2)) ; Replace with simplifying version

;;; Main differentiation function - YOUR CODE HERE
(define (deriv expr var)
  (cond
    [(number? expr) 0]
    [(variable? expr) (if (same-variable? expr var) 1 0)]
    [(sum? expr) 
     ; d/dx[u + v] = du/dx + dv/dx
     'TODO]
    [(product? expr)
     ; d/dx[u * v] = u'v + uv' (product rule)
     'TODO]
    [(power? expr)
     ; d/dx[u^n] = n * u^(n-1) * u' (chain rule)
     'TODO]
    [else (error "Unknown expression type" expr)]))

(define (simplify expr)
  ; Additional simplification pass
  expr)

;;; Tests
(module+ test
  (require rackunit)
  (check-equal? (deriv 5 'x) 0)
  (check-equal? (deriv 'x 'x) 1)
  (check-equal? (deriv 'y 'x) 0))
