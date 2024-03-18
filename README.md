## Codebase File Search
It's designed to traverse through the codebase, starting from the current directory where the script is executed. It will search through all files, excluding directories that typically contain a large number of irrelevant files for most searches, such as node_modules and .git. When it finds a match for the keyword you specify, it prints out the file path where the match was found. This approach should offer a faster and more focused search compared to using a file explorer's search function, especially for large codebases.

how to use: 
### `python python-search-files-script.py  "Keyword"`
