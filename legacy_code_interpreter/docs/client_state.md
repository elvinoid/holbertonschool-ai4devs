
### `docs/client_state.md`

```markdown
# Client State Module

## Purpose

Redis maintains state for each connected client, including input data, parsed command information, output data, and state related to blocking or authentication.

## Typical Lifecycle

```text
Connection
   |
   v
Read Input
   |
   v
Parse Request
   |
   v
Validate / Execute
   |
   v
Build Response
   |
   v
Write Response