import lzma, base64, os

# ---------------------------------------------------------
# 1. Load your source code (replace "morse.py" if needed)
# ---------------------------------------------------------
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "morse.py")

with open(file_path, "rb") as f:
    original = f.read()

print("Original size:", len(original), "bytes")

# ---------------------------------------------------------
# 2. Compress with LZMA (max preset)
# ---------------------------------------------------------
lzma_max = lzma.compress(original, preset=9)
print("LZMA (preset=9):", len(lzma_max), "bytes")

# ---------------------------------------------------------
# 3. Compress with LZMA + filters (optional)
# ---------------------------------------------------------
filters = [
    {"id": lzma.FILTER_DELTA, "dist": 1},
    {"id": lzma.FILTER_LZMA2, "preset": 9},
]

lzma_filtered = lzma.compress(original, format=lzma.FORMAT_XZ, filters=filters)
print("LZMA + Filters:", len(lzma_filtered), "bytes")

# ---------------------------------------------------------
# 4. Base64 versions (for comparison)
# ---------------------------------------------------------
b64_lzma = base64.b64encode(lzma_max)
b64_filtered = base64.b64encode(lzma_filtered)

print("LZMA + Base64:", len(b64_lzma), "bytes")
print("LZMA + Filters + Base64:", len(b64_filtered), "bytes")

# ---------------------------------------------------------
# 5. Embed raw binary directly (no Base64)
# ---------------------------------------------------------
# Use repr() to generate a Python-safe bytes literal
raw_literal = repr(lzma_max)
print("\nRaw-bytes literal length:", len(raw_literal), "characters")

# ---------------------------------------------------------
# 6. Loader example (executes the decompressed code)
# ---------------------------------------------------------
# Paste the raw_literal into payload_raw if you want a standalone loader
payload_raw = lzma_max  # replace with pasted literal for distribution

decompressed_code = lzma.decompress(payload_raw).decode("utf-8")

print("\nDecompression OK:", decompressed_code[:40], "...")
# exec(decompressed_code)   # uncomment to run the code