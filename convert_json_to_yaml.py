import json
import yaml

# Load your JSON data
with open('C:/Users/DELL/Downloads/UOL Programming Projects/Spring 2024/Data Mining/leo/data/intents.json', 'r') as json_file:
    data = json.load(json_file)

# Prepare the structure for YAML
nlu_data = {'nlu': []}
responses = {'responses': {}}

for intent_data in data['intents']:
    # Add examples for each intent
    examples_text = "\n".join(f"- {example}" for example in intent_data['patterns'])
    nlu_data['nlu'].append({'intent': intent_data['tag'], 'examples': f"|\n{examples_text}"})

    # Add responses for each intent
    response_key = f"utter_{intent_data['tag']}"
    responses['responses'][response_key] = [{'text': response} for response in intent_data['responses']]

# Combine data
rasa_data = {**nlu_data, **responses}

# Write to YAML
with open('C:/Users/DELL/Downloads/UOL Programming Projects/Spring 2024/Data Mining/leo/data/nlu.yml', 'w') as yaml_file:
    yaml.dump(rasa_data, yaml_file, allow_unicode=True)

print("Conversion complete. Data saved to 'converted_rasa_data.yml'")