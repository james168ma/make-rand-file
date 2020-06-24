# make-rand-file
A command line tool that makes a file of random characters of a specified size

```
usage: make-rand-file [OPTION]... SIZE

Make a random file of printable characters of size SIZE

positional arguments:
  SIZE                  size of file in bytes

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        write contents into OUTPUT_FILE
  -K, --kilobytes       SIZE is in terms of kilobytes
  -M, --megabytes       SIZE is in terms of megabytes
  -d, --digits          file of only random digits
  -L, --letters         file of only random letters
  -u, --uppercase       file of only uppercase letters
  -l, --lowercase       file of only lowercase letters
  -p, --punctuation     file of only punctuation characters
```
