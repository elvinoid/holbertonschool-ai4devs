# Dictionary and Rehashing Module

## Location

`src/dict.c` and related dictionary files.

## Purpose

Redis dictionaries provide hash-table-based storage for fast key and metadata lookup.

## Rehashing

When a dictionary needs to grow, Redis can maintain an old and a new hash table temporarily. Entries are moved incrementally instead of moving everything in one large blocking operation.

```text
Old Hash Table  --->  New Hash Table
       |                    ^
       +-- incremental -----+
             migration