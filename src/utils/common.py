# reading content of a yaml file
import yaml


def read_yml(yml_filepath):
    with open(yml_filepath, 'r') as file:
        content_dict = yaml.safe_load(file)
        
    return content_dict