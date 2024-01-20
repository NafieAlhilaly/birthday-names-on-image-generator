import arabic_reshaper
from bidi.algorithm import get_display
import sys
from PIL import Image, ImageDraw, ImageFont

IMAGE_NAME_AR = "templates/Happy birthday Poster Arabic.png"
IMAGE_NAME_EN = "templates/Happy birthday Poster English.png"
FONT_NAME = "font.ttf"
FONT_SIZE = 120
FONT_COLOR = (36, 160, 201)

if len(sys.argv) < 2:
    raise Exception("No arguments provided")

en_name = sys.argv[1]
ar_name = sys.argv[2]

# Load images
img_ar = Image.open(IMAGE_NAME_AR)
img_en = Image.open(IMAGE_NAME_EN)
text_start_position_x = (img_ar.width / 2) + 170
text_ar_start_position_x = img_ar.width - 130
text_start_position_y = (img_ar.height / 4) + 120


# process images
I1 = ImageDraw.Draw(img_en)
I1.font = ImageFont.truetype(FONT_NAME, FONT_SIZE, encoding="utf-8")
I1.text((text_start_position_x, text_start_position_y), en_name, fill=FONT_COLOR)
I2 = ImageDraw.Draw(img_ar)
text = get_display(arabic_reshaper.reshape(ar_name), base_dir="R")
arabic_font = ImageFont.truetype(FONT_NAME, FONT_SIZE, encoding="utf-8")
arabic_text_length = I2.textlength(text, font=arabic_font, font_size=FONT_SIZE)
I2.font = arabic_font
I2.text(
    (text_ar_start_position_x - arabic_text_length, text_start_position_y),
    text,
    fill=FONT_COLOR,
)


img_ar.save("img_ar_output.png")
img_en.save("img_en_output.png")
img_ar.close()
img_en.close()
