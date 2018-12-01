# Bitmap CLI Transformer


## Authors: Hannah Sindorf, Vince Masten, Joyce Liao

## Overview
This project is a CLI tool which accepts a source and target bitmap file, and, given a specified transformation, will mutate the original images pixel or color values before writing the mutated data to the target file path.

## Getting Started
1. clone repo
1. Navigate to folder bitmap
1. Enter one of the below commands to get started

### return headers
```
get_headers <source>
```
Returns a line-item response of the file's header data.

### transform
```
transform <original> <new> <transform>
```
Creates a new file at 'new' location with the provided 'transform' applied to the new file.
- original - original file's name
- new - new file's name (with extension)
- transform: name of transform:
  - tint_red: tints the image red
  - tint_blue: tints the image blue
  - tint_green: tints the image green
  - lighten: lightens the image
  - darken: darkens the image
  - invert: inverts the image
  - cave: surprise

### get assistance on the CLI
```
help
```

### Quit
```
exit
```


## Changelog:
- 11-29-18: Photo filters backend finished
- 11-30-18: CLI frontend finished
