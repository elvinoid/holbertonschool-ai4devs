# Redis Behavior Tests

This directory contains AI-assisted unit tests for behaviors identified during
the legacy Redis codebase analysis.

## Test Modules

- `test_resp_parser.py` - RESP protocol parsing
- `test_command_lookup.py` - Redis command lookup
- `test_rehashing.py` - Incremental hash-table rehashing
- `test_input_buffer.py` - Input-buffer processing
- `test_response.py` - RESP bulk-string responses

## Running Tests

Install pytest if necessary:

```bash
pip install pytest