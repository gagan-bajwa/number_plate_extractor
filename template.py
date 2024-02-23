import os
from pathlib import Path 

project_name = 'ANPR'

project_files_list = [
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/components/data_ingestion.py',
    f'src/{project_name}/components/data_transformation.py',
    f'src/{project_name}/components/model_trainer.py',
    f'src/{project_name}/components/model_pusher.py',
    f'src/{project_name}/components/prepare_base_model.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/logger/__init__.py',
    f'src/{project_name}/exception/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    'app.py'
]

for path in project_files_list:
    path = Path(path)
    file_dir,file_name = os.path.split(path)

    if file_dir!='':
        os.makedirs(file_dir,exist_ok=True)

    if (not os.path.exists(path)) or (os.path.getsize()==0):
        with open(path,'w') as f:
            pass
