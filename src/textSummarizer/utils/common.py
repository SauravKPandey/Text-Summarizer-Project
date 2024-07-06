import os
import sys
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """Reads YAML file and returns 
    Args: path_to_yaml: path like input
    Raises: 
            ValueError: if yaml is empty
            e: empty file
    Returns: ConfigBox: ConfigBox type
    """
    try: 
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file : {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError :
        raise ValueError("yaml file is empty")
    except Exception as e :
        raise e

@ensure_annotations
def create_directories(path_to_directory: list, verbose=True):
    """Creates list of directories
    
    Args: path_to_directory: list of paths to directories
          ignore_log(bool, optional):ignore if multiple directories is to be created
          """
    for path in path_to_directory:
        path = Path(path)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            if verbose:
                logger.info(f"Directory created : {path}")
        else:
            if verbose:
                logger.info(f"Directory already exists : {path}")

@ensure_annotations
def get_size(path:Path)-> str:
    """Returns size of file
    
    Args: path: path to file
    Returns: str: size of file in kb
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"


