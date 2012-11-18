#Purpose: To export a shapefile to WKT

from osgeo import ogr
import sys, os

input = ogr.Open(sys.argv[1])


layer_in = input.GetLayer()
layer_in.ResetReading()
feature_in = layer_in.GetNextFeature()

outfile = open(sys.argv[1] + ".wkt", "w")

while feature_in is not None:
    
    geom = feature_in.GetGeometryRef()
    geom_name = geom.GetGeometryName()

    outfile.write(str(geom)+ '\n')

    feature_in = layer_in.GetNextFeature()
