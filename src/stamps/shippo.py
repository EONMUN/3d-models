"""
Shippo (Seven Treasures) pattern stamp.
4 overlapping circles in a 2x2 grid whose arcs create a central star shape.
"""
from registry import register_stamp


def generate_shippo_scad(width=40.0, depth=40.0, height=20.0,
                          base_height=8.0, pattern_height=3.0,
                          handle_width=25.0, handle_depth=25.0,
                          ring_width=1.5, fn=64) -> str:
    # 4 circles in 2x2 grid. Radius = spacing so each circle
    # passes through adjacent centers, creating the central star.
    spacing = width / 3
    radius = spacing
    half_s = spacing / 2
    handle_height = height - base_height
    inner_r = radius - ring_width

    # 2x2 grid centered on origin
    centers = [
        (-half_s, -half_s),
        ( half_s, -half_s),
        (-half_s,  half_s),
        ( half_s,  half_s),
    ]

    rings = ""
    for i, (cx, cy) in enumerate(centers):
        rings += f"""        translate([{cx}, {cy}, {-pattern_height}])
            linear_extrude({pattern_height})
                difference() {{
                    circle(r={radius});
                    circle(r={inner_r});
                }}
"""

    return f"""// Shippo Pattern Stamp - {width}x{depth}x{height}mm
$fn = {fn};

// Base
translate([{-width/2}, {-depth/2}, 0])
    cube([{width}, {depth}, {base_height}]);

// Handle
translate([{-handle_width/2}, {-handle_depth/2}, {base_height}])
    cube([{handle_width}, {handle_depth}, {handle_height}]);

// Pattern - 4 circles in 2x2 grid
intersection() {{
    translate([{-width/2}, {-depth/2}, {-pattern_height}])
        cube([{width}, {depth}, {pattern_height}]);
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
