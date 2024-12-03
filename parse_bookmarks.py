import pandas as pd
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
from datetime import datetime

def extract_main_domain(url):
    try:
        parsed = urlparse(url)
        # Get domain without subdomain
        domain_parts = parsed.netloc.split('.')
        if len(domain_parts) > 2:
            return '.'.join(domain_parts[-2:])
        return parsed.netloc
    except:
        return url

def calculate_relative_age(timestamp):
    if not timestamp:
        return None
    
    now = datetime.now()
    date = pd.to_datetime(int(timestamp), unit='s')
    diff = now - date
    
    days = diff.days
    if days < 1:
        hours = diff.seconds // 3600
        return f"{hours} hours ago"
    elif days < 7:
        return f"{days} days ago"
    elif days < 30:
        weeks = days // 7
        return f"{weeks} weeks ago"
    elif days < 365:
        months = days // 30
        return f"{months} months ago"
    else:
        years = days // 365
        return f"{years} years ago"

def parse_bookmarks(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    data = []
    
    # Find the 2024 folder
    folder_2024 = soup.find('h3', string="2024")
    if folder_2024:
        # Get the next DL element which contains the bookmarks
        bookmarks_dl = folder_2024.find_next_sibling('dl')
        if bookmarks_dl:
            # Find all bookmarks in this folder
            for bookmark in bookmarks_dl.find_all('a'):
                try:
                    title = bookmark.text
                    url = bookmark.get('href')
                    date_added = bookmark.get('add_date')
                    
                    if url and not url.startswith('javascript:'):
                        try:
                            date_obj = pd.to_datetime(int(date_added), unit='s') if date_added else None
                            
                            data.append({
                                'title': title,
                                'link': url,
                                'site': extract_main_domain(url),
                                'date': date_obj.strftime('%Y-%m-%d') if date_obj else None,
                                'age': calculate_relative_age(date_added) if date_added else None
                            })
                        except (ValueError, TypeError):
                            continue
                except Exception:
                    continue

    df = pd.DataFrame(data)
    if 'date' in df.columns:
        df = df.sort_values('date', ascending=False)
    
    return df

def main():
    # File path
    file_path = 'bookmarks_12_3_24.html'

    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    # Parse bookmarks and create DataFrame
    df = parse_bookmarks(file_path)

    # Save to CSV
    output_file = "bookmarks_export.csv"
    df.to_csv(output_file, index=False)
    print(f"\nData exported to: {os.path.abspath(output_file)}")

if __name__ == '__main__':
    main() 