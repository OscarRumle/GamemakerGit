import struct
import zlib

def create_png(width, height, pixels, filename):
    """Create a simple PNG file"""
    def png_chunk(chunk_type, data):
        chunk = chunk_type + data
        return struct.pack('>I', len(data)) + chunk + struct.pack('>I', zlib.crc32(chunk) & 0xffffffff)

    # PNG signature
    png_signature = b'\x89PNG\r\n\x1a\n'

    # IHDR chunk
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)  # 6 = RGBA

    # IDAT chunk (image data)
    raw_data = b''
    for row in pixels:
        raw_data += b'\x00'  # Filter type 0 (None)
        raw_data += row

    idat_data = zlib.compress(raw_data, 9)

    # IEND chunk
    iend = png_chunk(b'IEND', b'')

    # Write PNG file
    with open(filename, 'wb') as f:
        f.write(png_signature)
        f.write(png_chunk(b'IHDR', ihdr))
        f.write(png_chunk(b'IDAT', idat_data))
        f.write(iend)

# Create normal button (blue background, white text area)
width, height = 200, 60
pixels_normal = []
for y in range(height):
    row = b''
    for x in range(width):
        # Blue button background
        row += bytes([70, 130, 180, 255])  # RGBA
    pixels_normal.append(row)

create_png(width, height, pixels_normal, 'Blank Pixel Game_1/sprites/spr_button/0.png')

# Create hover button (lighter blue)
pixels_hover = []
for y in range(height):
    row = b''
    for x in range(width):
        # Lighter blue for hover
        row += bytes([100, 160, 210, 255])  # RGBA
    pixels_hover.append(row)

create_png(width, height, pixels_hover, 'Blank Pixel Game_1/sprites/spr_button/1.png')

print("Button sprites created successfully!")
