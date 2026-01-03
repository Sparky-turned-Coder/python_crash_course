# =======================
# File Extensions

# Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to
#   a variable called filename. Then use the removesuffix() method to display the filename without the file
#   extension, like some file browsers do.

filename, filenameTwo, filenameThree = (
    "python_notes.txt\n",
    "golang_notes.txt\n",
    "typescript_notes.txt\n",
)


print(
    filename.removesuffix(".txt"),
    filenameTwo.removesuffix(".txt"),
    filenameThree.removesuffix(".txt"),
)
