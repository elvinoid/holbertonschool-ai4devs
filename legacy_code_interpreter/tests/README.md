
---

# Tests

### `tests/README.md`

```markdown
# Redis Behavior Tests

These are lightweight, runnable pytest tests covering behaviors discussed in the
legacy-code analysis. They do not require a Redis server because they use small
models of protocol parsing, command lookup, input buffering, and rehashing.

Run:

```bash
python -m pytest tests/