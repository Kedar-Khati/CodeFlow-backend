import os
import zipfile
from generator.generate_models import generate_model
from generator.generate_controllers import generate_controller
from generator.generate_routes import generate_routes
from generator.generate_manual import generate_manual
from generator.utils import ensure_directories, write_to_file


# Sample input
# json_data = [
#     {
#         "classname": "classA",
#         "classId": "1",
#         "attributes": [("id", "string"), ("quantity", "int")],
#         "apis": ["GET", "POST"]
#     },
#     {
#         "classname": "classB",
#         "classId": "2",
#         "attributes": [("id", "string"), ("class_id", "classA")],
#         "apis": ["POST", "GETALL", "PUT"]
#     }
# ]

def generate_backend(json_data):
    ensure_directories()

    for cls in json_data:
        classname = cls['classname']
        attributes = cls['attributes']
        apis = cls['apis']

        write_to_file(f"output/models/{classname}.model.js", generate_model(classname, attributes))
        write_to_file(f"output/controllers/{classname}.controller.js", generate_controller(classname, apis))
        write_to_file(f"output/routes/{classname}.routes.js", generate_routes(classname, apis))

    write_to_file("output/manual.txt", generate_manual(json_data))

    # Create a zip file
    zip_filename = "output/backend_files.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk("output"):
            for file in files:
                if file != "backend_files.zip":  # Avoid zipping the zip file itself
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), "output"))

    return zip_filename

if __name__ == "__main__":
    zip_filename = generate_backend(json_data)
    print(f"✅ Backend files generated and zipped in '{zip_filename}'.")