from PIL import Image, ImageDraw, ImageFont

# Load the image
image = Image.open("sample.jpg")

# Create a drawing context
draw = ImageDraw.Draw(image)

# Define the text properties
font = ImageFont.truetype("ALGER.TTF", 36)
text = "Hello, World!"
text_color = (255, 255, 255)

# Calculate the position to center the text
text_length = draw.textlength(text, font)
x = (image.width - text_length) / 2
y = image.height / 2

# Add text to the image
draw.text((x, y), text, fill=text_color, font=font)

# Save or display the modified image
image.save("output.jpg")