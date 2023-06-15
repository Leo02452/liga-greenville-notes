from PIL import Image

def combine_images(img1, img2, saved_image_path):
    img1 = Image.open(img1)
    img2 = Image.open(img2)

    width1, height1 = img1.size
    width2, height2 = img2.size

    combined_img = Image.new('RGB', (width1, height1 + height2))

    combined_img.paste(img1, (0,0))
    combined_img.paste(img2, (0,height1))

    combined_img.save(saved_image_path)