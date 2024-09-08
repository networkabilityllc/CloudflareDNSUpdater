import curses
import requests
import json

def get_record_id(zone_id, api_token, stdscr):
    if not zone_id or not api_token:
        stdscr.addstr("Zone ID and API Token are required!\n", curses.color_pair(1))
        stdscr.refresh()
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

    # Write the result to a file
    with open("recordID.txt", "w") as f:
        f.write(result_text)
    
    # Display the result on the screen
    stdscr.clear()
    stdscr.addstr(result_text + "\n", curses.color_pair(2))
    stdscr.refresh()

def main(stdscr):
    # Set up color pairs for styling
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Error message colors
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Success message colors

    stdscr.clear()

    # Display a security notice above input fields
    stdscr.addstr("Note: Zone ID and API Token input will be hidden for security reasons.\n\n", curses.color_pair(2))
    
    # Input prompts
    stdscr.addstr("Enter Cloudflare Zone ID: ", curses.A_BOLD)
    zone_id = stdscr.getstr().decode("utf-8")
    
    stdscr.addstr("Enter Cloudflare API Token: ", curses.A_BOLD)
    api_token = stdscr.getstr().decode("utf-8")

    # Call the function to get the DNS records
    get_record_id(zone_id, api_token, stdscr)

    # Wait for user input to exit
    stdscr.addstr("\nPress any key to exit...")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
