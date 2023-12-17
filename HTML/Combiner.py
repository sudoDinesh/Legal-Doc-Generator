import os

# Define the folder path where your HTML files are located
folder_path = 'HTML'

# Create an output text file to store the combined content
output_file_path = 'combined_html.txt'

# Initialize an empty string to store the combined content
combined_content = ""

# List all HTML files in the specified folder
html_files = [file for file in os.listdir(folder_path) if file.endswith('.html')]

# Iterate through each HTML file and append its content to the combined_content
for html_file in html_files:
    with open(os.path.join(folder_path, html_file), 'r', encoding='utf-8') as file:
        file_content = file.read()
        combined_content += f"===== {html_file} =====\n"
        combined_content += file_content + '\n'

# Write the combined content to the output text file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(combined_content)

print("HTML files combined and saved to", output_file_path)