# GRE Crawler

This Python script automates the search process for GRE exercises. Given a set of GRE exercises, it extracts the main question text (stem) from each exercise, searches for it online, and retrieves relevant links from the GRE KMF website.

## How It Works

The GRE Crawler script performs the following steps:
1. **Text Extraction**: Reads multiple GRE questions from a text file (`gre_text.txt`).
2. **Text Cleaning**: Cleans each question by removing placeholders, extra spaces, and unwanted characters.
3. **Parsing and Searching**: Extracts the core text of each question and automates a Google search query for each one, limited to the `gre.kmf.com` website.
4. **Link Output**: Outputs the links in the terminal and saves them to a file (`gre_links.txt`) for easy reference.

## Requirements

This script requires the following Python libraries:
- `re`: for regular expression handling.
- `requests`: to handle HTTP requests.
- `BeautifulSoup` from `bs4`: for parsing the HTML responses from Google search results.
- `urllib.parse`: for encoding the query into a URL-friendly format.

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone or download this repository.

   ```bash
   git clone https://github.com/DroitXenon/gre-crawler.git
   cd gre-crawler
   ```

2. Add your GRE questions to a text file named `gre_text.txt` in the repository directory. Ensure each question is formatted as follows:
   ```
   10-3: Question text goes here...
   A:option1 B:option2 C:option3 D:option4 E:option5
   ```

   **Note:** Each question ID (like `10-3`) should start a new question, followed by the question text and options.

3. Run the script:

   ```bash
   python gre_crawler.py
   ```

4. After running, the script will output the relevant links for each question in the terminal and save them to `gre_links.txt` for reference.
