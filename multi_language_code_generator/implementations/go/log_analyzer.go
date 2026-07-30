package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"sort"
	"strings"
)

var validLevels = map[string]bool{
	"DEBUG":    true,
	"INFO":     true,
	"WARNING":  true,
	"ERROR":    true,
	"CRITICAL": true,
}

type LogEntry struct {
	Timestamp string `json:"timestamp"`
	Level     string `json:"level"`
	Source    string `json:"source"`
	Message   string `json:"message"`
}

type Input struct {
	Logs      []string `json:"logs"`
	Keywords  []string `json:"keywords"`
	Threshold int      `json:"threshold"`
}

type Result struct {
	TotalEntries    int            `json:"total_entries"`
	LevelCounts     map[string]int `json:"level_counts"`
	KeywordMatches  map[string]int `json:"keyword_matches"`
	RepeatedSources []string       `json:"repeated_sources"`
}

func parseLine(line string) (LogEntry, error) {
	parts := strings.SplitN(line, "|", 4)

	if len(parts) != 4 {
		return LogEntry{}, fmt.Errorf("malformed log entry")
	}

	timestamp := strings.TrimSpace(parts[0])
	level := strings.TrimSpace(parts[1])
	source := strings.TrimSpace(parts[2])
	message := strings.TrimSpace(parts[3])

	if timestamp == "" {
		return LogEntry{}, fmt.Errorf("missing timestamp")
	}

	if !validLevels[level] {
		return LogEntry{}, fmt.Errorf("unknown log level")
	}

	if source == "" {
		return LogEntry{}, fmt.Errorf("missing source")
	}

	return LogEntry{
		Timestamp: timestamp,
		Level:     level,
		Source:    source,
		Message:   message,
	}, nil
}

func analyze(logs []string, keywords []string, threshold int) (Result, error) {
	if threshold < 1 {
		return Result{}, fmt.Errorf("threshold must be at least 1")
	}

	result := Result{
		TotalEntries:    0,
		LevelCounts:     make(map[string]int),
		KeywordMatches:  make(map[string]int),
		RepeatedSources: []string{},
	}

	for _, keyword := range keywords {
		normalized := strings.ToLower(strings.TrimSpace(keyword))

		if normalized != "" {
			result.KeywordMatches[normalized] = 0
		}
	}

	sourceCounts := make(map[string]int)

	for _, line := range logs {
		entry, err := parseLine(line)

		if err != nil {
			continue
		}

		result.TotalEntries++

		result.LevelCounts[entry.Level]++

		sourceCounts[entry.Source]++

		message := strings.ToLower(entry.Message)

		for keyword := range result.KeywordMatches {
			result.KeywordMatches[keyword] += strings.Count(
				message,
				keyword,
			)
		}
	}

	for source, count := range sourceCounts {
		if count >= threshold {
			result.RepeatedSources = append(
				result.RepeatedSources,
				source,
			)
		}
	}

	sort.Strings(result.RepeatedSources)

	return result, nil
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	var input Input

	if err := json.NewDecoder(reader).Decode(&input); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}

	if input.Threshold == 0 {
		input.Threshold = 2
	}

	result, err := analyze(
		input.Logs,
		input.Keywords,
		input.Threshold,
	)

	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}

	output, err := json.MarshalIndent(result, "", "  ")

	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}

	fmt.Println(string(output))
}