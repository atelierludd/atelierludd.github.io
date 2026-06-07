from PIL import Image
from pathlib import Path
import sys

input_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("IMG_TO_COMPRESS")
quality = int(sys.argv[2]) if len(sys.argv) > 2 else 85

output_dir = Path("IMG")
output_dir.mkdir(exist_ok=True)

tifs = list(input_dir.glob("*.tif")) + list(input_dir.glob("*.tiff"))

if not tifs:
    print("Aucun fichier .tif trouvé.")
    sys.exit()

for tif in tifs:
    out = output_dir / tif.with_suffix(".webp").name
    img = Image.open(tif)
    img.save(out, "WEBP", quality=quality)
    print(f"{tif.name} -> {out.name} ({out.stat().st_size // 1024} KB)")

print(f"\n{len(tifs)} fichier(s) convertis.")
