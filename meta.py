import json

# Load your original dataset
input_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\training_dataset.jsonl'
output_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\magicui.jsonl'

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        data = json.loads(line)
        cleaned_data = {
            "prompt": data["prompt"],
            "completion": data["completion"]
        }
        outfile.write(json.dumps(cleaned_data) + '\n')

print("Cleaned dataset saved to", output_file)
