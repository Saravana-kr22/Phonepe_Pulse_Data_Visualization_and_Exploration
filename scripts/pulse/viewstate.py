import pydeck as pdk
import pandas as pd
import geopandas as gpd

def state_coordinates():
    state_map = gpd.read_file("src/geojson/indian_states.geojson")
    state_map['coordinates'] = state_map['geometry'].centroid
    coordinates_df= state_map[["ST_NM", "coordinates"]]
    coordinates_df['coordinates'] = coordinates_df['coordinates'].apply(lambda geom: [geom.x, geom.y])
    state_values = coordinates_df.set_index('ST_NM')['coordinates'].to_dict()
    return state_values

'''state_value  = {'Arunachal Pradesh': [94.6748326791631, 28.036066389221745],
                'Assam': [92.82634309387305, 26.35497847998204],
                'Chandigarh': [76.78078044460244, 30.728361392535774],
                'Karnataka': [76.16747452915338, 14.710405551302284],
                'Manipur': [93.87884193997611, 24.735076113494813],
                'Meghalaya': [91.27735620953041, 25.53557728306151],
                'Mizoram': [92.83177176819507, 23.307807060427923],
                'Nagaland': [94.46701721365893, 26.06263369503263],
                'Punjab': [75.41580388296326, 30.842226635713363],
                'Rajasthan': [73.84984184046439, 26.584407666563767],
                'Sikkim': [88.47340321820725, 27.569923150949375],
                'Tripura': [91.73906864094313, 23.745137620836996],
                'Uttarakhand': [79.20658342280629, 30.156611868236627],
                'Telangana': [79.00868646725074, 17.80072036096087],
                'Bihar': [85.61004153869405, 25.679308370917205],
                'Kerala': [76.40848222253885, 10.450407387317862],
                'Madhya Pradesh': [78.28915293669499, 23.538135963929847],
                'Andaman & Nicobar': [92.95771321465169, 11.197968822798963],
                'Gujarat': [71.57222579220684, 22.69839433488582],
                'Lakshadweep': [72.77464262902227, 11.220600017411279],
                'Odisha': [84.43061890111004, 20.513987029808025],
                'Dadra and Nagar Haveli and Daman and Diu': [72.93083224907231,
                20.242551887312832],
                'Ladakh': [76.78170790242838, 34.9428904287699],
                'Jammu & Kashmir': [74.85839980588838, 33.64511955131811],
                'Chhattisgarh': [82.04096397209855, 21.26613164744112],
                'Delhi': [77.11574431711308, 28.643204318670872],
                'Goa': [74.05414749664932, 15.36387631250899],
                'Haryana': [76.34018047967007, 29.198138148009594],
                'Himachal Pradesh': [77.24450791093216, 31.926225889963035],
                'Jharkhand': [85.56363713960563, 23.65613966615685],
                'Tamil Nadu': [78.40845445799587, 11.01405549421972],
                'Uttar Pradesh': [80.566053063026, 26.923298352608214],
                'West Bengal': [87.98378526747015, 23.811829251836777],
                'Andhra Pradesh': [79.96564733254941, 15.756113460734964],
                'Puducherry': [79.86026451499595, 11.851519914672929],
                'Maharashtra': [76.10751008526249, 19.451500358423914]}'''

def viewstate(state):

    state_value = state_coordinates()

    if state == "All-India":
        initial_view_state = pdk.ViewState(
            latitude=18.17,
            longitude=79.78,
            zoom=4.2,
            pitch=25,  
            bearing=30,
            min_zoom=4,  
            max_zoom=7,
            height = 700
        )
    else:
        initial_view_state = pdk.ViewState(
            latitude=state_value[state][1],
            longitude=state_value[state][0],
            zoom=5,
            pitch=25,  
            bearing=30,
            min_zoom=4,  
            max_zoom=7,
            height = 700
        )
    return initial_view_state