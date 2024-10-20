## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of _Refactoring: Improving the Design of Existing Code_ by Martin Fowler.

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.

## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for a description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Refactoring: Move price_code Attribute

### Justification for Refactoring

In the previous implementation, the `price_code` attribute was part of the `Movie` class, but it was only being used by the `Rental` class. Moving the `price_code` to the `Rental` class simplifies the design and adheres to the principles of object-oriented programming. This change enhances cohesion by ensuring that attributes and methods related to rental pricing are encapsulated within the class that directly manages rentals.

### 2.1 Code Smells Indicating This Refactoring

Several code smells suggest the need for this refactoring:

1. **Middle Man**: The `Movie` class was acting as a middleman, delegating calls to pricing methods that were only relevant to rentals. This unnecessary delegation complicates the code and introduces additional layers of interaction that can be avoided.

2. **Violation of Single Responsibility Principle (SRP)**: The `Movie` class was responsible for both movie attributes and pricing logic. By moving the `price_code` to `Rental`, we ensure that each class has a single responsibility, making the code easier to understand and maintain.

3. **Low Cohesion**: The presence of pricing logic in the `Movie` class diluted its focus on movie-related attributes. By consolidating all pricing logic within `Rental`, we achieve higher cohesion, where related functionalities are grouped together.

### 2.2 Design Principle Suggesting This Refactoring

The primary design principle that suggests this refactoring is the **Single Responsibility Principle (SRP)**. According to SRP, a class should have only one reason to change, meaning it should encapsulate only one responsibility.

In our case:
- The `Movie` class was handling movie-related attributes and pricing strategies, which are conceptually different responsibilities.
- By moving the `price_code` attribute and its associated methods to the `Rental` class, we align each class with its core responsibility—`Movie` for movie details and `Rental` for rental transactions.

This refactoring leads to cleaner, more maintainable code and reduces potential sources of bugs by ensuring that changes related to pricing only affect the `Rental` class.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.