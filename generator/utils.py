import os

def ensure_directories():
    """Create necessary directories if they don't exist."""
    os.makedirs("output/models", exist_ok=True)
    os.makedirs("output/controllers", exist_ok=True)
    os.makedirs("output/routes", exist_ok=True)

# ✅ Define allowed primitive data types
PRIMITIVE_TYPES = {
    "string": "String",
    "int": "Number",
    "float": "Number",
    "boolean": "Boolean"
}

def format_attribute(attr_name, attr_type):
    """
    - ✅ Handles single primitive types (string, int, float, boolean)
    - ✅ Handles list of primitive types (string[], int[], etc.)
    - ✅ Handles foreign keys (any type not in primitive list)
    - ✅ Handles list of foreign keys (Cart[], Product[])
    """
    if attr_type.endswith("[]"):  # Handling lists
        base_type = attr_type[:-2]
        if base_type in PRIMITIVE_TYPES:
            return f"[{PRIMITIVE_TYPES[base_type]}]"  # List of Primitive Types
        return f"[{{ type: mongoose.Schema.Types.ObjectId, ref: '{base_type}' }}]"  # List of Foreign Keys

    if attr_type in PRIMITIVE_TYPES:  # Primitive Type
        return f"{{ type: {PRIMITIVE_TYPES[attr_type]}, required: true }}"

    return f"{{ type: mongoose.Schema.Types.ObjectId, ref: '{attr_type}' }}"  # Foreign Key

def write_to_file(path, content):
    """Write content to a file."""
    with open(path, "w") as f:
        f.write(content)
