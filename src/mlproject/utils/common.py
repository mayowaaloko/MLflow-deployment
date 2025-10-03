import os
from box.exceptions import BoxValueError
from src.mlproject import logger
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Raises:
        e: BoxValueError if the yaml file is empty

    Returns:
        ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise BoxValueError("yaml file is empty")
    except Exception as e:
        logger.exception(f"Error occurred while reading yaml file: {e}")
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates list of directories

    Args:
        path_to_directories (list): List of directories to be created
        verbose (bool, optional): Whether to log info messages. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary to a json file

    Args:
        path (Path): Path to the json file
        data (dict): Data to be saved
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a json file and returns a ConfigBox object

    Args:
        path (Path): Path to the json file

    Returns:
        ConfigBox: ConfigBox object
    """
    with open(path, "r") as json_file:
        content = json.load(json_file)
    logger.info(f"json file loaded from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data to a binary file using joblib

    Args:
        data (Any): Data to be saved
        path (Path): Path to the binary file
    """
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib

    Args:
        path (Path): Path to the binary file

    Returns:
        Any: Data loaded from the binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of a file

    Args:
        path (Path): Path to the file

    Returns:
        str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"{size_in_kb} KB"
