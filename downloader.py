import os
import re
import requests

def extract_matches_from_file(pattern, filename):
    """Returns a list of reg-ex matches for the specified pattern and file."""
    with open(filename, "r") as f:
        results = set(re.findall(pattern, f.read()))
        return results

def dl_html(url, filename):
    """Saves the html source of a specified url under the given filename."""
    req = requests.get(url, 'html.parser')

    with open(filename, "w") as f:
        f.write(req.text)
        f.close()

def dl_mp4(url, filename):
    """Downloads a mp4-file"""
    print(f"Downloading {filename}...")
    r = requests.get(url, stream = True)
    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)
        f.close()


# Go through html files, find download link for videos, download videos to desired location

def main():
# Download html source for main site
    main_url = "https://www.uio.no/studier/emner/hf/ifikk/EXPHIL03/v22/canvas-media/"

    main_html_file = "html/main_site.html"
    dl_html(main_url, main_html_file)

# Parse main site for links to subsites
    subsite_pattern = "(https://www.uio.no/studier/emner/hf/ifikk/EXPHIL03/v22/canvas-media/uke-\d\d/)"
    subsite_urls = extract_matches_from_file(subsite_pattern, main_html_file)

# Download html source for subsites
    for url in subsite_urls:
        name = url[-7:-1]
        dl_html(url, f"html/{name}.html")

# Find download links in subsites and download file
    dl_pattern = "(https://www.uio.no/studier/emner/hf/ifikk/EXPHIL03/v22/canvas-media/.*\.mp4)\?"

    html_files = sorted(os.listdir("html"))

    for file in html_files:

        if file == "main_site.html":
            continue

        print(f"Extracting download links from {file}...")
        dl_links = extract_matches_from_file(dl_pattern, f"html/{file}")

        for link in dl_links:
            folder_name = file[:-5]
            filename = link.split("/")[-1]
            try:
                os.makedirs(f"videos/{folder_name}")
            except FileExistsError:
                pass
            dl_mp4(link, f"videos/{folder_name}/{filename}")

if __name__ == "__name__":
    main()
