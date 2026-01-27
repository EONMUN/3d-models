"""
Shippo (Seven Treasures) pattern stamp.

Classic Japanese pattern of overlapping circles creating almond-shaped
(vesica piscis) intersections.

This module generates OpenSCAD code directly rather than using AnchorSCAD's
geometry system, because the Shippo pattern requires proper 2D ring extrusion
to maintain ring geometry when circles overlap.
"""
from registry import register_stamp


def generate_shippo_scad(
    width: float = 40.0,
    depth: float = 40.0,
    height: float = 20.0,
    base_height: float = 8.0,
    circle_radius: float = 10.0,
    ring_width: float = 1.2,
    pattern_height: float = 3.0,
    handle_width: float = 25.0,
    handle_depth: float = 25.0,
    fn: int = 64
) -> str:
    """Generate OpenSCAD code for a Shippo pattern stamp."""
    half_w = width / 2
    half_d = depth / 2
    handle_height = height - base_height
    spacing = circle_radius
    inner_r = circle_radius - ring_width

    # Generate ring center positions
    centers = []
    x = -half_w - circle_radius
    while x <= half_w + circle_radius:
        y = -half_d - circle_radius
        while y <= half_d + circle_radius:
            centers.append((x, y))
            y += spacing
        x += spacing

    lines = [
        f"// Shippo (Seven Treasures) Pattern Stamp",
        f"// Dimensions: {width}x{depth}x{height}mm",
        f"$fn = {fn};",
        "",
        f"// Base plate",
        f"translate([{-half_w}, {-half_d}, 0])",
        f"    cube([{width}, {depth}, {base_height}]);",
        "",
        f"// Handle",
        f"translate([{-handle_width/2}, {-handle_depth/2}, {base_height}])",
        f"    cube([{handle_width}, {handle_depth}, {handle_height}]);",
        "",
        f"// Shippo pattern (clipped to boundary)",
        f"intersection() {{",
        f"    // Clipping boundary",
        f"    translate([{-half_w}, {-half_d}, {-pattern_height}])",
        f"        cube([{width}, {depth}, {pattern_height}]);",
        f"    ",
        f"    // Union of all rings",
        f"    union() {{",
    ]

    for i, (cx, cy) in enumerate(centers):
        lines.extend([
            f"        // Ring {i} at ({cx:.1f}, {cy:.1f})",
            f"        translate([{cx}, {cy}, {-pattern_height}])",
            f"            linear_extrude({pattern_height})",
            f"                difference() {{",
            f"                    circle(r={circle_radius});",
            f"                    circle(r={inner_r});",
            f"                }}",
        ])

    lines.extend([
        f"    }}",
        f"}}",
    ])

    return "\n".join(lines)


class ShippoStampGenerator:
    """Generator for Shippo pattern stamps."""

    def __init__(self, **kwargs):
        self.width = kwargs.get('width', 40.0)
        self.depth = kwargs.get('depth', 40.0)
        self.height = kwargs.get('height', 20.0)
        self.base_height = kwargs.get('base_height', 8.0)
        self.circle_radius = kwargs.get('circle_radius', 10.0)
        self.ring_width = kwargs.get('ring_width', 1.2)
        self.pattern_height = kwargs.get('pattern_height', 3.0)
        self.handle_width = kwargs.get('handle_width', 25.0)
        self.handle_depth = kwargs.get('handle_depth', 25.0)
        self.fn = kwargs.get('fn', 64)

    def to_scad(self) -> str:
        return generate_shippo_scad(
            width=self.width,
            depth=self.depth,
            height=self.height,
            base_height=self.base_height,
            circle_radius=self.circle_radius,
            ring_width=self.ring_width,
            pattern_height=self.pattern_height,
            handle_width=self.handle_width,
            handle_depth=self.handle_depth,
            fn=self.fn
        )


@register_stamp('stamp_shippo')
def create_shippo_stamp():
    return ShippoStampGenerator()


@register_stamp('stamp_shippo_40mm')
def create_shippo_stamp_40mm():
    return ShippoStampGenerator(width=40.0, depth=40.0, height=20.0)
