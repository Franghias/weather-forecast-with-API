'''
Personal Project
Due 06/29/2025 @ 11:59 PM CST
Implement your project ensure that you incorporate the programming concepts below.  
Must integrate / include:
All necessary meaningful comments
Reading and writing to a file (File I/O)
String Manipulation
Input validation
Exception handling
Regular expressions
Basic Python syntax
Flow control
Functions
Lists
'''
import requests # import requests to use the API from National Weather Service
import pyautogui # import pyautogui to use the pop up alert and prompt
import sys # import sys to use sys.exit() to exit the program
import time # import time to use time.sleep() to let the user wait for a bit before continuing the just program for fun
from pathlib import Path # import Path to use the Path function in the pathlib module
import re # import re for regular expression to find the directory from the user input

# Returns the latitude and the longitude of 5 cities in Texas
# Return type is float because both latitude and longitude are number with decimals
def city_function(user_city: str) -> float: 
    # San Angelo, TX
    if user_city == '1': 
        return 31.4638, -100.437
    # Dallas, TX
    elif user_city == '2':
        return 32.7767, -96.7970
    # Houston, TX
    elif user_city == '3':
        return 29.7604, -95.3698
    # Austin, TX
    elif user_city == '4':
        return 30.2672, -97.7431
    # Fort Worth, TX
    elif user_city == '5':
        return 32.7555, -97.3308
    
    # Just return None if the input is not valid
    return None, None


# Takes the response object and returns the status code as an integer.
def status_code(response: requests.Response) -> int:
    # Use the try except block for safely handling the error
    try: 
        # Returns successfully if the code is 200, else raises an exception with the status code.
        if response.status_code == 200:
            print("Request was successful.")
            return response.status_code
        else:
            raise Exception(f"Request failed with status code: {response.status_code}")
    # If error occurs, it prints the error message and exits the program with the status code.
    except Exception as err:
        print(f"An error occurred: {err}")
        sys.exit(response.status_code)


# I will create a file to save the weather forecast information based on the user choice
# Return None after the file is created and the information about the weather forecast at the chosen placed is saved
def file_operations(weather_forecast_content: dict) -> None:
    print('What is the name of the file you want to save the weather forecast information?')
    file_name = input('Please type in the name of the file you want to save: ').strip().strip('"')
    file_path = Path(rf'C:\Users\lle2\Downloads\{file_name}.txt')

    if not file_name or file_name == '':
        # If the user did not type in anything, we will just use 'weather_forecast' as the default file name
        print('You did not type in anything, we will use the name \"weather_forecast\" as the default file name.')
        file_name = 'weather_forecast'
        file_path = Path(rf'C:\Users\lle2\Downloads\{file_name}.txt')
    elif ' ' in file_name or '"' in file_name:
        # If the user typed in a file name with space or double quotes, we will just remove them
        print('You typed in a file name with space or double quotes, we will remove them.')
        file_name = re.sub(r'[ "]+', '_', file_name)
        file_path = Path(rf'C:\Users\lle2\Downloads\{file_name}.txt')

    # Check if the file is already exists
    if file_path.is_file():
        # if true, then we will read and output this content to the terminal
        print(f'The file {file_path.name} already exists.')
        print('Let\'s see what is the content of this file:')
        with file_path.open('r') as file:
            print(file.read())
        
        # Now we will create another file with the same name but adding '_new' at the end
        print('Now, I will create another file with a similar name.')
        file_path = file_path.with_name(f'{file_name}_new.txt')

    # print where we will store the user directory and what is the file name will be
    print('The file will be saved in this directory:', file_path.parent)
    print(f'The file name will be {file_path.name}')

    # Now we start appending the content into this file after succesfully creating 
    with file_path.open('a') as file:  # use 'a' for append mode
        # append this first line
        file.write(f'Your forecast information in {weather_forecast_content['city']}, {weather_forecast_content['state']}: \n\n')

        # because we store the 'period' and 'forecast' key in the weather_forecast_content dictionary as a list, we handle them using zip
        for period, forecast in zip(weather_forecast_content['Period'], weather_forecast_content['Detailed Forecast']):
            file.write(f"{period}:\n{str(forecast).upper()}\n\n")

        # After finishing appending everything, we just display this message to the user, saying that we finished appending.
        print(f"Weather forecast information has been appended to {file_path.name} successfully.")

    # After finishing all, no need to return anything, so we just return None as a default
    return None

# Main function
def main():
    # Pop this up to the user for more interactive program
    pyautogui.alert("Welcome to the Personal Project!", "Introduction")
    pyautogui.alert("This program will help you show the weather forecast information from the place you wish to choose", "Information")
    
    # this if statement will let the user out of the program if click 'Cancel, other wise, continue stay at the program
    if pyautogui.confirm('Do you want to continue with this program?', buttons=['OK', 'Cancel']) == 'Cancel':
        pyautogui.alert('You clicked \'Cancel\', the program will be shut down. Thank you for using the program.')

        # this will exit out of the program with the code 0, means program finished successfully
        sys.exit(0)

    print('Hi there! Let\'s begin the program')

    # Guide the user to what to type in
    print('There are currently these cities below that you can choose from: ')
    print('1. San Angelo, Texas')
    print('2. Dallas, Texas')
    print('3. Houston, Texas')
    print('4. Austin, Texas')
    print('5. Fort Worth, Texas')
    user_city = pyautogui.prompt('Please type in the number of the city you want to see the weather forecast: ')


    # if the user input is valid (from 1 to 5), we will called the city_function to get the latitude and longitude of that chosen city
    if str(user_city) >= '1' and str(user_city) <= '5':
        latitude, longitude = city_function(user_city)
    # if the user clicked 'Cancel', the user_city will be stored as a None value, then we pop a new alert and then exit the program
    elif user_city == None:
        pyautogui.alert('You did not type in anything or you clicked Cancel, please restart the program and choose a valid option.')
        sys.exit(0)
    # else, the user typed in wrong value, we will pop up an alert and then exit the program
    else:
        pyautogui.alert('Invalid city selection. Please restart the program and choose a valid option.')
        sys.exit(0)
    
    # we will get the API from the National Weather Service using the latitude and longitude we got from above
    api_response = requests.get(f'https://api.weather.gov/points/{latitude},{longitude}')

    # Then we called the status_code function to check if the API is created successfully
    status_code(api_response)

    # transform into json format and we use them through "data" variable as an object
    data = api_response.json()

    # extract city
    city = data['properties']['relativeLocation']['properties']['city']

    # extract state
    state = data['properties']['relativeLocation']['properties']['state']

    # Just a fun program here to guess what are the user trying to input
    print('Let me processing this...')
    print('... Processing ... ')
    time.sleep(3)
    print(f'Thank you for choosing {city}, {state} to see the weather forecast')

    # Extract API link to forecast the weather
    forecast_api = data['properties']['forecast']

    # Request that API link
    forecast_api_response = requests.get(forecast_api)

    # Then we called the status_code function to check if the API is created successfully
    status_code(forecast_api_response)

    # Extract data from the forecast page under json format
    data_forecast = forecast_api_response.json()

    # Catch the error if we somehow cannot extract the detailed forecast for the closest period, thus the number [0]
    try: 
        detailed_forecast = data_forecast['properties']['periods'][0]['detailedForecast']
        if not detailed_forecast:
            raise Exception('Exit the program')
    except Exception as err:
        print('The error we are having is', err)

    # At this point we have sucessfully extracted the data, I just write it down here for 
    # fun because I let the user wait 3 seconds
    print(f'\nWe have extracted the data. The weather forecast said that in {city}, {state}...\n')
    time.sleep(3)
    print(f'{data_forecast['properties']['periods'][0]['name']}: ')
    print(str(detailed_forecast).upper())
    print()

    time.sleep(3)

    # stored the length of the total periods available in the forecast data
    maximum_periods_available = len(data_forecast['properties']['periods'])

    # Then just output these to guide the user what to do next
    print('Above is just the sample of the nearest forecast, if you want to see more details')
    print('You can predict for the next ' + str(maximum_periods_available) + ' periods')
    print('You can type in the number of the period you want to see: type 1 or up to 14 in one integer number')
    print('Or you can type in \'yes\' to see all of the next forecast period')
    print('Or you can type in \'no\' to exit the program')

    # Stored the user input
    user_input = input('Please type in your input: ').strip().lower()

    # This is the dictionary that will be used to store the weather forecast information
    weather_forecast_content = {
        'city': '',
        'state': '',
        'Period': [],
        'Detailed Forecast': []
    }
    # Firstly, stored the city and state into this dictionary weather_forecast_content
    weather_forecast_content['city'] = city
    weather_forecast_content['state'] = state

    # Then we check if the user input is 'yes
    # we stored every periods the National Weather Service has from the API into the dictionary weather_forecast_content
    if user_input == 'yes':
        for i in range(maximum_periods_available):
            print(f"{data_forecast['properties']['periods'][i]['name']}: \n{str(data_forecast['properties']['periods'][i]['detailedForecast']).upper()}\n\n")
            weather_forecast_content['Period'].append(data_forecast['properties']['periods'][i]['name'])
            weather_forecast_content['Detailed Forecast'].append(str(data_forecast['properties']['periods'][i]['detailedForecast']).upper())
        
        # After appending everything, called file_opeartions function to save the weather forecast information into a file
        file_operations(weather_forecast_content)

    # else if user_input is 'no', we exit the program with the code 0, meaning the program finished successfully
    elif user_input == 'no':
        print('Exit the program!')
        sys.exit(0)

    # else if user input one number from the range 1 to the maximum_periods_available, we will print out that period's detailed forecast
    elif user_input.isdigit() and int(user_input) > 0 and int(user_input) <= maximum_periods_available:
        print(f"{data_forecast['properties']['periods'][int(user_input) - 1]['name']}: \n{str(data_forecast['properties']['periods'][int(user_input) - 1]['detailedForecast']).upper()}\n")

        weather_forecast_content['Period'] = [data_forecast['properties']['periods'][int(user_input) - 1]['name']]
        weather_forecast_content['Detailed Forecast'] = [str(data_forecast['properties']['periods'][int(user_input) - 1]['detailedForecast']).upper()]

        # Then called file_opeartions function to save the weather forecast information into a file
        file_operations(weather_forecast_content)

    # else if the user input did not type in a number, we will exit the program with the code 1, meaning the program did not finish successfully
    elif re.match(r'^[0-9]+$', user_input) is None:
        print('The user typed in the wrong input. The program will shut down.')
        sys.exit(1)

    # else, after all the validation and still not pass, it means the user typed in number that is out of range, thus the program will shut down
    # with the code 1, meaning the program did not finish successfully
    else: 
        print(f'The user does not typed in the range from 1 to {maximum_periods_available}. The program will shut down.')
        sys.exit(1)

    # Final message to the user to notice that the program is finished successfully
    # Then exit with the code 0, meaning the program finished successfully
    print('End of program without any issue. Thank you for using the program. :D')
    sys.exit(0)

# Just to confirm that we will only use the main function and not taking the main function from other programs
if __name__ == '__main__':
    main()