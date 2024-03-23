import pydeck as pdk
import pandas as pd
import geopandas as gpd
from scripts.data.hover_data import *
from scripts.pulse.hexa_value import *


def update_map(info_dict):
    state = info_dict["state"]
    state_map = gpd.read_file("src/geojson/indian_states.geojson")
    info_dict_i= info_dict
    info_dict_i["state"] = "All-India"
    state_map["state"] = "India"
    hover_df = hover_data(info_dict_i)
    state_map = pd.merge(state_map, hover_df, on="ST_NM")
    district_map = gpd.read_file("src/geojson/indian_districts.geojson")
    district_map = district_map[district_map.NAME_1 == state]
    district_code = district_map[["NAME_2","geometry"]]
    district_code = district_code.rename(columns={'NAME_2': 'ST_NM'})
    info_dict["state"] = state
    hover_df = hover_data(info_dict)
    print(info_dict)
    print(1)
    print(hover_df)
    print(district_code)
    district_code = pd.merge(district_code, hover_df, on='ST_NM')
    district_code["state"] = state
    state_code = state_map[state_map.ST_NM != state]
    updated_map = pd.concat([state_code,district_code], ignore_index=True)
    print(2)
    print(updated_map)
    return updated_map

def update_hexa_data(state):
    hexagon_data = pd.read_csv("src/pincode_coordinates.csv")
    updated_hexa_data = hexagon_data[hexagon_data.state == state]
    return updated_hexa_data

def create_layers(info_dict):
    state_map = gpd.read_file("src/geojson/indian_states.geojson")
    hexagon_data = pd.read_csv("src/pincode_coordinates.csv")
    state = info_dict["state"]
    
    
    if state == "All-India":
        hover_df = hover_data(info_dict)
        state_map = pd.merge(state_map, hover_df, on="ST_NM")
        state_map["state"] = "India"

        geolayer = pdk.Layer(
            'GeoJsonLayer',
            data=state_map,
            get_fill_color=[58,60,94],  
            get_line_color=[255, 255, 255],   
            lineWidthMinPixels=0.6,
            filled=True,
            stroked=True,
            interactive=True, 
            pickable=True,
            auto_highlight=True,
            highlight_color=[111,54,173],  
            update_triggers={"get_fill_color": "highlighted"},  
            order=1,
        )

        hexagon_data = add_hexa_value(hexagon_data, info_dict)
        print(hexagon_data)
        
        hexagon_layer = pdk.Layer(
            'HexagonLayer', 
            data=hexagon_data,
            get_position='[longitude, latitude]', 
            radius=8500,
            elevation_scale=400, 
            extruded=True, 
            #pickable=True, 
            opacity=0.3, 
            #elevation_range=[0, 3000], 
            upper_percentile=100, 
            interactive=True, 
            order=3,
            zIndex=1000,  
            get_fill_color=[255, 0, 0] ,
            get_elevation='val',
            coverage=1) 
        return geolayer, hexagon_layer
    else:
        updated_map = update_map(info_dict)
        updated_hexa_data = update_hexa_data(state)
        hexagon_data = add_hexa_value(updated_hexa_data, info_dict)
        geolayer = pdk.Layer(
            'GeoJsonLayer',
            data=updated_map,
            get_fill_color=[58,60,94],  
            get_line_color=[255, 255, 255],   
            lineWidthMinPixels=0.6,
            filled=True,
            stroked=True,
            interactive=True, 
            pickable=True,
            auto_highlight=True,
            highlight_color=[111,54,173],  
            update_triggers={"get_fill_color": "highlighted"},  
            order=1,
        )
        print(hexagon_data)
        hexagon_layer = pdk.Layer(
            'HexagonLayer', 
            data=hexagon_data,
            get_position='[longitude, latitude]', 
            radius=8500,
            elevation_scale=500, 
            extruded=True, 
            #pickable=True, 
            opacity=0.3, 
            #elevation_range=[0, 3000], 
            upper_percentile=100, 
            interactive=True, 
            order=3,
            zIndex=1000,  
            get_fill_color=[255, 0, 0] ,
            get_elevation='val',
            coverage=1)
        
        info_dict["state"] = "All-India"
        hover_df = hover_data(info_dict)
        state_map = pd.merge(state_map, hover_df, on="ST_NM")
        state_map["state"] = "India"
        state_map['label_lon'] = state_map['geometry'].centroid.x
        state_map['label_lat'] = state_map['geometry'].centroid.y
        
        text_layer = pdk.Layer(
            "TextLayer",
            data=state_map[state_map.ST_NM != state],
            get_position=["label_lon", "label_lat"],
            get_text="ST_NM",
            get_color=[255, 255, 255],  # RGBA values for text color
            get_size=12.5,
            pickable=True,
            get_alignment_baseline="'bottom'",
            get_text_anchor="'middle'"
        )

        return geolayer, hexagon_layer, text_layer

