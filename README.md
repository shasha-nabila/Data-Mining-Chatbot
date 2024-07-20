# Leo: A Chatbot on the University of Leeds Official Website

For my data and text mining related module, I've created a chatbot prototype using the Rasa framework and a dataset from [Kaggle](https://www.kaggle.com/datasets/niraliivaghani/chatbot-dataset). The dataset has been fine-tuned to fit the project using the `_convert_json_to_yaml.py` script and some manual tweaks.

## Project Structure

- **.rasa**: Contains configuration and metadata for the Rasa project.
- **actions**: Custom actions for the Rasa chatbot.
- **data**: Training data and datasets used for the project.
- **models**: Trained models and model configurations.
- **tests**: Test cases for the project.
- **config.yml**: Rasa configuration file.
- **credentials.yml**: Contains credentials.
- **domain.yml**: Defines the conversation domain for Rasa.
- **endpoints.yml**: Endpoint configuration for Rasa.
- **_convert_json_to_yaml.py**: Script used to convert the Kaggle dataset into the required format.

## Documentation

The attached PDF (`Documentation.pdf`) provides a detailed overview of the project, including the thought process, implementation details, and the results of the prototype.
