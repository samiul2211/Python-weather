weather = {
    "Alabama": "Avg °F:62.8 and Avg °C:17.1",
     "Alaska": "Avg °F 26.6	and Avg °C :-3.0",
     "Arizona": "Avg °F: 60.3 and  Avg °C: 15.7"
}
  
def weather_finder():
    print("Welcome to The Average Annual Temperature for Each US State")
    user = input("What state do you want to know the Average Annual Temperature?:")


    if user in weather:
        print("The Average Annual Temperature " + user+" " + weather[user])
    else:
        print('That key is not in the dictionary.')
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        weather_finder()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()


weather_finder()










    {"name" : "Alabama", "Avg °F": "62.8", "Avg °C" :"17.1" }, 
    {"name" : "Alaska", "Avg °F": "26.6	", "Avg °C" :"-3.0" }, 
    {"name" : "Arizona", "Avg °F": "60.3", "Avg °C" :"15.7" }, 
    {"name" : "Arkansas", "Avg °F": "60.4", "Avg °C" :"15.8" }, 
    {"name" : "California", "Avg °F": "59.4", "Avg °C" :"15.2" }, 
    {"name" : "Colorado", "Avg °F": "45.1", "Avg °C" :"7.3" }, 
    {"name" : "Connecticut", "Avg °F": "49.0", "Avg °C" :"9.4" }, 
    {"name" : "Delaware", "Avg °F": "55.3", "Avg °C" :"12.9" }, 
    {"name" : "Florida", "Avg °F": "70.7", "Avg °C" :"21.5" }, 
    {"name" : "Georgia", "Avg °F": "63.5", "Avg °C" :"17.5" }, 
    {"name" : "Hawaii", "Avg °F": "70.0", "Avg °C" :"21.1" }, 
    {"name" : "Idaho", "Avg °F": "44.4", "Avg °C" :"6.9" }, 
    {"name" : "Illinois", "Avg °F": "51.8", "Avg °C" :"11.0" }, 
    {"name" : "Indiana", "Avg °F": "51.7", "Avg °C" :"10.9" }, 
    {"name" : "Iowa", "Avg °F": "47.8", "Avg °C" :"8.8" }, 
    {"name" : "Kansas", "Avg °F": "54.3", "Avg °C" :"12.4" }, 
    {"name" : "Kentucky", "Avg °F": "55.6", "Avg °C" :"13.1" }, 
    {"name" : "Louisiana", "Avg °F": "66.4", "Avg °C" :"19.1" }, 
    {"name" : "Maine", "Avg °F": "41.0", "Avg °C" :"5.0" }, 
    {"name" : "Maryland", "Avg °F": "54.2", "Avg °C" :"12.3" }, 
    {"name" : "Massachusetts", "Avg °F": "47.9", "Avg °C" :"8.8" }, 
    {"name" : "Michigan", "Avg °F": "44.4", "Avg °C" :"6.9" }, 
    {"name" : "Minnesota", "Avg °F": "41.2", "Avg °C" :"5.1" }, 
    {"name" : "Mississippi", "Avg °F": "63.4", "Avg °C" :"17.4" }, 
    {"name" : "Missouri", "Avg °F": "54.5", "Avg °C" :"12.5" }, 
    {"name" : "Montana", "Avg °F": "42.7", "Avg °C" :"5.9" }, 
    {"name" : "Nebraska", "Avg °F": "48.8", "Avg °C" :"9.3" }, 
    {"name" : "Nevada", "Avg °F": "49.9", "Avg °C" :"9.9" }, 
    {"name" : "New Hampshire", "Avg °F": "43.8", "Avg °C" :"6.6" }, 
    {"name" : "New Jersey", "Avg °F": "52.7", "Avg °C" :"11.5" },
    {"name" : "New Mexico", "Avg °F": "53.4", "Avg °C" :"11.9" },
    {"name" : "New York", "Avg °F": "45.4", "Avg °C" :"7.4" },
    {"name" : "North Carolina", "Avg °F": "59.0", "Avg °C" :"15.0" },
    {"name" : "North Dakota", "Avg °F": "40.4", "Avg °C" :"4.7" }, 
    {"name" : "Ohio	", "Avg °F": "50.7", "Avg °C" :"10.4" },
    {"name" : "Oklahoma", "Avg °F": "59.6", "Avg °C" :"15.3" },
    {"name" : "Oregon", "Avg °F": "48.4", "Avg °C" :"9.1" },
    {"name" : "Pennsylvania", "Avg °F": "48.8", "Avg °C" :"9.3" },
    {"name" : "Rhode Island", "Avg °F": "50.1", "Avg °C" :"10.1" },
    {"name" : "South Carolina", "Avg °F": "62.4", "Avg °C" :"16.9" },
    {"name" : "South Dakota", "Avg °F": "45.2", "Avg °C" :"7.3" },
    {"name" : "Tennessee", "Avg °F": "57.6", "Avg °C" :"14.2" },
    {"name" : "Texas", "Avg °F": "64.8", "Avg °C" :"18.2" },
    {"name" : "Utah	", "Avg °F": "48.6", "Avg °C" :"9.2" },
    {"name" : "Vermont", "Avg °F": "42.9", "Avg °C" :"6.1" },
    {"name" : "Virginia", "Avg °F": "55.1", "Avg °C" :"12.8" },
    {"name" : "Washington", "Avg °F": "48.3", "Avg °C" :"9.1" },
    {"name" : "West Virginia", "Avg °F": "51.8", "Avg °C" :"11.0" },
    {"name" : "Wisconsin", "Avg °F": "43.1", "Avg °C" :"6.2" },
    {"name" : "Wyoming", "Avg °F": "42.0", "Avg °C" :"5.6" },
]