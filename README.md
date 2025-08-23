# UART Thermostat GUI

This is a Python-based graphical user interface (GUI) for controlling a simulated house thermostat. It was developed as a school project and is designed to communicate with an embedded simulation of a house environment over a UART serial connection.

## Features

*   **Real-time Temperature Monitoring:** View the current temperature of the simulated environment.
*   **Temperature Control:** Set a desired temperature and have the simulation adjust accordingly.
*   **Configurable Rooms:** The simulation can be configured with different rooms or zones by modifying the `room_configs.json` file.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd uart-thermostat-gui
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the application, run the following command from the root directory of the project:

```bash
python utg/main.py
```

## Configuration

The settings for the simulated rooms (e.g., initial temperature, size) can be adjusted by editing the `utg/room_configs.json` file.
