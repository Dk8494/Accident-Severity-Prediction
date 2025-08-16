import streamlit as st
import numpy as np
import pickle
from PIL import Image
from sklearn import pipeline

pipe=pickle.load(open('/Users/devendrakumar/Coding /Python Lib and basic/Libraries/scikit-Learn/pipelines.pkl','rb'))
img=Image.open('/Users/devendrakumar/Coding /Python Lib and basic/Libraries/scikit-Learn/Pipelines.png',)




def pred(day_of_week, Age_band_of_driver, Sex_of_driver, Educational_level,
         Vehicle_driver_relation, Driving_experience, Type_of_vehicle, Owner_of_vehicle,
         Service_year_of_vehicle, Defect_of_vehicle, Area_accident_occured, Lanes_or_Medians,
         Road_allignment, Types_of_Junction, Road_surface_type, Road_surface_conditions,
         Light_conditions, Weather_conditions, Type_of_collision, Number_of_vehicles_involved,
         Number_of_casualties, Vehicle_movement, Casualty_class, Sex_of_casualty,
         Age_band_of_casualty, Casualty_severity, Work_of_casuality, Fitness_of_casuality,
         Pedestrian_movement, Cause_of_accident, hours_of_days, pipe):
    # Use the ACTUAL variables, not string column names
    features = np.array([[day_of_week, Age_band_of_driver, Sex_of_driver, Educational_level,
                          Vehicle_driver_relation, Driving_experience, Type_of_vehicle, Owner_of_vehicle,
                          Service_year_of_vehicle, Defect_of_vehicle, Area_accident_occured, Lanes_or_Medians,
                          Road_allignment, Types_of_Junction, Road_surface_type, Road_surface_conditions,
                          Light_conditions, Weather_conditions, Type_of_collision, Number_of_vehicles_involved,
                          Number_of_casualties, Vehicle_movement, Casualty_class, Sex_of_casualty,
                          Age_band_of_casualty, Casualty_severity, Work_of_casuality, Fitness_of_casuality,
                          Pedestrian_movement, Cause_of_accident, hours_of_days]])

    result = pipe.predict(features)
    return result


st.title("Accident prediction With Pipelines")
st.image(img)
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            min-width: 400px;   /* 👈 increase width */
            max-width: 400px;   /* 👈 keep it fixed */
        }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.write("User Input:")
    day_of_week=st.selectbox("day_of_weeks",['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
    Age_band_of_driver=st.selectbox("Age_band_of_driver",['18-30','31-50','over 51','unknown','under 18'])
    Sex_of_driver=st.selectbox("Sex_of_driver",['male','female','Unknown'])
    Educational_level=st.selectbox("Educational_level",['Junior high school','Elementary school','High school','Above high school','Writing & reading','Unknown','Illiterate'])
    Vehicle_driver_relation=st.selectbox("Vehicle_driver_relation",['Employees','Ownwer','other','Unknown'])
    Driving_experience=st.selectbox("Driving_experience",['5-10yr','2-5yr','Above 10yr','1-2yr','Below 1 yr','No License','Unknown'])
    Type_of_vehicle=st.selectbox("Type_of_driver_relation",['Automobile','Lorry (41?100Q)','Other','Pick up upto 10Q','Public (12 seats)','Stationwagen','Lorry (11?40Q)','Public (13?45 seats)','Public (> 45 seats)','Long lorry','Taxi','Motorcycle','Special vehicle','Ridden horse','Turbo','Bajaj','Bicycle'])
    Owner_of_vehicle=st.selectbox("Owner of vehicle_relation",['Owner','Governmental','Organization','Other'])
    Service_year_of_vehicle=st.selectbox("Service_year_of_vehicle",['Unknown','2-5yr','Above 10yr','5-10yr','1-2yr','Below 1yr'])
    Defect_of_vehicle = st.selectbox('Defect of Vehicle', ['No defect', '7', '5'])
    Area_accident_occured = st.selectbox('Area of Accident Occurred',
                                         ['Residential areas', 'Office areas', 'Recreational areas',
                                          'Industrial areas', 'Other', 'Church areas', 'Market areas',
                                          'Unknown', 'Rural village areas', 'Outside rural areas',
                                          'Hospital areas', 'School areas',
                                          'Rural village areasOffice areas', 'Recreational areas'])
    Lanes_or_Medians = st.selectbox('Lanes or Medians',
                                    ['Undivided Two way', 'other', 'Double carriageway (median)', 'One way',
                                     'Two-way (divided with solid lines road marking)',
                                     'Two-way (divided with broken lines road marking)', 'Unknown'])
    Road_allignment = st.selectbox('Road Allignment',
                                   ['Tangent road with flat terrain', 'Tangent road with mild grade and flat terrain',
                                    'Escarpments', 'Tangent road with rolling terrain', 'Gentle horizontal curve',
                                    'Tangent road with mountainous terrain and',
                                    'Steep grade downward with mountainous terrain',
                                    'Sharp reverse curve', 'Steep grade upward with mountainous terrain'])
    Types_of_Junction = st.selectbox('Types of Junction',
                                     ['No junction', 'Y Shape', 'Crossing', 'O Shape', 'Other', 'Unknown', 'T Shape',
                                      'X Shape'])
    Road_surface_type = st.selectbox('Road Surface Type',
                                     ['Asphalt roads', 'Earth roads', 'Asphalt roads with some distress',
                                      'Gravel roads', 'Other'])
    Road_surface_conditions = st.selectbox('Road Surface Conditions',
                                           ['Dry', 'Wet or damp', 'Snow', 'Flood over 3cm. deep'])
    Light_conditions = st.selectbox('Light Conditions', ['Daylight', 'Darkness - lights lit', 'Darkness - no lighting',
                                                         'Darkness - lights unlit'])
    Weather_conditions = st.selectbox('Weather Conditions',
                                      ['Normal', 'Raining', 'Raining and Windy', 'Cloudy', 'Other', 'Windy',
                                       'Snow', 'Unknown', 'Fog or mist'])
    Type_of_collision = st.selectbox('Type of Collision',
                                     ['Collision with roadside-parked vehicles', 'Vehicle with vehicle collision',
                                      'Collision with roadside objects', 'Collision with animals', 'Other',
                                      'Rollover', 'Fall from vehicles', 'Collision with pedestrians',
                                      'With Train', 'Unknown'])
    Number_of_vehicles_involved = st.number_input('Number of Vehicles Involved', min_value=1, max_value=10, step=1,
                                                  value=1)
    Number_of_casualties = st.number_input('Number of Casualties', min_value=1, max_value=10, step=1, value=1)
    Vehicle_movement = st.selectbox('Vehicle Movement',
                                    ['Going straight', 'U-Turn', 'Moving Backward', 'Turnover', 'Waiting to go',
                                     'Getting off', 'Reversing', 'Unknown', 'Parked', 'Stopping', 'Overtaking',
                                     'Other', 'Entering a junction'])
    Casualty_class = st.selectbox('Casualty Class', ['NA', 'Driver or rider', 'Pedestrian', 'Passenger'])
    Sex_of_casualty = st.selectbox('Sex of Casualty', ['NA', 'Male', 'Female'])
    Age_band_of_casualty = st.selectbox('Age Band of Casualty', ['NA', '31-50', '18-30', 'Under 18', 'Over 51', '5'])
    Casualty_severity = st.selectbox('Casualty Severity', ['NA', '3', '2', '1'])
    Work_of_casuality = st.selectbox('Work of Casualty',
                                     ['Driver', 'Other', 'Unemployed', 'Employee', 'Self-employed', 'Student',
                                      'Unknown'])
    Fitness_of_casuality = st.selectbox('Fitness of Casualty', ['Normal', 'Deaf', 'Other', 'Blind', 'NormalNormal'])
    Pedestrian_movement = st.selectbox('Pedestrian Movement', ["Not a Pedestrian",
                                                               "Crossing from driver's nearside",
                                                               "Crossing from nearside - masked by parked or statioNot a Pedestrianry vehicle",
                                                               "Unknown or other",
                                                               "Crossing from offside - masked by  parked or statioNot a Pedestrianry vehicle",
                                                               "In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing)",
                                                               "Walking along in carriageway, back to traffic",
                                                               "Walking along in carriageway, facing traffic",
                                                               "In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing) - masked by parked or statioNot a Pedestrianry vehicle"])
    Cause_of_accident = st.selectbox('Cause of Accident', ['Moving Backward', 'Overtaking', 'Changing lane to the left',
                                                           'Changing lane to the right', 'Overloading', 'Other',
                                                           'No priority to vehicle', 'No priority to pedestrian',
                                                           'No distancing', 'Getting off the vehicle improperly',
                                                           'Improper parking', 'Overspeed', 'Driving carelessly',
                                                           'Driving at high speed', 'Driving to the left', 'Unknown',
                                                           'Overturning', 'Turnover',
                                                           'Driving under the influence of drugs',
                                                           'Drunk driving'])
    Hour_of_Day = st.selectbox('Hour of Day',
                               [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])

if st.sidebar.button("Predict"):
    predicted_class=pred(day_of_week=day_of_week,Age_band_of_driver=Age_band_of_driver,Sex_of_driver=Sex_of_driver,Educational_level=Educational_level,Vehicle_driver_relation=Vehicle_driver_relation,Driving_experience=Driving_experience,Type_of_vehicle=Type_of_vehicle,Owner_of_vehicle=Owner_of_vehicle,Service_year_of_vehicle=Service_year_of_vehicle,Defect_of_vehicle=Defect_of_vehicle,Area_accident_occured=Area_accident_occured,Lanes_or_Medians=Lanes_or_Medians,Road_allignment=Road_allignment,Types_of_Junction=Types_of_Junction,Road_surface_type=Road_surface_type,Road_surface_conditions=Road_surface_conditions,Light_conditions=Light_conditions,Weather_conditions=Weather_conditions,Type_of_collision=Type_of_collision,Number_of_vehicles_involved=Number_of_vehicles_involved,Number_of_casualties=Number_of_casualties,Vehicle_movement=Vehicle_movement,Casualty_class=Casualty_class,Sex_of_casualty=Sex_of_casualty,Age_band_of_casualty=Age_band_of_casualty,Casualty_severity=Casualty_severity,Work_of_casuality=Work_of_casuality,Fitness_of_casuality=Fitness_of_casuality,Pedestrian_movement=Pedestrian_movement,Cause_of_accident=Cause_of_accident,hours_of_days=Hour_of_Day,pipe=pipe)

    st.success(predicted_class)






