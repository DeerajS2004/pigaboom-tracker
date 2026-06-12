# Pigaboom Tracker

A GitHub Actions based data collector for Pigaboom crash game multipliers.

The workflow launches a headless Chromium browser using Playwright, opens the game page, extracts the latest 45 visible multiplier results, and appends them to a timestamped text file.

## Features

* Fully automated using GitHub Actions
* No local computer required after setup
* Stores snapshots with timestamps
* Simple TXT output format
* Easy to analyze later using Python, Excel, R, or custom scripts
* Collects the latest 45 visible results every scheduled run

## Repository Structure

```text
pigaboom-tracker/
│
├── collect.py
├── requirements.txt
├── data.txt
│
└── .github/
    └── workflows/
        └── collect.yml
```

## Data Format

Each snapshot is appended to `data.txt`:

```text
============================================================
2026-06-12 12:00:00 UTC
============================================================

13.81x
2.44x
1.03x
7.55x
...
```

## Requirements

* GitHub Account
* GitHub Actions enabled
* Playwright

## Workflow Schedule

Current schedule:

```yaml
schedule:
  - cron: "*/9 * * * *"
```

This runs approximately every 9 minutes.

## How It Works

1. GitHub Actions starts.
2. Chromium launches in headless mode.
3. Pigaboom page loads.
4. Latest 45 multipliers are extracted.
5. Snapshot is appended to `data.txt`.
6. Changes are committed back to the repository.

## Output

All collected snapshots are stored in:

```text
data.txt
```

Each entry contains:

* UTC timestamp
* 45 visible multipliers at the time of collection

## Notes

* GitHub scheduled workflows are not guaranteed to run exactly on schedule.
* Delays of a few minutes may occur.
* If the game session token expires, the collector may require updates.
* Historical data is preserved because snapshots are appended instead of overwritten.

## Disclaimer

This project is intended for educational, statistical, and data-analysis purposes only. Users are responsible for complying with the terms of service of any website they access.
