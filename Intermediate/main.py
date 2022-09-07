import requests
import datetime
from datetime import datetime

API_KEY  = '647c93399c38f664311c2e439a9e5ef8'
API_ID = 'a12934b9'

# use in the json = params
params = {
 "query":"ran 3 miles and swim for 10 minutes",
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":20
}

headers = {"x-app-id": API_ID, 
           "x-app-key": API_KEY}

repsonse = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=params, headers=headers)
print(repsonse)
result = repsonse.json()
exercises = result['exercises']
print(exercises)

now = datetime.now()
today_date = now.date().strftime("%d/%m/%Y")
time = now.strftime("%X")

# add each exercise to the sheety 
for i in range(len(exercises)):
    exercise = exercises[i]
    type = exercise.get('name').title()
    duration_min = float(exercise.get('duration_min'))
    calories = float(exercise.get('nf_calories'))

    # Parameters have to be lower case
    row = {
        "workout":{
            "date": today_date,
            "time": time,
            "exercise": type,
            "duration": duration_min,
            "calories": calories
        }
    }
    post_exercise_to_sheety = requests.post("https://api.sheety.co/adbcb11bf48d8c09db36862ba2d8d3e4/workoutTracking/workouts", json = row)
    print(post_exercise_to_sheety.text)
