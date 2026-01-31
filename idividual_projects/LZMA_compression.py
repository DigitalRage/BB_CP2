import lzma

# Data to compress
data = b""""""
# Compress
compressed_data = lzma.compress(data)
print(f"Original size: {len(data)} bytes")
print(f"Compressed size: {len(compressed_data)} bytes")

# Decompress
decompressed_data = lzma.decompress(compressed_data)
print(f"Decompressed matches original: {decompressed_data == data}")