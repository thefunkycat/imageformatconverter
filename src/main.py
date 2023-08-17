from PIL import Image
import argparse
import os
import pillow_heif

# Register Pillow HEIF opener
pillow_heif.register_heif_opener()

# Define input arguments
parser = argparse.ArgumentParser(description="CLI Image Format Converter")
parser.add_argument("input_file", help="Input image file")
parser.add_argument("output_file", help="Output image file")
parser.add_argument("-of", "--oformat", help="Output image format (e.g., JPEG, PNG, HEIC)")
parser.add_argument("-if", "--iformat", help="Input image format (e.g., JPEG, PNG, HEIC)")
parser.add_argument("-q", "--quality", help="Output image quality")
args = parser.parse_args()

# Parse and store input arguments
output_format = (args.oformat if args.oformat else os.path.splitext(args.output_file)[1].lstrip('.')).upper()
quality = args.quality if args.quality else 85 # default value
input_format = (args.iformat if args.iformat else os.path.splitext(args.input_file)[1].lstrip('.')).upper()
output_file = args.output_file
input_file = args.input_file

# in the future, work on creating and saving it in local env and returning the path to it, or specifying directory for output to be saved and saving there

if output_format in ["HEIC", "HEIF"]:

    if input_format in ["JPG", "JPEG", "PNG"]:
        input_image = Image.open(input_file)
        heif_file = pillow_heif.from_bytes(
                        mode = input_image.mode,
                        size = input_image.size,
                        data = input_image.tobytes())
        heif_file.save(output_file, quality=quality)

    elif input_format in ["HEIF", "HEIF"]:
        print("Image already in " + input_format)


elif output_format in ["JPEG", "PNG", "GIF", "JPG"]:

    if input_format in ["JPEG", "PNG", "GIF", "JPG"]:  
        input_image = Image.open(input_file)
        input_image.save(output_file, format=output_format, quality=quality)

    elif input_format in ["HEIC", "HEIF"]:
        heif_file = pillow_heif.open_heif(args.input_file)
        output_image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)
        output_image.save(output_file, format=output_format, quality=quality) 
        
else:
    print("Unsupported output format")

print("Image successfully converted from " + input_format + " to " + output_format + " and saved here: " + output_file)
