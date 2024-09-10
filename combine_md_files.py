import os

def combine_md_files(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(folder_path):
            if filename.endswith('.md'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(f"# Content from {filename}\n\n")
                    outfile.write(infile.read())
                    outfile.write("\n\n---\n\n")  # Separator between files
    print(f"Combined Markdown files into {output_file}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    output_file = input("Enter the output file name (e.g., combined.md): ")
    combine_md_files(folder_path, output_file)