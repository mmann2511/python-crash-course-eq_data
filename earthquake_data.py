from pathlib import Path
import json

import plotly.express as px

class EarthquakeData:
    """Represents earthquake data from a GeoJSON file"""
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.mags, self.lons, self.lats, self.eq_titles = [], [], [], []
        self.title = None #store the map title

    def load_data(self):
        """Read json data and extract relevant field"""
        contents = self.filepath.read_text(encoding='utf-8')
        all_eq_data = json.loads(contents)

        # Store dataset title
        self.title = all_eq_data['metadata']['title']

        all_eq_dicts = all_eq_data['features']

        for eq_dict in all_eq_dicts:
            mag = eq_dict['properties']['mag']
            if mag is not None and mag > 0:    
                self.mags.append(mag)
                self.lons.append(eq_dict['geometry']['coordinates'][0])
                self.lats.append(eq_dict['geometry']['coordinates'][1])
                self.eq_titles.append(eq_dict['properties']['title'])        


    def plot(self):
        """Plot earthquake data on a world map"""
        fig = px.scatter_geo(
            lat=self.lats,
            lon=self.lons,
            size=self.mags,
            color=self.mags,
            color_continuous_scale='Viridis',
            title=self.title or 'Global Earthquakes',
            labels={'color': 'Magnitude'},
            projection='natural earth',
            hover_name=self.eq_titles,
        )    
        fig.show()