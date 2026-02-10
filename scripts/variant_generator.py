#!/usr/bin/env python3
"""
Variant Generator for Project 2: Symbolic Differentiator
CSC3301 Programming Language Paradigms

Generates unique test parameters based on student ID.
Each student gets deterministic but unique values for testing.

This variant system assigns different trigonometric functions
and test expressions to each student.
"""
import hashlib
import json
import sys
import random
from pathlib import Path


# All available trigonometric functions with their derivatives
TRIG_FUNCTIONS = {
    'sin': {'derivative': 'cos', 'description': 'sine'},
    'cos': {'derivative': '(lambda (x) (- (sin x)))', 'description': 'cosine'},
    'tan': {'derivative': 'sec^2', 'description': 'tangent'},
    'sec': {'derivative': '(lambda (x) (* (sec x) (tan x)))', 'description': 'secant'},
    'csc': {'derivative': '(lambda (x) (- (* (csc x) (cot x))))', 'description': 'cosecant'},
    'cot': {'derivative': '(lambda (x) (- (csc^2 x)))', 'description': 'cotangent'}
}

# Derivative rules in Racket/Scheme notation
DERIVATIVE_RULES = {
    'sin': "d/dx[sin(u)] = cos(u) * u'",
    'cos': "d/dx[cos(u)] = -sin(u) * u'",
    'tan': "d/dx[tan(u)] = sec^2(u) * u'",
    'sec': "d/dx[sec(u)] = sec(u) * tan(u) * u'",
    'csc': "d/dx[csc(u)] = -csc(u) * cot(u) * u'",
    'cot': "d/dx[cot(u)] = -csc^2(u) * u'"
}


def generate_variant(student_id: str) -> dict:
    """
    Generate a unique variant configuration based on student ID.

    Uses deterministic hashing so the same student ID always
    produces the same variant.
    """
    # Create deterministic seed from student ID
    seed = int(hashlib.sha256(student_id.encode()).hexdigest(), 16) % (2**32)
    rng = random.Random(seed)

    # Select 3-4 trigonometric functions for this student
    all_trig = list(TRIG_FUNCTIONS.keys())
    rng.shuffle(all_trig)
    num_trig = rng.randint(3, 4)
    selected_trig = sorted(all_trig[:num_trig])  # Sort for consistency

    # Generate test polynomial coefficients
    poly_coeffs = [rng.randint(1, 10) for _ in range(3)]

    # Generate power test values
    power_base = rng.choice([2, 3, 4, 5])
    power_exp = rng.choice([2, 3, 4])

    # Generate test expressions based on selected trig functions
    test_expressions = []

    # Basic polynomial test
    test_expressions.append({
        'expr': f"'(+ (* {poly_coeffs[0]} (^ x 2)) (* {poly_coeffs[1]} x) {poly_coeffs[2]})",
        'description': f"{poly_coeffs[0]}x^2 + {poly_coeffs[1]}x + {poly_coeffs[2]}",
        'type': 'polynomial'
    })

    # Power rule test
    test_expressions.append({
        'expr': f"'(^ x {power_exp})",
        'description': f"x^{power_exp}",
        'type': 'power'
    })

    # Product rule test
    prod_coeff = rng.randint(2, 5)
    test_expressions.append({
        'expr': f"'(* {prod_coeff} (^ x 2))",
        'description': f"{prod_coeff} * x^2",
        'type': 'product'
    })

    # Add trig function tests based on selected functions
    for trig_func in selected_trig[:2]:  # Test first 2 selected trig functions
        test_expressions.append({
            'expr': f"'({trig_func} x)",
            'description': f"{trig_func}(x)",
            'type': 'trigonometric'
        })

    # Chain rule with trig test
    chain_trig = rng.choice(selected_trig)
    chain_coeff = rng.randint(2, 4)
    test_expressions.append({
        'expr': f"'({chain_trig} (* {chain_coeff} x))",
        'description': f"{chain_trig}({chain_coeff}x)",
        'type': 'chain_rule'
    })

    # Generate expected derivative format hints
    derivative_hints = {}
    for trig in selected_trig:
        derivative_hints[trig] = DERIVATIVE_RULES[trig]

    variant = {
        "student_id": student_id,
        "variant_seed": seed,
        "trigonometric_functions": {
            "required": selected_trig,
            "count": len(selected_trig),
            "derivative_rules": derivative_hints
        },
        "test_parameters": {
            "polynomial_coefficients": poly_coeffs,
            "power_base": power_base,
            "power_exponent": power_exp
        },
        "test_expressions": test_expressions,
        "simplification_requirements": {
            "zero_elimination": True,  # 0 + x = x, 0 * x = 0
            "identity_simplification": True,  # 1 * x = x
            "constant_folding": True  # 2 + 3 = 5
        }
    }

    return variant


def generate_test_file(variant: dict, repo_root: Path):
    """
    Generate a Racket test file based on the variant configuration.
    """
    trig_funcs = variant["trigonometric_functions"]["required"]
    test_exprs = variant["test_expressions"]

    test_content = f'''#lang racket
;;; Visible Tests for Symbolic Differentiator
;;; Generated for variant: {variant["student_id"]}
;;;
;;; Required trigonometric functions: {", ".join(trig_funcs)}

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
     (check-not-false (deriv '(^ x {variant["test_parameters"]["power_exponent"]}) 'x)
                      "d/dx[x^{variant["test_parameters"]["power_exponent"]}] should return a result"))))

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
'''

    # Ensure tests/visible directory exists
    visible_tests_dir = repo_root / "tests" / "visible"
    visible_tests_dir.mkdir(parents=True, exist_ok=True)

    test_file_path = visible_tests_dir / "test_differentiator.rkt"
    test_file_path.write_text(test_content)
    print(f"Generated test file: {test_file_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python variant_generator.py <student_id>")
        print("Example: python variant_generator.py john_doe")
        sys.exit(1)

    student_id = sys.argv[1]
    repo_root = Path(__file__).parent.parent

    print(f"Generating variant for student: {student_id}")

    # Generate variant
    variant = generate_variant(student_id)

    # Save variant config
    config_path = repo_root / ".variant_config.json"
    with open(config_path, 'w') as f:
        json.dump(variant, f, indent=2)
    print(f"Saved variant config to {config_path}")

    # Generate test file
    generate_test_file(variant, repo_root)

    # Display summary
    print("\n=== Variant Summary ===")
    print(f"Student ID: {variant['student_id']}")
    print(f"Seed: {variant['variant_seed']}")
    print(f"Required trig functions: {', '.join(variant['trigonometric_functions']['required'])}")
    print(f"Number of test expressions: {len(variant['test_expressions'])}")
    print("\nDerivative rules to implement:")
    for trig, rule in variant['trigonometric_functions']['derivative_rules'].items():
        print(f"  {rule}")


if __name__ == "__main__":
    main()
