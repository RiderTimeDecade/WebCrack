import os
from typing import List

def read_urls_from_file(filename: str = 'url.txt') -> List[str]:
    """Read and filter URLs from the specified file."""
    urls = []
    if not os.path.exists(filename):
        print(f"{filename} not exist!")
        return urls
        
    print(f"{filename} exists!\n")
    with open(filename, 'r', encoding="UTF-8") as url_file:
        for url in url_file.readlines():
            url = url.strip()
            if url.startswith('#') or url == '' or ('.edu.cn' in url) or ('.gov.cn' in url):
                continue
            urls.append(url)
    return urls