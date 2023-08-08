import os
import requests
from datetime import datetime, timedelta

# URLs for the files
urls = [
    "https://www.cftc.gov/dea/newcot/c_disagg.txt",
    "https://www.cftc.gov/dea/newcot/f_disagg.txt",
    "https://www.cftc.gov/dea/newcot/FinFutWk.txt",
    "https://www.cftc.gov/dea/newcot/FinComWk.txt"
]

# Directory to save the downloaded files
download_dir = "weekly_COT_data"

# Ensure the download directory exists
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

def download_file(url, dest_folder):
    response = requests.get(url)
    date_today = datetime.now()
    date_today_str = date_today.strftime("%Y%m%d")
    if response.status_code == 200:
        file_name = url.split("/")[-1]
        file_name_with_date = file_name.split(".")[0] + "_" + date_today_str + "." + file_name.split(".")[1]
        file_path = os.path.join(dest_folder, file_name_with_date)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_name_with_date} to {dest_folder}")
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")

# Download files for each URL
for url in urls:
    download_file(url, download_dir)
