# 3D Pattern Stamps - AI Agent Context

## Project Overview
This project generates 3D pattern stamps for use in art creation. Pattern stamps feature repeating geometric or decorative patterns that can be pressed into clay, paint, or other media.

**Key Documentation:**
- `SPEC.md`: Technical specifications for stamp dimensions, materials, and design principles.
- `README.md`: User-facing documentation with setup and usage instructions.

## Architecture

### Python/AnchorSCAD Workflow
All stamp models are generated via Python code using the `anchorscad` library.

- **Source:** `src/` (Root package directory).
- **Library:** Uses `anchorscad` for geometry generation.
- **Registry:** Stamps are registered using `@registry.register_stamp("name")` (defined in `src/registry.py`).

### Directory Structure
```
src/
├── registry.py          # Stamp registration system
├── config.py            # Global stamp configuration (dimensions, defaults)
├── stamps/              # Stamp pattern definitions
│   └── __init__.py
└── utils/               # Utility functions (grids, borders, etc.)
    └── __init__.py
```

### Build System
- **Output:** Generates `.scad` and `.stl` files in `build/`.
- **Usage:**
  - `bin/render`: Build all registered stamps.
  - `bin/render [filter]`: Build stamps matching the filter string.
  - `bin/render --list`: List all registered stamps.
  - `bin/render --scad-only`: Skip STL generation (faster).

### Archive
The `archive/src/` directory contains the original Python code from the previous project (Keystone Hardware modular computer case) for reference.

## Development Workflow

1. **Create a Stamp:**
   - Define a class decorated with `@ad.shape` in `src/stamps/`.
   - Use `@ad.anchor` to define connection points.
   - Register the stamp with `@registry.register_stamp("stamp_name")`.

2. **Verify/Render:**
   - Run `bin/render [stamp_name]` to generate SCAD/STL.
   - Import the `.scad` file into OpenSCAD to preview.

3. **Testing:**
   - Write unit tests in `tests/` to verify geometric dimensions.
   - Run tests with `bin/test`.

4. **Committing:**
   - Use **Semantic Commit Messages** with a clear subject line.
   - Format: `<type>(<scope>): <subject>`
   - Example: `feat(stamps): add honeycomb pattern stamp`
   - Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.

## Pattern Design Guidelines

### Stamp Components
1. **Base:** Flat surface with the pattern relief cut into it.
2. **Pattern:** Raised or recessed design that transfers to the medium.
3. **Handle:** Ergonomic grip for pressing the stamp.

### Design Principles
- Pattern elements should have adequate spacing for clean impressions.
- Relief depth should be consistent (default 3mm).
- Edges should be slightly chamfered to prevent medium buildup.
- Handle should be centered for even pressure distribution.

## AnchorSCAD Patterns

- **Boolean Operations:** Use `HoleMode` for subtractions:
  ```python
  body = shape.solid().at(...)
  hole = other_shape.hole().at(...)
  body.add_at(hole) # Subtraction
  ```
- **Coloring:** Apply `.colour()` to `SolidMode` **before** `.at()`:
  ```python
  shape.solid("name").colour("red").at("centre")
  ```
- **Matrices:** Use `ad.IDENTITY` (constant), not `ad.identity()`.

## Dependencies
- **Python:** `anchorscad`, `numpy`, `pytest`.
- **System:** `openscad` CLI required for STL generation.
- **Environment:** Managed via Nix flake.
