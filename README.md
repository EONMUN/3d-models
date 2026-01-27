# 3D Pattern Stamps

Generate 3D-printable pattern stamps for art creation. Pattern stamps feature repeating geometric or decorative designs that can be pressed into clay, paint, plaster, or other media.

## Features

- Parametric stamp generation via Python/AnchorSCAD
- Configurable dimensions for different stamp sizes
- Variety of pattern styles (geometric, organic, decorative)
- Ergonomic handle designs
- Export to STL for 3D printing

## Requirements

- Python 3.10+
- [OpenSCAD](https://openscad.org/) (for STL generation)
- Nix (optional, for reproducible environment)

## Installation

### With Nix (Recommended)

```bash
# Enter the development environment
nix develop
```

### Manual Setup

```bash
# Install Python dependencies
pip install anchorscad numpy pytest
```

## Usage

### List Available Stamps

```bash
bin/render --list
```

### Build All Stamps

```bash
bin/render
```

### Build Specific Stamp

```bash
bin/render honeycomb
```

### Generate SCAD Only (Faster)

```bash
bin/render --scad-only
```

### Preview in OpenSCAD

```bash
openscad build/stamp_name.scad
```

## Project Structure

```
src/
├── registry.py          # Stamp registration system
├── config.py            # Global configuration
├── stamps/              # Stamp pattern definitions
│   └── __init__.py
└── utils/               # Utility functions
    └── __init__.py
build/                   # Generated SCAD and STL files
archive/                 # Reference code from previous project
```

## Creating New Stamps

1. Create a new file in `src/stamps/` (e.g., `my_pattern.py`)
2. Define a stamp class using AnchorSCAD:

```python
import anchorscad as ad
from registry import register_stamp
from config import StampDimensions

@ad.shape
@register_stamp("my_pattern")
class MyPatternStamp(ad.CompositeShape):
    dims: StampDimensions = ad.dtfield(StampDimensions())

    def build(self, maker):
        # Build your stamp geometry here
        pass
```

3. Run `bin/render my_pattern` to generate the files

## Stamp Sizes

| Size   | Base (mm)   | Pattern Area (mm) | Handle Height (mm) |
|--------|-------------|-------------------|-------------------|
| Small  | 30 x 30     | 20 x 20           | 20                |
| Medium | 50 x 50     | 40 x 40           | 25                |
| Large  | 100 x 100   | 84 x 84           | 35                |

## License

MIT License - See [LICENSE](LICENSE) for details.
