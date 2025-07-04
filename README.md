# 🌦️ Simple Texas Weather Forecast with API


## 📌 Overview

This is a personal Python project that fetches real-time weather forecasts from the **National Weather Service (NWS)** API. The user can interactively select one of five Texas cities to view the forecast and optionally save it to a local file. The app includes user prompts via pop-ups, input validation, and error handling for a smooth user experience.

This is a video where I explained how the code works and its flow: [Simple Texas Weather Forecast with API](https://angelostate.yuja.com/V/Video?v=13197984&a=19250832&isPlaying=false&startTime=0)

Feel free to comment and let me know if you see any issues or if you want to contribute to this repository.
  
### 🛠️ Core Features
  

- 📍 Choose from five Texas cities for weather data

- ⛅ Fetches forecast data using the ([National Weather Service](https://api.weather.gov/))

- 💾 Saves the forecast to a `.txt` file, handling existing file conflicts gracefully. The default directory is `C:\Users\User\Downloads\`, and you can adjust it to save as you wish.

- 🧠 Uses core Python concepts: file I/O, regular expressions, exception handling, input validation, functions, and more

- 🖥️ User-friendly prompts with `pyautogui` popups


## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.7+
- pip install requests pyautogui
- Internet connection (to access the weather API)
  
### 📦 Installation
1.  **Clone this repository:**
```bash
git  clone https://github.com/Franghias/weather-forecast-with-API.git

cd  weather-forecast-with-API
```
  

## 🖥️ How to Use

1.  **Run the file through Visual Studio Code or other code editor:**
  
2.  **Follow on-screen prompts:**  
- Choose a city by typing a number (1–5)

- Decide whether to view just a sample forecast or more detailed ones

- Choose whether to save the forecast to a file


3.  **File Output Example:**

Forecasts are saved to your `Downloads` folder (C:\Users\User\Downloads\) with the provided file name. If the file already exists, a new one will be created with `_new` appended.
  
---


## 🧠 Concepts Used

This project demonstrates:

- ✅ **Basic Python syntax** (functions, control flow, loops, etc.)

- ✅ **Functions and modularization**

- ✅ **User input validation** and `pyautogui`-based prompts

- ✅ **String manipulation** and formatting

- ✅ **Regular expressions** using `re`

- ✅ **File I/O** using `pathlib` and safe appending

- ✅ **Exception handling** with `try/except`

- ✅ **HTTP requests** using `requests`

- ✅ **Working with JSON APIs**
  
---
  

## 📸 Sample Output

```text

Welcome to the Personal Project!

This program will help you show the weather forecast information from the place you wish to choose

Hi there! Let's begin the program
There are currently these cities below that you can choose from: 
1. San Angelo, Texas
2. Dallas, Texas
3. Houston, Texas
4. Austin, Texas
5. Fort Worth, Texas
Request was successful.
Let me processing this...
... Processing ...
Thank you for choosing Austin, TX to see the weather forecast
Request was successful.

We have extracted the data. The weather forecast said that in Austin, TX...

Today: 
A SLIGHT CHANCE OF SHOWERS AND THUNDERSTORMS. MOSTLY SUNNY, WITH A HIGH NEAR 97. 
HEAT INDEX VALUES AS HIGH AS 106. SOUTH WIND 0 TO 5 MPH. CHANCE OF PRECIPITATION IS 20%.

Above is just the sample of the nearest forecast, if you want to see more details
You can predict for the next 14 periods
You can type in the number of the period you want to see: type 1 or up to 14 in one integer number
Or you can type in 'yes' to see all of the next forecast period
Or you can type in 'no' to exit the program
Please type in your input: 2
Tonight: 
A SLIGHT CHANCE OF SHOWERS AND THUNDERSTORMS BEFORE 7PM. MOSTLY CLEAR, WITH A LOW AROUND 75. 
HEAT INDEX VALUES AS HIGH AS 102. SOUTH WIND AROUND 5 MPH. CHANCE OF PRECIPITATION IS 20%. 
NEW RAINFALL AMOUNTS LESS THAN A TENTH OF AN INCH POSSIBLE.

What is the name of the file you want to save the weather forecast information?
Please type in the name of the file you want to save: weather_forecast_Austin 
The file will be saved in this directory: C:\Users\User\Downloads
The file name will be weather_forecast_Austin.txt
Weather forecast information has been appended to weather_forecast_Austin.txt successfully.
End of program without any issue. Thank you for using the program. :D
```
