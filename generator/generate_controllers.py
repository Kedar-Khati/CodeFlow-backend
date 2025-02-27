def generate_controller(classname, apis):
    controller_code = f"const {classname} = require('../models/{classname}.model');\n\n"
    
    if "GET" in apis:
        controller_code += f"exports.get{classname}ById = async (req, res) => {{\n"
        controller_code += f"  try {{\n"
        controller_code += f"    const item = await {classname}.findById(req.params.id);\n"
        controller_code += f"    if (!item) return res.status(404).send('{classname} not found');\n"
        controller_code += f"    res.send(item);\n"
        controller_code += f"  }} catch (err) {{\n"
        controller_code += f"    res.status(500).send('Server error');\n"
        controller_code += f"  }}\n}}\n\n"
    
    if "POST" in apis:
        controller_code += f"exports.create{classname} = async (req, res) => {{\n"
        controller_code += f"  try {{\n"
        controller_code += f"    const newItem = new {classname}(req.body);\n"
        controller_code += f"    await newItem.save();\n"
        controller_code += f"    res.status(201).send(newItem);\n"
        controller_code += f"  }} catch (err) {{\n"
        controller_code += f"    res.status(500).send('Server error');\n"
        controller_code += f"  }}\n}}\n\n"

    if "PUT" in apis:
        controller_code += f"exports.update{classname} = async (req, res) => {{\n"
        controller_code += f"  try {{\n"
        controller_code += f"    const updatedItem = await {classname}.findByIdAndUpdate(req.params.id, req.body, {{ new: true }});\n"
        controller_code += f"    if (!updatedItem) return res.status(404).send('{classname} not found');\n"
        controller_code += f"    res.send(updatedItem);\n"
        controller_code += f"  }} catch (err) {{\n"
        controller_code += f"    res.status(500).send('Server error');\n"
        controller_code += f"  }}\n}}\n\n"
    
    if "GETALL" in apis:
        controller_code += f"exports.getAll{classname}s = async (req, res) => {{\n"
        controller_code += f"  try {{\n"
        controller_code += f"    const items = await {classname}.find();\n"
        controller_code += f"    res.send(items);\n"
        controller_code += f"  }} catch (err) {{\n"
        controller_code += f"    res.status(500).send('Server error');\n"
        controller_code += f"  }}\n}}\n"
    
    return controller_code
