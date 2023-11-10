from compas.geometry import Point
from compas.geometry import Polyline
from compas.geometry import NurbsCurve
from compas.scene import SceneObject
from compas.colors import Color


points = [Point(0, 0, 0), Point(3, 6, 0), Point(6, -3, 3), Point(10, 0, 0)]

curve = NurbsCurve.from_parameters(
    points=points,
    weights=[1.0, 1.0, 1.0, 1.0],
    knots=[0.0, 1.0],
    multiplicities=[4, 4],
    degree=3,
)

# ==============================================================================
# Visualisation
# ==============================================================================

SceneObject.clear()

SceneObject(curve).draw(color=Color.green())
SceneObject(Polyline(curve.points)).draw(show_points=True)

SceneObject.redraw()
