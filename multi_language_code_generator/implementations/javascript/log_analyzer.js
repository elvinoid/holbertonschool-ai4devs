const fs = require("fs");

const VALID_LEVELS = new Set([
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL"
]);

function parseLine(line) {
    const parts = line.split("|", 4).map(part => part.trim());

    if (parts.length !== 4) {
        throw new Error("Malformed log entry");
    }

    const [timestamp, level, source, message] = parts;

    if (!timestamp) {
        throw new Error("Missing timestamp");
    }

    if (!VALID_LEVELS.has(level)) {
        throw new Error("Unknown log level");
    }

    if (!source) {
        throw new Error("Missing source");
    }

    return {
        timestamp,
        level,
        source,
        message
    };
}

function analyze(logs, keywords = [], threshold = 2) {
    if (threshold < 1) {
        throw new Error("Threshold must be at least 1");
    }

    const levelCounts = {};
    const keywordMatches = {};
    const sourceCounts = {};

    for (const keyword of keywords) {
        const normalized = keyword.trim().toLowerCase();

        if (normalized) {
            keywordMatches[normalized] = 0;
        }
    }

    let totalEntries = 0;

    for (const line of logs) {
        let entry;

        try {
            entry = parseLine(line);
        } catch (error) {
            continue;
        }

        totalEntries++;

        const level = entry.level;
        levelCounts[level] = (levelCounts[level] || 0) + 1;

        const source = entry.source;
        sourceCounts[source] = (sourceCounts[source] || 0) + 1;

        const message = entry.message.toLowerCase();

        for (const keyword of Object.keys(keywordMatches)) {
            let position = 0;

            while ((position = message.indexOf(keyword, position)) !== -1) {
                keywordMatches[keyword]++;
                position += keyword.length;
            }
        }
    }

    const repeatedSources = Object.keys(sourceCounts)
        .filter(source => sourceCounts[source] >= threshold)
        .sort();

    return {
        total_entries: totalEntries,
        level_counts: levelCounts,
        keyword_matches: keywordMatches,
        repeated_sources: repeatedSources
    };
}

if (require.main === module) {
    const input = fs.readFileSync(0, "utf8");
    const data = JSON.parse(input);

    const result = analyze(
        data.logs || [],
        data.keywords || [],
        data.threshold || 2
    );

    console.log(JSON.stringify(result, null, 2));
}

module.exports = {
    parseLine,
    analyze
};