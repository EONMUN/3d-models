# AnchorSCAD stamp registration
import anchorscad as ad
import inspect
import re
from typing import Dict, Callable

# Stamp Registry
_STAMP_REGISTRY: Dict[str, Callable[[], ad.Shape]] = {}


def register_stamp(name: str):
    """Decorator to register a stamp for rendering."""
    def decorator(cls_or_func):
        _STAMP_REGISTRY[name] = cls_or_func
        return cls_or_func
    return decorator


def get_registry():
    return _STAMP_REGISTRY


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def auto_register_module(module, prefix: str = ""):
    """
    Scans a module for Shape classes and registers them if they have defaults.
    """
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, ad.Shape) and obj is not ad.Shape and obj is not ad.CompositeShape:
            # Only register classes defined in this module
            if obj.__module__ != module.__name__:
                continue

            # Generate candidate name
            part_name = prefix + camel_to_snake(name)

            try:
                # Check for required arguments without defaults
                sig = inspect.signature(obj)
                required_args = [
                    p.name for p in sig.parameters.values()
                    if p.default == inspect.Parameter.empty and p.name != 'self'
                ]

                if not required_args:
                    if part_name not in _STAMP_REGISTRY:
                        _STAMP_REGISTRY[part_name] = lambda cls=obj: cls()
            except Exception:
                pass
