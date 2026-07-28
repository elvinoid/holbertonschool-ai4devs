# AI Configuration

## AI Assistant

- **IDE:** Visual Studio Code
- **AI Assistant:** GitHub Copilot
- **Primary Languages:** JavaScript, Python, YAML, Markdown
- **Version Control:** Git and GitHub

## Copilot Usage

GitHub Copilot is configured to assist with code generation, refactoring, debugging, documentation, and code review.

AI-generated code is always reviewed and tested before being committed to the repository.

## Language-Specific Rules

### JavaScript

- Follow modern JavaScript practices.
- Use clear and descriptive variable names.
- Use `const` by default and `let` when reassignment is required.
- Use semicolons.
- Validate API input.
- Handle errors explicitly.
- Follow REST API conventions.
- Avoid unnecessary dependencies.

### Python

- Follow PEP 8 style guidelines.
- Use type hints where practical.
- Use descriptive function and variable names.
- Handle exceptions explicitly.
- Keep functions focused and maintainable.

### YAML

- Use 2-space indentation.
- Keep keys consistent and descriptive.
- Validate YAML syntax before committing.
- Follow OpenAPI 3.x conventions when documenting APIs.

### Markdown

- Use clear headings.
- Keep documentation concise and structured.
- Include code examples where useful.

## Specialized AI Workflows

### Code Review

GitHub Copilot is used to review code before committing.

Review focus areas:

- Security vulnerabilities
- Input validation
- Error handling
- Performance
- Code quality
- Maintainability
- REST API best practices

### Documentation Generator

Copilot can be used to generate and update:

- README files
- API documentation
- Code comments
- OpenAPI descriptions
- Setup instructions

## AI Review Workflow

1. Implement the feature.
2. Ask Copilot to review the implementation.
3. Check security and error handling.
4. Review the generated suggestions manually.
5. Apply appropriate improvements.
6. Run tests.
7. Commit the final reviewed implementation.

## Example Prompts

### Code Review

> Review this code for security vulnerabilities, input validation problems, error handling issues, and performance problems. Suggest specific improvements.

### Documentation

> Generate concise Markdown documentation for this API endpoint, including its purpose, parameters, request body, response, and possible errors.

### Refactoring

> Refactor this code to improve readability and maintainability while preserving its existing behavior.