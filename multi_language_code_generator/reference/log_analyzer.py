class LogAnalyzer:
    """Analyze application logs."""

    VALID_LEVELS = {
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    }

    def parse_line(self, line: str) -> dict:
        """Parse one log line.

        Expected format:
        YYYY-MM-DD HH:MM:SS | LEVEL | SOURCE | MESSAGE
        """
        parts = [part.strip() for part in line.split("|", 3)]

        if len(parts) != 4:
            raise ValueError("Malformed log entry")

        timestamp, level, source, message = parts

        if not timestamp:
            raise ValueError("Missing timestamp")

        if level not in self.VALID_LEVELS:
            raise ValueError("Unknown log level")

        if not source:
            raise ValueError("Missing source")

        return {
            "timestamp": timestamp,
            "level": level,
            "source": source,
            "message": message,
        }

    def analyze(
        self,
        logs: list[str],
        keywords: list[str] | None = None,
        threshold: int = 2,
    ) -> dict:
        """Analyze valid log entries."""
        if keywords is None:
            keywords = []

        if threshold < 1:
            raise ValueError("Threshold must be at least 1")

        level_counts = {}
        keyword_matches = {
            keyword.lower(): 0
            for keyword in keywords
            if keyword.strip()
        }
        source_counts = {}
        total_entries = 0

        for line in logs:
            try:
                entry = self.parse_line(line)
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