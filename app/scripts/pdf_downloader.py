import os,requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to download a file from a given URL
def download_file(url, directory):
    filename = os.path.join(directory, url.split("/")[-1])

    if os.path.exists(filename):
        print(f"Skipping download: {filename} already exists")
        return

    response = requests.get(url, stream=True)

    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

    print(f"Downloaded: {filename}")

# Function to find and download all PDF links on a webpage
def download_pdf_links(url, directory):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    raw_pdf_links = soup.find_all("a", href=lambda href: href and href.lower().endswith(".pdf"))

    if not raw_pdf_links:
        print("No PDF links found on the webpage.")
        return
    
    pdf_links = []
    for link in raw_pdf_links:
        absolute_url = urljoin(url, link["href"])
        pdf_links.append(absolute_url)

    unique_pdf_links = set(pdf_links)

    os.makedirs(directory, exist_ok=True)
    print(f"Downloading {len(unique_pdf_links)} PDF files to directory: {directory}")

    for link in unique_pdf_links:
        download_file(link, directory)

# Main entry point
if __name__ == "__main__":
    # Specify the URL of the website to scrape
    website_url = ""

    # Specify the directory to save the downloaded PDF files
    list = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for i in list:
        download_directory = "Dir-" + i
        download_pdf_links(website_url + i, download_directory)
