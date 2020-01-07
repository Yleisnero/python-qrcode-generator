# python-qrcode-generator

QR-Code Generator for numeric QR-Codes in Python

Using python-qrcode: https://pypi.org/project/qrcode & https://github.com/lincolnloop/python-qrcode 

## Usage
- Clone or download the python-qrcode-generator repository
- Open your Terminal and change your working directory to the directory where you want to generate your QRCodes
- Run the generate_qrcodes.py file with your arguments

## Arguments
|  Argument  |             Description            | Position |
|:----------:|:----------------------------------:|:--------:|
|  File Type |        Can be "png" or "svg"       |     1    |
|    First   |         First QRCode number        |     2    |
|    Last    |         Last QRCode number         |     3    |
| [Box Size] | Box Size for the generated QRCodes |     4    |
- The default Box Size is is 10 (== 1mm per rectangle)

## Examples
### Generate QRCodes for the numbers 1 to 10 as pngs
```
python3 generate_qrcodes.py "png" 1 10
```
### Generate a QRCode for the numbers 42 as svg
```
python3 generate_qrcodes.py "svg" 42 42
```
### Generate QRCodes for the numbers 1111 to 2222 as pngs with a box size of 42
```
python3 generate_qrcodes.py "png" 1111 2222 42
```
### Generate QRCodes from other directory
```
python3 storehere/python-qrcode-generator/generate_qrcodes.py "png" 1 10
```
The QRCodes are going to be stored in your current directory e.g. storehere/
