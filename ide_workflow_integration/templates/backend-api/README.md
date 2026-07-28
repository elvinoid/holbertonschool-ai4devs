# Backend API Template with AI Support

## Overview

A reusable backend API project template configured for AI-assisted development in Visual Studio Code.

This template is designed for building REST APIs with Node.js and Express.js while using GitHub Copilot to improve development productivity.

## Features

- Node.js backend structure
- Express.js REST API support
- GitHub Copilot support
- AI-assisted code generation
- AI code review workflow
- AI documentation generation workflow
- ESLint recommendations
- Prettier formatting
- Input validation
- Error handling
- Security and performance considerations

## AI Configuration

The `.copilot-settings.yaml` file contains recommended AI coding rules for JavaScript and Express.js development.

The configuration includes:

- Modern JavaScript syntax
- `const` and `let` usage
- ESLint-compatible code
- Prettier formatting
- Input validation
- Explicit error handling
- REST API best practices
- Security considerations
- Performance considerations

## Automation

The `automation/tasks.json` file provides AI-assisted workflows for:

### AI Code Review

Reviews backend code for:

- Security issues
- Input validation
- Error handling
- Performance
- Maintainability

### AI API Documentation

Generates API documentation including:

- API endpoints
- HTTP methods
- Request parameters
- Request bodies
- Responses
- Error responses

## Recommended VS Code Extensions

- GitHub Copilot
- GitHub Copilot Chat
- ESLint
- Prettier - Code formatter

## Setup

Install Node.js 18 or later.

Install project dependencies:

```bash
npm install