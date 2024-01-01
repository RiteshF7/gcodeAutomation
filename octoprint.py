import requests

def start_print(api_key, octoprint_url, file_path):
    # API endpoint to start a print job
    endpoint = f"{octoprint_url}/api/job"

    # Headers with API key
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": api_key,
    }

    # Payload to start a print job
    payload = {
        "command": "start",
        "print": True,
        "file": file_path,
    }

    try:
        # Make a POST request to start the print job
        response = requests.post(endpoint, headers=headers, json=payload)

        # Check if the request was successful (status code 204)
        if response.status_code == 204:
            print(f"Print job started successfully for file: {file_path}")
        else:
            print(f"Failed to start print job. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def stop_print(api_key, octoprint_url):
    # API endpoint to stop the print job
    endpoint = f"{octoprint_url}/api/job"

    # Headers with API key
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": api_key,
    }

    # Payload to stop the print job
    payload = {
        "command": "cancel",
    }

    try:
        # Make a POST request to stop the print job
        response = requests.post(endpoint, headers=headers, json=payload)

        # Check if the request was successful (status code 204)
        if response.status_code == 204:
            print("Print job stopped successfully.")
        else:
            print(f"Failed to stop print job. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def send_gcode(api_key, octoprint_url, gcode_command):
    # API endpoint to send a GCODE command
    endpoint = f"{octoprint_url}/api/printer/command"

    # Headers with API key
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": api_key,
    }

    # Payload with the GCODE command
    payload = {
        "commands": [gcode_command],
    }

    try:
        # Make a POST request to send the GCODE command
        response = requests.post(endpoint, headers=headers, json=payload)

        # Check if the request was successful (status code 204)
        if response.status_code == 204:
            print(f"GCODE command '{gcode_command}' sent successfully.")
        else:
            print(f"Failed to send GCODE command. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Replace these values with your OctoPrint setup
    API_KEY = "E0F5A30AD9C94ED9B12A323C9C2B42FA"
    OCTOPRINT_URL = "http://192.168.1.43:5000"  # Replace with your OctoPrint server URL
   
   # Replace with the path to your GCODE file
    FILE_PATH = "auto.gcode"  

 # Replace with your desired GCODE command
    GCODE_COMMAND = """
G0 Z50
G0 X1 Y1 
G0 X0 Y200 
G0 X117 Y200 Z1
G0 X117 Y0 Z1 
G0 X117 Y200 Z1 
G0 X117 Y0 Z1 """
    #GCODE_COMMAND = "G28 " 

    
    
    # Start the print job
   # start_print(API_KEY, OCTOPRINT_URL, FILE_PATH)

    # Optionally, send a GCODE command
    send_gcode(API_KEY, OCTOPRINT_URL, GCODE_COMMAND)

    # Optionally, stop the print job after a certain duration or based on some condition
    #stop_print(API_KEY, OCTOPRINT_URL)


