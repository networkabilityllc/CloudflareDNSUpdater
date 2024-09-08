import tkinter as tk
from tkinter import scrolledtext
import requests
from tkinter import messagebox

def get_record_id():
    zone_id = zone_id_entry.get()
    api_token = api_token_entry.get()
    
    if not zone_id or not api_token:
        messagebox.showerror("Input Error", "Zone ID and API Token are required!")
        return

    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data['success']:
            result_text = "Record ID(s):\n"
            for record in data['result']:
                result_text += f"Domain: {record['name']}\nID: {record['id']}\n"
        else:
            result_text = "Error retrieving data: " + str(data['errors'])

    except requests.exceptions.HTTPError as err:
        result_text = f"HTTP error occurred: {err}"
    except Exception as err:
        result_text = f"Other error occurred: {err}"

    # Display the results in the scrolledtext area
    result_text_area.delete(1.0, tk.END)  # Clear previous text
    result_text_area.insert(tk.END, result_text)

# Set up the tkinter window
root = tk.Tk()
root.title("Cloudflare Record ID Fetcher")

# Dark mode color scheme
bg_color = "#2E2E2E"  # Dark gray background
fg_color = "#FFFFFF"  # White text
entry_bg_color = "#4B4B4B"  # Darker gray for entry fields
button_bg_color = "#444444"  # Gray background for the button

# Configure the window background color
root.configure(bg=bg_color)

# Create a text area for displaying results with dark mode colors
result_text_area = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD, bg=bg_color, fg=fg_color, insertbackground=fg_color)
result_text_area.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

# Create input fields for Zone ID and API Token with dark mode colors
tk.Label(root, text="Zone ID:", bg=bg_color, fg=fg_color).grid(column=0, row=1, sticky='E', padx=5, pady=5)
zone_id_entry = tk.Entry(root, width=40, bg=entry_bg_color, fg=fg_color, insertbackground=fg_color)
zone_id_entry.grid(column=1, row=1, padx=5, pady=5)

tk.Label(root, text="API Token:", bg=bg_color, fg=fg_color).grid(column=0, row=2, sticky='E', padx=5, pady=5)
api_token_entry = tk.Entry(root, width=40, show='*', bg=entry_bg_color, fg=fg_color, insertbackground=fg_color)  # Mask the API token with *
api_token_entry.grid(column=1, row=2, padx=5, pady=5)

# Create a button to trigger the API call with dark mode colors
fetch_button = tk.Button(root, text="Get Record ID", command=get_record_id, bg=button_bg_color, fg=fg_color)
fetch_button.grid(column=0, row=3, columnspan=2, pady=10)

# Start the tkinter main loop
root.mainloop()
