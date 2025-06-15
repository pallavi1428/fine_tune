import json

# Path to your input and output files
input_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\acternityui_comps.jsonl'
output_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\acternity.jsonl'

# Process the JSONL file
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        data = json.loads(line)

        # Keep only prompt and completion
        cleaned_data = {
            "prompt": data.get("prompt", ""),
            "completion": data.get("completion", ""),
            "source": "aceternity ui"  # Add the source field
        }

        # Write to output file
        outfile.write(json.dumps(cleaned_data, ensure_ascii=False) + '\n')

print("✅ Cleaning completed. Output saved to:", output_file)
