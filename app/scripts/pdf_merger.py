from PyPDF2 import PdfMerger
import os

# Function to merge multiple PDF files into a single PDF
def merge_pdfs(input_files, output_file):
    merger = PdfMerger()

    # Merge each input file into the output file
    for file in input_files:
        merger.append(file)

    # Write the merged PDF to the output file
    merger.write(output_file)
    merger.close()


# Function to get a list of file names in a directory
def get_file_names(directory):
    file_names = []

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_names.append(os.path.join(directory, filename))

    file_names.sort()

    return file_names

# Main entry point
if __name__ == "__main__":
    # Specify the directory to read file names from
    directory = "enter directory path here"

    for dir in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, dir)):
            print(f"Merging PDF files in directory: {dir}")

            # Get the list of file names
            files = get_file_names(os.path.join(directory, dir))

            # Print the file names
            for file in files:
                print(file)

            # Specify the output file to save the merged PDF
            output_file = dir + ".pdf"

            merge_pdfs(files, output_file)
