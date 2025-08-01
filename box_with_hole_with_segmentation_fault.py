import cadquery as cq
from cadquery.vis import show

result = cq.Workplane("front").box(2, 3, 0.5)  # make a basic prism
result = (
    result.faces(">Z").workplane().hole(1)
)  # find the top-most face and make a hole

show(result)


