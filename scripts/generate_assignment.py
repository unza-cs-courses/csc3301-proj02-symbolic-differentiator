#!/usr/bin/env python3
"""
Generate personalized ASSIGNMENT.md from template.
CSC3301 Programming Language Paradigms - Project 2: Symbolic Differentiator
"""
import json
from pathlib import Path


def main():
    repo_root = Path(__file__).parent.parent

    # Load variant config
    config_path = repo_root / ".variant_config.json"
    if not config_path.exists():
        print("No variant config found. Run variant_generator.py first.")
        return

    with open(config_path) as f:
        variant = json.load(f)

    # Load template
    template_path = repo_root / "ASSIGNMENT_TEMPLATE.md"
    if not template_path.exists():
        print("No assignment template found.")
        return

    template = template_path.read_text()

    # Extract variant data
    trig_funcs = variant["trigonometric_functions"]["required"]
    derivative_rules = variant["trigonometric_functions"]["derivative_rules"]
    test_expressions = variant["test_expressions"]

    # Format trigonometric functions list
    trig_list = "\n".join([f"- **{func}** (derivative of {func})" for func in trig_funcs])

    # Format derivative rules
    rules_text = "\n".join([f"- `{rule}`" for rule in derivative_rules.values()])

    # Format test expressions
    expr_list = []
    for expr in test_expressions:
        expr_list.append(f"- `{expr['expr']}` ({expr['description']}) - Type: {expr['type']}")
    test_expr_text = "\n".join(expr_list)

    # Replace placeholders
    assignment = template
    assignment = assignment.replace("{{STUDENT_ID}}", variant["student_id"])
    assignment = assignment.replace("{{TRIG_FUNCTIONS_LIST}}", trig_list)
    assignment = assignment.replace("{{DERIVATIVE_RULES}}", rules_text)
    assignment = assignment.replace("{{TEST_EXPRESSIONS}}", test_expr_text)

    # Write personalized assignment
    output_path = repo_root / "ASSIGNMENT.md"
    output_path.write_text(assignment)
    print(f"Generated personalized assignment: {output_path}")

    # Display summary
    print(f"\nAssignment generated for: {variant['student_id']}")
    print(f"Required trig functions: {', '.join(trig_funcs)}")
    print(f"Number of test expressions: {len(test_expressions)}")


if __name__ == "__main__":
    main()
