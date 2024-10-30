Feature: Basic Calculator Operations
    As a user
    I want to perform basic arithmetic operations
    So that I can calculate results quickly

Scenario: Add two numbers
    Given the Flask calculator is running
    When I add 2 and 3
    Then the result should be 5

Scenario: Subtract two numbers
    Given the Flask calculator is running
    When I subtract 5 from 8
    Then the result should be 3


Scenario: Divide by zero
    Given the Flask calculator is running
    When I divide 10 by 0
    Then the result should be "Error: Division by zero"
