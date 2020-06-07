from django.contrib.gis.geos import GEOSGeometry
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .forms import MapWidget
from .forms import WorldBorderForm


def index(request):
    form = WorldBorderForm()
    context = {'form': form}
    return render(request, 'index.html', context)
# def index(request):
#     template = loader.get_template('map.html')
#     map_widget = MapWidget()
#     value = GEOSGeometry(
#         '{"type":"MultiPolygon", "coordinates": [[[[-56.14914894104003,'
#         ' -33.189642368629116], [-56.14914894104003, -33.18583537264943],'
#         ' [-56.14185333251953, -33.18583537264943], [-56.14185333251953,'
#         ' -33.189642368629116], [-56.14914894104003, -33.189642368629116]],'
#         ' [[-56.14743232727051, -33.18834944515198], [-56.14743232727051,'
#         ' -33.186769179430186], [-56.14494323730469, -33.186769179430186],'
#         ' [-56.14494323730469, -33.18834944515198], [-56.14743232727051,'
#         ' -33.18834944515198]]], [[[-56.14957809448242, -33.19244363735929],'
#         ' [-56.14957809448242, -33.19000151065257], [-56.14434242248535,'
#         ' -33.19000151065257], [-56.14434242248535, -33.19244363735929],'
#         ' [-56.14957809448242, -33.19244363735929]]]]}')
#     print(map_widget.render(name='map', value=value))
#     return HttpResponse(map_widget.render(name='map', value=value))
    # context = {
    #     'hue': 2,
    #     'widget': MapWidget()
    # }
    # widget_html = MapWidget.render()
    # return render(..., {'widget_html': widget_html})
    # return MapWidget.render(context, request)
    # return HttpResponse(template.render(context, request))
