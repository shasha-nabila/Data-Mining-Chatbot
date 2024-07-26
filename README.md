# Leo: A Chatbot on the University of Leeds Official Website

For my data and text mining related module, I've created a chatbot prototype using the **Rasa framework** and a dataset from [Kaggle](https://www.kaggle.com/datasets/niraliivaghani/chatbot-dataset). The initial step involved extracting this JSON-format dataset, which contained a collection of potential user queries and their corresponding responses. The dataset was chosen for its relevance to common inquiries prospective students might make on the University of Leeds website. To make this dataset compatible with the Rasa framework, the `convert_json_to_yaml.py` script was utilized to transform the JSON data into the YAML format. This conversion was crucial as Rasa's training process requires data in YAML format to define intents, entities, and corresponding examples effectively. Additionally, **SpaCy**, a powerful data mining and natural language processing tool, was integrated to enhance the chatbot's ability to understand and respond to user inputs accurately through entity recognition and POS-tagging. The dataset has been fine-tuned with some manual tweaks to fit the project requirements.
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
- **convert_json_to_yaml.py**: Script used to convert the Kaggle dataset into the required format.

## Documentation

The attached PDF (`Documentation.pdf`) provides a detailed overview of the project, including the thought process, implementation details, and the results of the prototype.
