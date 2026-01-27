# 3D Pattern Stamp Specification

## 1. Overview

This document defines the technical specifications for 3D-printable pattern stamps used in art creation. Pattern stamps transfer repeating designs onto clay, paint, plaster, or other malleable media.

### 1.1. Design Goals

- **Usability:** Stamps should be comfortable to hold and press evenly.
- **Durability:** Designs should withstand repeated use without degradation.
- **Printability:** All geometry should be 3D-printable without supports where possible.
- **Versatility:** Support various pattern styles and sizes.

## 2. Stamp Anatomy

A stamp consists of three primary components:

### 2.1. Base

The flat surface containing the pattern relief.

| Parameter       | Small  | Medium | Large  | Unit |
|-----------------|--------|--------|--------|------|
| Width           | 30     | 50     | 100    | mm   |
| Depth           | 30     | 50     | 100    | mm   |
| Height          | 8      | 10     | 12     | mm   |

### 2.2. Pattern Area

The region where the design is applied, inset from the base edges.

| Parameter       | Small  | Medium | Large  | Unit |
|-----------------|--------|--------|--------|------|
| Margin          | 5      | 5      | 8      | mm   |
| Pattern Width   | 20     | 40     | 84     | mm   |
| Pattern Depth   | 20     | 40     | 84     | mm   |

### 2.3. Handle

Ergonomic grip attached to the top of the base.

| Parameter       | Small  | Medium | Large  | Unit |
|-----------------|--------|--------|--------|------|
| Width           | 20     | 30     | 50     | mm   |
| Depth           | 20     | 30     | 50     | mm   |
| Height          | 20     | 25     | 35     | mm   |
| Fillet Radius   | 3      | 3      | 3      | mm   |

## 3. Pattern Design

### 3.1. Relief Depth

The depth at which patterns are cut into or raised from the base surface.

| Parameter       | Value  | Unit |
|-----------------|--------|------|
| Standard Depth  | 3.0    | mm   |
| Minimum Depth   | 1.5    | mm   |
| Maximum Depth   | 5.0    | mm   |

### 3.2. Pattern Spacing

Minimum spacing between pattern elements to ensure clean impressions.

| Medium Type     | Min Spacing | Unit |
|-----------------|-------------|------|
| Clay            | 2.0         | mm   |
| Paint           | 1.5         | mm   |
| Plaster         | 3.0         | mm   |

### 3.3. Edge Treatment

Pattern edges should be treated to prevent medium buildup:

- **Chamfer Angle:** 45 degrees
- **Chamfer Width:** 0.5mm
- **Draft Angle:** 2-5 degrees (for deep patterns)

## 4. Material Considerations

### 4.1. Recommended Materials

| Material | Use Case                    | Layer Height |
|----------|-----------------------------|--------------|
| PLA      | General use, clay           | 0.1-0.2mm    |
| PETG     | Paints, solvents            | 0.1-0.2mm    |
| Resin    | Fine detail patterns        | 0.025-0.05mm |

### 4.2. Print Orientation

- **Preferred:** Pattern face down on build plate
- **Reason:** Best surface finish on stamping surface
- **Handle:** May require supports depending on geometry

### 4.3. Post-Processing

- Light sanding of pattern surface (400+ grit) improves release
- Food-safe sealant for use with edible media
- Acetone vapor smoothing for ABS (optional)

## 5. Pattern Types

### 5.1. Geometric Patterns

| Pattern        | Element Size | Spacing |
|----------------|--------------|---------|
| Honeycomb      | 5-10mm hex   | 1-2mm   |
| Grid           | 3-8mm square | 1-2mm   |
| Dots           | 2-5mm circle | 3-6mm   |
| Chevron        | 5-15mm       | 2-3mm   |

### 5.2. Organic Patterns

| Pattern        | Element Size | Notes              |
|----------------|--------------|-------------------|
| Waves          | 3-5mm height | Continuous curves  |
| Leaves         | 10-20mm      | Overlapping okay   |
| Scales         | 5-10mm       | Fish scale pattern |

### 5.3. Decorative Patterns

| Pattern        | Element Size | Notes              |
|----------------|--------------|-------------------|
| Celtic knot    | 15-30mm      | Interlocking lines |
| Mandala        | Full stamp   | Radial symmetry    |
| Border         | 5-10mm width | Edge patterns      |

## 6. Export Formats

### 6.1. Primary Outputs

| Format | Purpose                    |
|--------|---------------------------|
| .scad  | OpenSCAD source (preview) |
| .stl   | 3D printing               |

### 6.2. STL Requirements

- Binary STL format
- Units: millimeters
- Manifold geometry (watertight)
- No inverted normals

## 7. Quality Checklist

Before finalizing a stamp design:

- [ ] Pattern elements have adequate spacing
- [ ] Relief depth is consistent
- [ ] Edges are chamfered
- [ ] Handle is centered on base
- [ ] Geometry is manifold
- [ ] Pattern area fits within margins
- [ ] File renders without errors in OpenSCAD
