import json
import sys


VALID_LEVELS = {
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL",
}


def parse_line(line):
    parts = [part.strip() for part in line.split("|", 3)]

    if len(parts) != 4:
        raise ValueError("Malformed log entry")

    timestamp, level, source, message = parts

    if not timestamp:
        raise ValueError("Missing timestamp")

    if level not in VALID_LEVELS:
        raise ValueError("Unknown log level")

    if not source:
        raise ValueError("Missing source")

    return {
        "timestamp": timestamp,
        "level": level,
        "source": source,
        "message": message,
    }


def analyze(logs, keywords=None, threshold=2):
    if keywords is None:
        keywords = []

    if threshold < 1:
        raise ValueError("Threshold must be at least 1")

    level_counts = {}
    keyword_matches = {}
    source_counts = {}

    for keyword in keywords:
        keyword = keyword.strip().lower()
        if keyword:
            keyword_matches.setdefault(keyword, 0)

    total_entries = 0

    for line in logs:
        try:
            entry = parse_line(line)
        except ValueError:
            continue

        total_entries += 1

        level = entry["level"]
        level_counts[level] = level_counts.get(level, 0) + 1

        source = entry["source"]
        source_counts[source] = source_counts.get(source, 0) + 1

        message = entry["message"].lower()

        for keyword in keyword_matches:
            keyword_matches[keyword] += message.count(keyword)

    repeated_sources = sorted(
        source
        for source, count in source_counts.items()
        if count >= threshold
    )

    return {
        "total_entries": total_entries,
        "level_counts": level_counts,
        "keyword_matches": keyword_matches,
        "repeated_sources": repeated_sources,
    }


if __name__ == "__main__":
    data = json.load(sys.stdin)

    result = analyze(
        data.get("logs", []),
        data.get("keywords", []),
        data.get("threshold", 2),
    )

    print(json.dumps(result, indent=2))