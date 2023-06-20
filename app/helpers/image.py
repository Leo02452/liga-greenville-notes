from PIL import Image, ImageOps

def invert_colors(image_path, inverted_image_path):
    image = Image.open(image_path)
    r,g,b = image.split()
    rgb_image = Image.merge('RGB', (r,g,b))
    inv_image = ImageOps.invert(rgb_image)
    r2,g2,b2 = inv_image.split()
    inverted_image = Image.merge('RGB', (r2,g2,b2,))
    inverted_image.save(inverted_image_path)

def combine_images(img1, img2, saved_image_path):
    img1 = Image.open(img1)
    img2 = Image.open(img2)

    width1, height1 = img1.size
    width2, height2 = img2.size

    combined_img = Image.new('RGB', (width1, height1 + height2))

    combined_img.paste(img1, (0,0))
    combined_img.paste(img2, (0,height1))

    combined_img.save(saved_image_path)