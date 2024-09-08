# Cloudflare Record ID Fetcher

## Purpose

The **Cloudflare Record ID Fetcher** is a simple Python-based GUI application that allows users to fetch and display the DNS Record IDs for a specific Cloudflare zone. The user provides the **Zone ID** and **API Token**, and the app retrieves and lists the corresponding DNS records with their associated domain names and record IDs.

### Key Features
- Dark mode interface for a modern look.
- Dynamically shows or hides the scrollbar based on content size.
- Outputs Cloudflare DNS record IDs and their associated domains.

## Prerequisites

To run this application on **Windows**, you will need:

1. **Python 3.x** (including `pip` for package management).
2. **Requests** Python library for API interaction.
3. **Tkinter** Python library (should be pre-installed with Python).

### Tools for Installation:
To streamline the installation process, you can use either of the following Windows package managers:

- **Chocolatey**: A popular Windows package manager.
- **winget**: The Windows Package Manager.

## Installation Guide

### 1. Install Python

You can install Python using **Chocolatey** or **winget**.

- **Using Chocolatey**:
```
choco install python310
```
- **Using winget**
```
winget install Python.Python.3.10
```
### 2. Install Required Python Libraries

Once Python is installed, open your terminal (CMD or PowerShell) and install the required libraries using pip:
```
pip install requests
```
- **The tkinter library comes pre-installed with most Python distributions, but if for any reason it is missing, you can install it using the following command**:
```
pip install tk
```
### 3. Clone or Download the Project
- **If you haven't done so already, clone or download the project to your local machine**:
```
git clone https://github.com/networkabilityllc/CloudflareDNSUpdater
```
### 4. Running the Application

- **Navigate to the project directory and run the cloudflare_fetcher.py file**:
```
python cloudflare_fetcher.py
```
This will launch the GUI application.

### 5. Using the Application

   1) Enter your Zone ID and API Token in the respective fields.
   2) Click the Get Record ID button.
   3) The DNS Record IDs for your Cloudflare zone will be displayed in the results area.

###   How It Works

- **Zone ID: A unique identifier for your Cloudflare zone (domain).**
- **API Token: Your Cloudflare API token, which must have permissions to access DNS records.**

The app sends a GET request to Cloudflare's API to retrieve the DNS records for the provided zone and displays the record IDs along with their associated domain names.
You will need the Record ID for the bash script that runs as the scheduled updater

### 6. Using the Record ID:
   1) Open update_dns.sh in vim or nano
   2) Edit the variable section of the file and insert the:
   - ** Zone ID into zone_id (between the quotes)**
   - ** Your API Token into api_token (between the quotes)**
   - ** The Record ID obtained by running the GetRecordID.py script for the domain you want to update into record_id (between the quotes)**
   - ** The full name of the subdomain you are wanting to update into subdomain.example.com (between the quotes)**
### 7. Run the script (should not require elevation)
   - ** If there were no errors, it will simply return OK**
   - ** If there was a problem, it will report the error