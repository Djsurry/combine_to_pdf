# Combine to pdf
Takes a series of images and combines them into 1 pdf file and then compresses that file.

## Setup steps
1. Install requirements 

> `brew install jpegoptim` and `brew install imagemagick` for mac

> `sudo apt-get install jpegoptim` and `sudo apt-get install imagemagick` for linux

2. Name images to be combined `1.JPG`, `2.JPG`, ... , `N.JPG`. Acceptable file extensions are
- `JGP`
- `PNG`
- `JPEG`

## Usage
`python combine_to_pdf.py <output_filename> -d <dpi>`
- `output_filename` is the name of the pdf that will be created. Required
- `-d` is the dpi, a level of compression where lower is more compressed. By default it is 30. Optional

## Notes
I did not write the shell script, I found it [here](http://www.alfredklomp.com/programming/shrinkpdf/).
