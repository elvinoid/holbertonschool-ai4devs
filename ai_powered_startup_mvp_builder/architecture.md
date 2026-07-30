# System Architecture - AI Code Modernization Assistant

## Overview

The system uses a simple web application architecture.

```text
+------------------+
|      User        |
+--------+---------+
         |
         v
+------------------+
|   Web Interface  |
+--------+---------+
         |
         v
+------------------+
|    Backend API   |
+--------+---------+
         |
    +----+----+
    |         |
    v         v
+--------+  +-------------+
| AI     |  | Database    |
| Service|  |             |
+--------+  +-------------+
    |
    v
+------------------+
| Code Analysis    |
| & Recommendations|
+------------------+