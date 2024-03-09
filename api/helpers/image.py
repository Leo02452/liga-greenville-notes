from PIL import Image, ImageOps, ImageEnhance
from io import BytesIO

def invert_colors(image_content):
    image = Image.open(BytesIO(image_content))
    r,g,b = image.split()
    rgb_image = Image.merge('RGB', (r,g,b))
    inv_image = ImageOps.invert(rgb_image)
    r2,g2,b2 = inv_image.split()
    inverted_image = Image.merge('RGB', (r2,g2,b2))
    bw_image = ImageOps.grayscale(inverted_image)
    enhacer = ImageEnhance.Contrast(bw_image)
    bw_image = enhacer.enhance(2.5)

    output_buffer = BytesIO()
    bw_image.save(output_buffer, format="PNG")
    return output_buffer.getvalue()

def combine_images(img1, img2):
    img1 = Image.open(BytesIO(img1))
    img2 = Image.open(BytesIO(img2))

    width1, height1 = img1.size
    width2, height2 = img2.size

    combined_img = Image.new('RGB', (width1, height1 + height2))

    combined_img.paste(img1, (0,0))
    combined_img.paste(img2, (0,height1))

    output_buffer = BytesIO()
    combined_img.save(output_buffer, format="PNG")
    return output_buffer.getvalue()
