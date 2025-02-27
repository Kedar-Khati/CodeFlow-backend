import json

def generate_manual(json_data):
    manual = ""
    
    for cls in json_data:
        classname = cls['classname']
        apis = cls['apis']
        attributes = cls['attributes']
        
        manual += f"\n{classname} API Endpoints\n"
        
        for api in apis:
            if api == "GET":
                manual += f"- GET /{classname}/:id\n"
            elif api == "POST":
                manual += f"- POST /{classname} (Body: {json.dumps(dict(attributes), indent=4)})\n"
            elif api == "PUT":
                manual += f"- PUT /{classname}/:id (Body: {json.dumps(dict(attributes), indent=4)})\n"
            elif api == "GETALL":
                manual += f"- GETALL /{classname}/all\n"

    return manual
