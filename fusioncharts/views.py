from django.shortcuts import render
from fusioncharts.fusioncharts import FusionCharts
# it is a default view.
# please go to the samples folder for others view


def catalogue(request):
    return render(request, 'catalogue.html')


def chart(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json",
         # The data is passed as a string in the `dataSource` as parameter.
        """{
               "chart": {
                  "caption":"Harry\'s SuperMart",
                  "subCaption":"Top 5 stores in last month by revenue",
                  "numberPrefix":"$",
                  "theme":"ocean"
               },
               "data": [
                    {"label":"Bakersfield Central", "value":"880000"},
                    {"label":"Garden Groove harbour", "value":"730000"},
                    {"label":"Los Angeles Topanga", "value":"590000"},
                    {"label":"Compton-Rancho Dom", "value":"520000"},
                    {"label":"Daly City Serramonte", "value":"330000"}
                ]
            }""")

    # returning complete JavaScript and HTML code,
    # which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output' : column2d.render()})