import os

# Define the folder and file structure
structure = {
    "ats_project": {
        "requirements.txt": "",
        "app": {
            "__init__.py": "",
            "config.py": "",
            "utils": {
                "file_handler.py": "",
                "text_extraction.py": "",
                "text_cleaning.py": "",
                "embedding_model.py": "",
                "similarity_scoring.py": "",
                "evaluation.py": "",
                "report_generator.py": ""
            },
            "services": {
                "company_service.py": "",
                "candidate_service.py": ""
            },
            "interface": {
                "company_interface.py": "",
                "candidate_interface.py": ""
            },
            "main.py": ""
        },
        "models": {}
    }
}

# Function to create files and folders recursively
def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(base_path, exist_ok=True)
            file_path = os.path.join(base_path, name)
            with open(file_path, 'w') as f:
                f.write(content)

if __name__ == "__main__":
    create_structure(".", structure)
    print("Project structure created successfully!")
