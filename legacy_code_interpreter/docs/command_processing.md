
### `docs/command_processing.md`

```markdown
# Command Processing Module

## Location

`src/server.c` and related command-processing code.

## Purpose

Command processing takes parsed client input and determines whether and how the requested Redis command should execute.

## Main Responsibilities

- Find the requested command.
- Validate command arguments.
- Check client and server state.
- Apply relevant access-control checks.
- Dispatch the command implementation.
- Coordinate execution with other Redis subsystems.

## Important Pattern

This is orchestration code. It connects several subsystems rather than implementing one isolated algorithm.

## Risks

- High control-flow complexity.
- Changes can affect authentication, replication, persistence, and responses.
- Error paths can be difficult to reason about.

## Modernization Opportunities

- Extract independent validation steps.
- Add focused tests for command errors and state-dependent behavior.
- Document important client-state transitions.
- Prefer small refactorings over large rewrites.