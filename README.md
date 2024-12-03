# Chrome Bookmark Exporter

A Python script that extracts bookmarks from Chrome/Firefox HTML exports, specifically focusing on links saved in the "2024" folder. The script processes the bookmarks and exports them to a CSV file with useful metadata.

## Features

- Extracts bookmarks from Chrome/Firefox HTML exports
- Focuses on links within the "2024" folder
- Calculates relative ages (e.g., "2 months ago")
- Extracts main domain names from URLs
- Sorts by date (newest first)
- Exports to CSV format

## Requirements

- Python 3.x
- pandas
- beautifulsoup4

## Usage

1. Export your bookmarks from Chrome/Firefox to an HTML file
2. Name the file `bookmarks_12_3_24.html` (or update the filename in the script)
3. Run:

```bash
python parse_bookmarks.py
```

## Output Format

The script generates a `bookmarks_export.csv` with the following columns:
- title: The bookmark title
- link: Full URL
- site: Main domain name
- date: Date added (YYYY-MM-DD)
- age: Relative time since adding (e.g., "2 months ago")

## How It Works

1. Parses the HTML bookmarks file using BeautifulSoup
2. Locates the "2024" folder
3. Extracts bookmark metadata including dates and URLs
4. Processes timestamps into human-readable formats
5. Exports the data to CSV

## Example Output

```cs
title,link,site,date,age
"Example Article",https://example.com/article,example.com,2024-03-01,2 months ago
```


## License

MIT