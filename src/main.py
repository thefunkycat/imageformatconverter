from PIL import Image
import argparse
import os
import pyheif

parser = argparse.ArgumentParser(description="CLI Image Format Converter")
parser.add_argument("input_file", help="Input image file")
parser.add_argument("output_file", help="Output image file")
parser.add_argument("-f", "--format", help="Output image format (e.g., JPEG, PNG, HEIC)")
parser.add_argument("-q", "--quality", help="Output image quality")
args = parser.parse_args()

input_image = Image.open(args.input_file)
output_format = args.format if args.format else os.path.splitext(args.output_file)[1].lstrip('.')
quality = args.quality if args.quality else 85 # default value

if output_format == "HEIC":
    heif_image = pyheif.read(args.input_file)
    image = Image.frombytes(
        heif_image.mode, heif_image.size, heif_image.data,
        "raw", heif_image.mode, heif_image.stride,
    )
    image.save(args.output_file, format="HEIC", quality=85)  # HEIC quality setting

elif output_format in ["JPEG", "PNG", "GIF"]:
    input_image.save(args.output_file, format=output_format)
    print(f"Image converted and saved as {args.output_file} in {output_format} format")

else:
    print("Unsupported output format")
