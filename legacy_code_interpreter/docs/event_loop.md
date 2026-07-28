# Event Loop Module

## Location

`src/ae.c` and related event-loop files.

## Purpose

Redis uses an event-driven architecture to process network activity and scheduled work without creating one dedicated thread for every client.

## How It Works

The event loop:

1. Checks registered file/socket events.
2. Waits for operating-system notifications.
3. Executes callbacks for ready events.
4. Processes scheduled time events.
5. Repeats continuously while the server is running.

## Important Pattern

The module uses an event loop with callbacks. Network activity and timers are converted into events that trigger specific handlers.

## Risks

- A long-running callback can delay other clients.
- Platform-specific event mechanisms increase complexity.
- Timing-sensitive behavior can be difficult to test.

## Modernization Opportunities

- Add event-loop latency metrics.
- Keep OS-specific code behind a stable abstraction.
- Add regression tests for readable, writable, timeout, and empty-event scenarios.