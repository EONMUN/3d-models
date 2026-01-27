# Global stamp configuration
from anchorscad import datatree
from dataclasses import field


@datatree
class StampDimensions:
    """Default dimensions for pattern stamps."""

    # Base dimensions
    base_width: float = 50.0      # mm
    base_depth: float = 50.0      # mm
    base_height: float = 10.0     # mm

    # Pattern dimensions
    pattern_depth: float = 3.0    # Depth of pattern relief (mm)
    pattern_margin: float = 5.0   # Margin from edge to pattern (mm)

    # Handle dimensions
    handle_width: float = 30.0    # mm
    handle_depth: float = 30.0    # mm
    handle_height: float = 25.0   # mm
    handle_fillet: float = 3.0    # mm

    # Grid patterns
    grid_spacing: float = 5.0     # Default spacing between pattern elements (mm)

    @property
    def pattern_area_width(self) -> float:
        return self.base_width - 2 * self.pattern_margin

    @property
    def pattern_area_depth(self) -> float:
        return self.base_depth - 2 * self.pattern_margin


@datatree
class SmallStampDimensions(StampDimensions):
    """Smaller stamp configuration."""
    base_width: float = 30.0
    base_depth: float = 30.0
    base_height: float = 8.0
    handle_width: float = 20.0
    handle_depth: float = 20.0
    handle_height: float = 20.0


@datatree
class LargeStampDimensions(StampDimensions):
    """Larger stamp configuration for bigger patterns."""
    base_width: float = 100.0
    base_depth: float = 100.0
    base_height: float = 12.0
    pattern_margin: float = 8.0
    handle_width: float = 50.0
    handle_depth: float = 50.0
    handle_height: float = 35.0
