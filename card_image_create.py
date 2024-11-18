from PIL import Image, ImageDraw, ImageFont

# Dimensions in centimeters, convert to pixels (1 cm ≈ 37.7953 pixels at 96 dpi)
dpi = 96  # Adjust if needed for your printer's resolution
cm_to_pixels = lambda cm: int(cm * 37.7953)
canvas_width = cm_to_pixels(6.35)
canvas_height = cm_to_pixels(8.89)

def create_custom_image(input_image_path, output_image_path, text):
    # Load and downscale the input image
    img = Image.open(input_image_path)
    target_height = canvas_height // 3
    img = img.resize((canvas_width, target_height), Image.ANTIALIAS)

    # Create a blank canvas
    canvas = Image.new("RGB", (canvas_width, canvas_height), "white")

    # Paste the image onto the top third of the canvas
    canvas.paste(img, (0, 0))

    # Add text to the bottom two-thirds
    draw = ImageDraw.Draw(canvas)
    
    # Load a font (you might need to specify the font path)
    try:
        font = ImageFont.truetype("arial.ttf", size=20)  # Use a common font
    except IOError:
        font = ImageFont.load_default()  # Fallback to default font

    # Define the text area
    text_area_top = target_height
    text_area_height = canvas_height - target_height
    text_area_width = canvas_width

    # Format and center the text
    lines = text.split("\n")  # Split text into lines if needed
    line_height = text_area_height // (len(lines) + 1)

    y = text_area_top + (line_height // 2)
    for line in lines:
        text_width, _ = draw.textsize(line, font=font)
        x = (text_area_width - text_width) // 2  # Center align
        draw.text((x, y), line, fill="black", font=font)
        y += line_height

    # Save the final image
    canvas.save(output_image_path)
    print(f"Image saved at {output_image_path}")

# Example usage
create_custom_image(
    input_image_path="input.jpg",       # Path to your input image
    output_image_path="output.jpg",    # Path to save the output
    text="Your text here\nAnother line of text"  # Text for the bottom 2/3
)
