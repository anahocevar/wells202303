import altair as alt
import pandas as pd
from vega_datasets import data

def plot_wells(well_coords):
    
    #process data
    columns = ['latitude', 'longitude', 'depth', 'gradient']
    well_coords = pd.DataFrame(well_coords, columns=columns)
    
    counties = alt.topo_feature(data.us_10m.url, 'counties')

    map_ = (alt.Chart(counties).mark_geoshape(fill='lightgray',
                                      stroke='white')
                        .project(type='albersUsa')
                        .properties(
                        width=500,
                        height=300
            ))

    well_locations = (alt.Chart(well_coords)
                         .mark_circle()
                         .encode(longitude='longitude',
                                latitude='latitude',
                                color=alt.Color('gradient:Q',
                                        scale=alt.Scale(scheme='inferno', 
                                                            domain=[0, 0.1])),
                                 tooltip=[alt.Tooltip('depth:Q', title='Depth (m)'),
                                          alt.Tooltip('gradient:Q', title='Gradient (°C/m)', format='0.2f')])

                     )

    return map_ + well_locations