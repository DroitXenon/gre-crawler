import re
import requests
from bs4 import BeautifulSoup
import urllib.parse

def clean_exercise_text(text):
    # Remove placeholders like (1)______
    text = re.sub(r"\(\d+\)______", "", text)
    # Split lines and keep only the stem line (the first line after the number)
    lines = text.strip().split("\n")
    if len(lines) > 0:
        stem = lines[0].strip()
    else:
        stem = ""
    return stem

# Function to parse exercises and extract only the search term line
def parse_exercises(text):
    # Updated pattern to handle multi-line exercises
    pattern = r'(\d{2}-\d{1,2})[:：](.+?)(?=(?:\d{2}-\d{1,2})[:：]|$)'
    matches = re.findall(pattern, text, re.DOTALL)
    exercises = []
    
    for match in matches:
        exercise_id = match[0]
        exercise_text = clean_exercise_text(match[1].strip())
        exercises.append((exercise_id, exercise_text))
    
    return exercises

def search_gre_kmf(exercise_id, stem):
    query = urllib.parse.quote(stem)
    url = f"https://www.google.com/search?q=site:gre.kmf.com+{query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    for result in soup.find_all('a', href=True):
        link = result['href']
        if 'gre.kmf.com/explain' in link:
            # Extract only the actual link
            actual_link = link.split('&')[0].replace('/url?q=', '')
            return f"{exercise_id}: {actual_link}"
    
    return f"{exercise_id}: No link found"

def main():
    # Read GRE exercise text from gre_text.txt
    try:
        with open("gre_text.txt", "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: 'gre_text.txt' not found. Please ensure the file is in the same directory as this script.")
        return
    
    exercises = parse_exercises(text)
    results = []
    
    for exercise_id, stem in exercises:
        link = search_gre_kmf(exercise_id, stem)
        results.append(link)
        print(link)  # Output each result as it’s found
    
    with open("gre_links.txt", "w") as file:
        for result in results:
            file.write(result + "\n")

if __name__ == "__main__":
    main()
