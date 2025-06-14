import json

# File paths - use raw strings to avoid Windows path errors
input_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\training_data00.jsonl'
output_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\check.jsonl'

# Read your input dataset
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# This list will hold your improved dataset
new_dataset = []

for line in lines:
    data = json.loads(line)

    # Extract prompt and code exactly as is
    prompt = data['prompt']
    code = data['code']

    # Extract metadata fields if available
    if 'metadata' in data:
        metadata = data['metadata']
        category = metadata.get('category', '')
        tags = ', '.join(metadata.get('tags', []))
        colors = ', '.join(metadata.get('colors', []))

        # Create metadata string to append to prompt
        metadata_string = f"\n\nAdditional Details:\nCategory: {category}\nTags: {tags}\nColors: {colors}"
    else:
        metadata_string = ""

    # Combine prompt and metadata
    enhanced_prompt = prompt + metadata_string

    # Save both prompt and code as required
    new_dataset.append({
        'prompt': enhanced_prompt,
        'code': code
    })

# Write the improved dataset to a new file
with open(output_file, 'w', encoding='utf-8') as f:
    for item in new_dataset:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f"✅ Dataset cleaned and saved to {output_file}")
