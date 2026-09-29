# Project Statement

## Problem Statement
First-year engineering students, particularly those balancing rigorous coursework in fields like Artificial Intelligence and Machine Learning, frequently struggle to maintain consistency across coding practice, assignments, and self-study. Existing productivity tools are often overly complex, bloated with unnecessary features, or require constant internet connectivity. There is a clear need for a fast, distraction-free, terminal-based tool that allows students to quickly log tasks and track study sessions directly from their coding environment.

## Scope of the Project
This project provides a localized, dependency-free command-line application. It is intentionally scoped to focus on two core pillars: task lifecycle management (creation, viewing, and completion) and study habit tracking (logging focused hours). The system utilizes local file storage to ensure data persistence across sessions, functioning entirely offline without the need for external databases or APIs.

## Target Users
- Undergraduate engineering students managing multiple course deadlines.
- Programmers and developers who prefer terminal-based utilities over web applications.
- Anyone looking for a minimalist, offline habit and task tracker.

## High-Level Features
1. **Interactive CLI Navigation:** A loop-driven main menu with screen-clearing utility for a clean user experience.
2. **Task Categorization & Prioritization:** Ability to assign deadlines, categories, and priority levels to academic tasks.
3. **Quantitative Study Logging:** An array-based tracking system for logging floating-point study hours.
4. **Automated Analytics:** Mathematical computation of task completion rates and study session averages.
5. **Robust Error Handling:** Continuous input validation to prevent crashes from invalid user entries.