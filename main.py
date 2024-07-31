from PIL import Image, ImageFont, ImageDraw

# Global Variables
FONT_FILE = ImageFont.truetype(r'resources/font/GreatVibes-Regular.ttf', 360)
FONT_COLOR = "#FFFFFF"

template = Image.open(r'resources/templates/template2.png')
WIDTH, HEIGHT = template.size


def make_certificates(name):
    """Function to save certificates as a .png file"""

    image_source = Image.open(r'resources/templates/template2.png')
    draw = ImageDraw.Draw(image_source)

    # Adding the logo
    logo = Image.open(r'resources/logo/logo.png')
    logo_width, logo_height = logo.size

    # Placing it in the top middle
    logo_position = ((WIDTH - logo_width) // 2, (HEIGHT - logo_height) // 12)
    image_source.paste(logo, logo_position, logo)

    # Finding the bounding box of the text.
    # The 'textsize' method has been deprecated and replaced by the 'textbbox' method in newer versions of Pillow
    bbox = draw.textbbox((0, 0), name, font=FONT_FILE)
    name_width = bbox[2] - bbox[0]
    name_height = bbox[3] - bbox[1]

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./out/" + name + ".png")
    print('Saving Certificate of:', name)


if __name__ == "__main__":

    # names = ['Tushar Nankani', "Full Name", 'Some Long Ass Name Might Not Work']
    names = ['Asib Hossen']
    for name in names:
        make_certificates(name)

    print(len(names), "certificates done.")
