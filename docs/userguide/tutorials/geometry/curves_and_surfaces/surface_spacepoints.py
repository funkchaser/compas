from compas.geometry import Point
from compas.geometry import Polyline
from compas.geometry import NurbsSurface
from compas.scene import SceneObject


points = [
    [Point(0, 0, 0), Point(1, 0, 0), Point(2, 0, 0), Point(3, 0, 0), Point(4, 0, 0)],
    [Point(0, 1, 0), Point(1, 1, 2), Point(2, 1, 2), Point(3, 1, 0), Point(4, 1, 0)],
    [Point(0, 2, 0), Point(1, 2, 2), Point(2, 2, 2), Point(3, 2, 0), Point(4, 2, 0)],
    [Point(0, 3, 0), Point(1, 3, 0), Point(2, 3, 0), Point(3, 3, 0), Point(4, 3, 0)],
]

surface = NurbsSurface.from_points(points=points)

# ==============================================================================
# Points over UV space
# ==============================================================================

spacepoints = surface.xyz(nu=50, nv=10)

# ==============================================================================
# Visualisation
# ==============================================================================

SceneObject.clear()

for row in surface.points:
    SceneObject(Polyline(row)).draw()

for col in zip(*list(surface.points)):
    SceneObject(Polyline(col)).draw()

SceneObject(surface).draw()

for point in spacepoints:
    SceneObject(point).draw()

SceneObject.redraw()
