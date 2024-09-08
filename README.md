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
