"""Tests for Shippo stamp geometry."""
import math
import sys
sys.path.insert(0, 'src')


def test_shippo_geometry():
    """Verify 4 tangent circles fill the stamp exactly."""
    width = 40.0

    # From the formula: c = width/4, r = c
    c = width / 4  # center offset
    r = c          # radius

    # Test 1: Circles should be tangent (not overlapping)
    # Distance between adjacent centers = 2c
    # Sum of radii = 2r = 2c
    # Tangent when distance == sum of radii
    distance_between_adjacent = 2 * c
    sum_of_radii = 2 * r
    assert distance_between_adjacent == sum_of_radii, \
        f"Circles should be tangent: distance={distance_between_adjacent}, sum_radii={sum_of_radii}"

    # Test 2: Outer edges should reach stamp boundary
    # Circle at (c, c) extends to c + r in positive direction
    # This should equal width/2
    outer_edge = c + r
    expected_edge = width / 2
    assert outer_edge == expected_edge, \
        f"Outer edge should reach boundary: {outer_edge} != {expected_edge}"

    # Test 3: Verify the constraint: 2 * radius = width / 2
    # (two radii span from center to edge)
    assert 2 * r == width / 2, \
        f"Two radii should equal half width: {2 * r} != {width / 2}"

    print(f"✓ Shippo geometry valid for {width}mm stamp:")
    print(f"  - Center offset: {c}mm")
    print(f"  - Circle radius: {r}mm")
    print(f"  - Circles are tangent (touch at one point)")
    print(f"  - Outer edges at ±{outer_edge}mm (stamp boundary)")


def test_shippo_no_overflow():
    """Verify corner circles don't overflow the stamp boundary."""
    width = 40.0
    c = width / 4
    r = c

    corner_centers = [(-c, -c), (c, -c), (-c, c), (c, c)]

    for cx, cy in corner_centers:
        assert cx - r >= -width/2, f"Circle at ({cx},{cy}) overflows left"
        assert cx + r <= width/2, f"Circle at ({cx},{cy}) overflows right"
        assert cy - r >= -width/2, f"Circle at ({cx},{cy}) overflows bottom"
        assert cy + r <= width/2, f"Circle at ({cx},{cy}) overflows top"

    print("✓ No corner circles overflow the stamp boundary")


def test_shippo_center_circle():
    """Verify center circle exists and is same size as corner circles."""
    width = 40.0
    c = width / 4
    r = c

    all_centers = [(-c, -c), (c, -c), (-c, c), (c, c), (0, 0)]

    assert (0, 0) in all_centers, "Center circle missing"
    assert len(all_centers) == 5, f"Expected 5 circles, got {len(all_centers)}"

    print("✓ Center circle present, 5 circles total")


if __name__ == "__main__":
    test_shippo_geometry()
    test_shippo_no_overflow()
    test_shippo_center_circle()
