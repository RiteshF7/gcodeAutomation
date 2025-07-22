# Bulk 3D Print Automation with OctoPrint API

This project automates batch 3D printing by generating dynamic G-code files and controlling OctoPrint-enabled printers via REST API. It supports configurable repeat printing, Z-axis offsets, and custom temperature settings for high-volume production.

## Features

- Dynamic G-code generation with repeat logic and configurable offsets  
- JSON-driven print configuration for temperature, copy count, and movement profiles  
- OctoPrint REST API integration for remote print control  
- Modular design using separate processors for config parsing and G-code assembly  
- Command dispatch system for structured printhead movement

## Project Structure

project-root/
├── gcodes/
│   └── main.gcode               # Auto-generated bulk G-code file
├── config.json                  # Centralized printer config and job parameters
├── main.py                      # Main automation entrypoint
├── jsonproccesor.py             # Parses config and provides structured parameters
├── codeprocessor.py             # Handles G-code segments: pre, post, and object code
└── README.md                    # Documentation and usage guide


## Configuration

Adjust values in `config.json` to suit your printer setup:


{
  "bedTemp": "65",
  "fline": "0.1",
  "sline": "0.4",
  "nozzleTemp": "215",
  "lineheight": "2.3",
  "coolbedtemp": "30",
  "coolnozzzeltemp": "210",
  "babystep": "8",
  "copies": 3
}

## How It Works
- The script generates repeated G-code segments using precode, mainobj, and postcode.
- It adds Z-height offset per iteration using lineheight + index * babystep.
- The final G-code is written to gcodes/main.gcode.
- Optional OctoPrint API commands allow you to start or cancel prints and send G-code directly.


## Example Usage

API_KEY = "YOUR_API_KEY"
OCTOPRINT_URL = "http://your-printer-ip:5000"
FILE_PATH = "auto.gcode"
GCODE_COMMAND = "G28"  # Home all axes

send_gcode(API_KEY, OCTOPRINT_URL, GCODE_COMMAND)
start_print(API_KEY, OCTOPRINT_URL, FILE_PATH)
stop_print(API_KEY, OCTOPRINT_URL)

## Getting Started

Place your desired G-code object sequence into codeprocessor.py
Set parameters in config.json
Run the script:
python main.py
Generated G-code will be saved in gcodes/main.gcode

## Future Enhancements

Add support for multiple printers
Build a web-based dashboard for managing batches
Integrate logging and real-time status feedback
Queue management for continuous production

## License
# MIT License

Feel free to use, modify, and extend for personal or commercial use.
Let me know if you want a matching GitHub repo description or contributor guidelines section. I can help you polish the whole repo top to bottom.
