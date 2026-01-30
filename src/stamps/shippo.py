"""
Shippo pattern stamp - 4 tangent circles filling the stamp.
"""
from registry import register_stamp


def generate_shippo_scad(width=40.0, depth=40.0, height=20.0,
                          base_height=8.0, pattern_height=3.0,
                          handle_width=25.0, handle_depth=25.0,
                          ring_width=1.5, fn=64) -> str:
    # 4 circles: tangent to neighbors, outer edges at stamp boundary
    # c = center offset, r = radius
    # Tangent condition: 2c = 2r → r = c
    # Boundary condition: c + r = width/2 → 2c = width/2 → c = width/4
    c = width / 4
    r = c  # tangent circles

    handle_height = height - base_height
    inner_r = r - ring_width

    hw = width / 2
    hd = depth / 2
    centers = [
        # 4 corner circles
        (-c, -c), (c, -c), (-c, c), (c, c),
        # Center circle
        (0, 0),
        # 4 edge half circles (clipped by intersection)
        (0, -hd), (0, hd),   # top and bottom edges
        (-hw, 0), (hw, 0),   # left and right edges
        # 4 corner quarter circles (clipped by intersection)
        (-hw, -hd), (hw, -hd), (-hw, hd), (hw, hd),
    ]

    rings = ""
    for cx, cy in centers:
        rings += f"""        translate([{cx}, {cy}, {-pattern_height}])
            linear_extrude({pattern_height})
                difference() {{
                    circle(r={r});
                    circle(r={inner_r});
                }}
"""

    return f"""// Shippo Pattern Stamp - 4 tangent circles
$fn = {fn};

translate([{-width/2}, {-depth/2}, 0]) cube([{width}, {depth}, {base_height}]);

intersection() {{
    translate([{-width/2}, {-depth/2}, {-pattern_height}]) cube([{width}, {depth}, {pattern_height}]);
    union() {{
{rings}    }}
}}
"""


class ShippoStampGenerator:
    def __init__(self, **kwargs):
        self.params = kwargs

    def to_scad(self) -> str:
        return generate_shippo_scad(**self.params)


@register_stamp('stamp_shippo')
def create_shippo_stamp():
    return ShippoStampGenerator()


@register_stamp('stamp_shippo_40mm')
def create_shippo_stamp_40mm():
    return ShippoStampGenerator(width=40.0, depth=40.0, height=20.0)
