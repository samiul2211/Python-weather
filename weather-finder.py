#import weather_finder

weather = {
    "Alabama": "Avg °F 62.8 and Avg °C : 17.1", 
    "Alaska": "Avg °F: 26.6	and Avg °C: -3.0", 
    "Arizona": "Avg °F: 60.3 and Avg °C:15.7", 
    "Arkansas": "Avg °F: 60.4 and Avg °C: 15.8", 
    "California": "Avg °F: 59.4 and Avg °C:15.2", 
    "Colorado": "Avg °F: 45.1 and Avg °C: 7.3", 
    "Connecticut": "Avg °F: 49.0 and Avg °C: 9.4",
    "Delaware": "Avg °F: 55.3 and Avg °C: 12.9", 
    "Florida": "Avg °F 70.7 and Avg °C: 21.5", 
    "Georgia": "Avg °F 63.5 and Avg °C: 17.5", 
    "Hawaii": "Avg °F: 70.0 and Avg °C: 21.1", 
    "Idaho": "Avg °F: 44.4 and Avg °C: 6.9",
    "Illinois": "Avg °F: 51.8 and Avg °C: 11.0" , 
    "Indiana": "Avg °F: 51.7 and Avg °C: 10.9", 
    "Iowa": "Avg °F: 47.8 and Avg °C: 8.8", 
    "Kansas": "Avg °F: 54.3 and Avg °C: 12.4", 
    "Kentucky": "Avg °F: 55.6 and Avg °C: 13.1",
    "Louisiana": "Avg °F: 66.4 and Avg °C: 19.1", 
    "Maine": "Avg °F: 41.0 and Avg °C: 5.0", 
    "Maryland": "Avg °F: 54.2 and Avg °C: 12.3", 
    "Massachusetts": "Avg °F: 47.9 and Avg °C: 8.8", 
    "Michigan": "Avg °F: 44.4 and Avg °C: 6.9",
    "Minnesota": "Avg °F: 41.2 and Avg °C: 5.1", 
    "Mississippi": "Avg °F: 63.4 and Avg °C: 17.4", 
    "Missouri": "Avg °F: 54.5 and Avg °C: 12.5", 
    "Montana": "Avg °F: 42.7 and Avg °C: 5.9",
    "Nebraska": "Avg °F: 48.8 and Avg °C:9.3", 
    "Nevada": "Avg °F: 49.9 and Avg °C: 9.9", 
    "New Hampshire": "Avg °F: 43.8 and Avg °C: 6.6", 
    "New Jersey": "Avg °F: 52.7 and Avg °C: 11.5", 
    "New Mexico": "Avg °F: 53.4 and Avg °C: 11.9",
    "New York": "Avg °F: 45.4 and Avg °C: 7.4",
    "North Carolina": "Avg °F: 59.0 and Avg °C: 15.0",
    "North Dakota": "Avg °F: 40.4 and Avg °C: 4.7", 
    "Ohio": "Avg °F: 50.7 and Avg °C: 10.4",
    "Oklahoma": "Avg °F: 59.6 and Avg °C: 15.3",
    "Oregon": "Avg °F: 48.4 and Avg °C: 9.1",
    "Pennsylvania": "Avg °F: 48.8 and Avg °C: 9.3",
    "Rhode Island": "Avg °F: 50.1 and Avg °C: 10.1",
    "South Carolina": "Avg °F: 62.4 and Avg °C: 16.9",
    "South Dakota": "Avg °F: 45.2 and Avg °C: 7.3",
    "Tennessee": "Avg °F: 57.6 and Avg °C: 14.2",
    "Texas": "Avg °F: 64.8 and Avg °C: 18.2",
    "Utah": "Avg °F: 48.6 and Avg °C: 9.2",
    "Vermont": "Avg °F: 42.9 and Avg °C: 6.1",
    "Virginia": "Avg °F: 55.1 and Avg °C: 12.8",
    "Washington": "Avg °F: 48.3 and Avg °C: 9.1",
    "West Virginia": "Avg °F: 51.8 and Avg °C: 11.0",
    "Wisconsin": "Avg °F: 43.1 and Avg °C: 6.2",
    "Wyoming": "Avg °F: 42.0 and Avg °C : 5.6",
}

def weather_finder():
    print("Welcome to The Average Annual Temperature for Each US State")
    user = input("What state do you want to know the Average Annual Temperature?:")

    user = user.title()

    if user in weather:
        print("")
        print("The Average Annual Temperature " + user+" " + weather[user])
    else:
        print("")
        print('That key is not in the dictionary.')
    again()


def again():
    calc_again = input('''
Do you want to another state Average Annual Temperature?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        weather_finder()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()


weather_finder()

    

#print(weather[4]["name"])

