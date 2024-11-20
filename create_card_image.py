from PIL import Image, ImageDraw, ImageFont

# Dimensions in centimeters, convert to pixels (1 cm ≈ 37.7953 pixels at 96 dpi)
dpi = 96  # Adjust if needed for your printer's resolution
cm_to_pixels = lambda cm: int(cm * 37.7953)
canvas_width = 241  # px
canvas_height = cm_to_pixels(8.89)


def wrap_text(draw, text, font, max_width):
    paragraphs = text.split("\n")  # Split into paragraphs by newline characters
    lines = []

    for paragraph in paragraphs:
        words = paragraph.split()
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            bbox = draw.textbbox((0, 0), test_line, font=font)
            text_width = bbox[2] - bbox[0]

            if text_width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        # Append the final line of the paragraph
        if current_line:
            lines.append(current_line)

        # Add an empty line for the newline character, preserving paragraph breaks
        lines.append("")

    # Remove the trailing empty line added by the last paragraph
    if lines and lines[-1] == "":
        lines.pop()

    return lines


def draw_oracle_text(draw, text, max_width, max_height, buffer, font_path, initial_font_size):
    # Start with the initial font size
    font_size = initial_font_size
    while font_size > 1:
        # Load the font with the current size
        try:
            font = ImageFont.truetype(font_path, size=font_size)
        except IOError:
            font = ImageFont.load_default()

        # Wrap the text and calculate the total height
        wrapped_text = wrap_text(draw, text, font, max_width)
        text_height = sum(draw.textbbox((0,0),line,font=font)[3] + 5 for line in wrapped_text)  # Line height + spacing

        # Check if the wrapped text fits within the text area
        if text_height + buffer <= max_height:
            return wrapped_text, font

        # Reduce font size and try again
        font_size -= 1

    # Fallback to the smallest font if no size fits
    return wrap_text(draw, text, font, max_width), font


def create_card_image(card, output_dest):
    # Card variables
    name = card.get("name", "default")
    file_name = f"{output_dest}{name}.jpg"
    img = card.get("img")
    text = card.get("oracle_text", "")
    mana_cost = card.get("mana_cost", "")
    power = card.get("power", "")
    toughness = card.get("toughness", "")
    pow_tou = f"{power}/{toughness}" if power and toughness else ""
    type_line = card.get("type_line", "")

    # Downscale the image
    target_height = canvas_height // 3
    img = img.resize((canvas_width - 50, target_height), Image.Resampling.LANCZOS)

    # Create a blank canvas
    canvas = Image.new("RGB", (canvas_width, canvas_height), "white")

    # Paste the image onto the top third of the canvas
    canvas.paste(img, (23, 35))

    # Add text to the bottom two-thirds
    draw = ImageDraw.Draw(canvas)

    # Load font
    font_path = "arial.ttf"
    try:
        font = ImageFont.truetype(font_path, size=10)  # Normal font
    except IOError:
        font = ImageFont.load_default()

    # Card Name
    draw.text((3, 3), name, fill="black", font=font)

    # Card Mana Cost
    draw.text((3, 13), mana_cost, fill="black", font=font)

    # Define text area dimensions
    text_area_top = target_height
    text_area_height = canvas_height - target_height
    text_area_width = canvas_width

    # Card Type
    draw.text((3, text_area_top + 40), type_line, fill="black", font=font)

    # Power/Toughness
    draw.text((canvas_width - 27, canvas_height - 15), pow_tou, fill="black", font=font)

    # Oracle Text
    wrapped_text, oracle_font = draw_oracle_text(
        draw=draw,
        text=text,
        max_width=text_area_width - 6,  # Small margin for text alignment
        max_height=text_area_height - 20,  # Leave a 20-pixel buffer
        buffer=20,
        font_path=font_path,
        initial_font_size=10,
    )

    # Draw oracle text
    y = text_area_top + 55
    for line in wrapped_text:
        bbox = draw.textbbox((0, 0), line, font=oracle_font)  # Get bounding box for the line
        line_height = bbox[3] - bbox[1]  # Calculate line height
        draw.text((3, y), line, fill="black", font=oracle_font)
        y += line_height + 5  # Line height + spacing

    # Save the final image
    canvas.save(file_name)
    print(f"Image saved at {file_name}")
    # return canvas,file_name
    return file_name
