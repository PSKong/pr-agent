import os
import json

def extract_text_from_log(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) > 1:
            data = json.loads(lines[1].strip())  # Convert the second line to JSON
            data1 = json.loads(lines[0].strip())
            pr_url = data1['record']['extra']['pr_url']

            return data.get('text', ''),pr_url
        return None

def main(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.log'):
            file_path = os.path.join(folder_path, filename)
            text_content,pr_url = extract_text_from_log(file_path)
            if text_content:
                md_filename = f"{os.path.splitext(filename)[0]}.md"
                md_file_path = os.path.join(folder_path, md_filename)
                with open(md_file_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(f"# Text from {filename},{pr_url}\n\n")
                    md_file.write(text_content)
                    
                print(f"Extracted text from {filename} to {md_filename}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    main(folder_path)