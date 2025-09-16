from src.mapfile_web import PubMapWEB
import sys


map_web = PubMapWEB(sys.argv[1])
map_web.wsgi()
