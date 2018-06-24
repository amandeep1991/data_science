import os
os.chdir("F:\\kvch\\Final Presentations")
from rasa_nlu.training_data import load_data
training_data = load_data("training_data.json")
import json
print(json.dumps(training_data.training_examples[22].as_dict(), indent=2))