def generate_routes(classname, apis):
    routes_code = f"const express = require('express');\n"
    routes_code += f"const router = express.Router();\n"
    routes_code += f"const {classname}Controller = require('../controllers/{classname}.controller');\n\n"

    if "GET" in apis:
        routes_code += f"router.get('/{classname}/:id', {classname}Controller.get{classname}ById);\n"
    
    if "POST" in apis:
        routes_code += f"router.post('/{classname}', {classname}Controller.create{classname});\n"

    if "PUT" in apis:
        routes_code += f"router.put('/{classname}/:id', {classname}Controller.update{classname});\n"
    
    if "GETALL" in apis:
        routes_code += f"router.get('/{classname}/', {classname}Controller.getAll{classname}s);\n"

    routes_code += f"\nmodule.exports = router;\n"
    
    return routes_code
