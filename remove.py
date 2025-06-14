import json

input_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\training_data00.jsonl'
output_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\training_dataset.jsonl'

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        data = json.loads(line)
        for key in ["original_filename", "screenshot", "path"]:
            data.get('metadata', {}).pop(key, None)
        json.dump(data, outfile, ensure_ascii=False)
        outfile.write('\n')

print("Cleaned file saved as:", output_file)
