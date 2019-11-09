from django.shortcuts import render
from django.http import HttpResponse

from ..fusioncharts import FusionCharts
from ..fusioncharts import FusionTable
from ..fusioncharts import TimeSeries
import requests

# Loading Data and schema from a Static JSON String url
# The `chart` method is defined to load chart data from an JSON string.


def chart(request):

    #data = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/plotting-multiple-series-on-time-axis-data.json').text
    #schema = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/plotting-multiple-series-on-time-axis-schema.json').text

    data = requests.get(r'C:\Users\manish.singh\Desktop\test.json').text
    schema = requests.get(r'C:\Users\manish.singh\Desktop\test.json').text
    fusionTable = FusionTable(schema, data)
    timeSeries = TimeSeries(fusionTable)

    timeSeries.AddAttribute("caption", """{ 
											text: 'Strong Seasons'
										  }""")

    timeSeries.AddAttribute("subcaption", """{ 
                                    text: 'Stock Analysis'
                                    }""")
                                    
    timeSeries.AddAttribute("series", "'Type'")

    timeSeries.AddAttribute("yAxis", """[{
                                            plot: 'Stock Value',
                                            title: 'Stock Value',
                                            format: {
                                            prefix: '$'
                                            }
                                        }]""")

    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", 700, 450, "chart-1", "json", timeSeries)

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return render(request, 'index.html', {'output': fcChart.render(), 'chartTitle': "Plotting strong and weak seasons for stock"})