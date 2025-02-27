from generator.utils import format_attribute

def generate_model(classname, attributes):
    model_code = f"const mongoose = require('mongoose');\n\n"
    model_code += f"const {classname}Schema = new mongoose.Schema({{\n"
    
    for attr_name, attr_type in attributes:
        model_code += f"  {attr_name}: {format_attribute(attr_name, attr_type)},\n"

    model_code = model_code.rstrip(",\n") + "\n"
    model_code += "});\n\n"
    model_code += f"module.exports = mongoose.model('{classname}', {classname}Schema);\n"
    
    return model_code
