from PIL import Image, ImageDraw, ImageFont

# Dimensions in centimeters, convert to pixels (1 cm ≈ 37.7953 pixels at 96 dpi)
dpi = 96  # Adjust if needed for your printer's resolution
cm_to_pixels = lambda cm: int(cm * 37.7953)
canvas_width = 241 #px
canvas_height = cm_to_pixels(8.89)

def wrap_text(draw, text, font, max_width):
    """Wrap text to fit within a given width."""
    words = text.split()
    lines = []
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

    lines.append(current_line)
    return lines

def create_card_image( card ):
    name = card['name']
    file_name = "./images/" + name + ".jpg"
    img = card['img']
    text = card['oracle_text'].split('\n')

    # downscale
    target_height = canvas_height // 3
    print(canvas_height)
    img = img.resize((canvas_width-50, target_height), Image.Resampling.LANCZOS)

    # Create a blank canvas
    canvas = Image.new("RGB", (canvas_width, canvas_height), "white")

    # Paste the image onto the top third of the canvas
    canvas.paste(img, (23, 25))

    # Add text to the bottom two-thirds
    draw = ImageDraw.Draw(canvas)
    
    # Load a font (you might need to specify the font path)
    try:
        font = ImageFont.truetype("arial.ttf", size=10)  # Use a common font
    except IOError:
        font = ImageFont.load_default()  # Fallback to default font

    ### text

    # Card Name
    draw.text((3,3), name, fill="black",font=font )

    # Define the text area
    text_area_top = target_height
    text_area_height = canvas_height - target_height
    text_area_width = canvas_width

    # Card Type
    draw.text((3,text_area_top+30), card['type_line'], fill="black",font=font )

    # Card Colors
    # colors = "Colors: " + card['colors']
    # draw.text((3,canvas_height -5), colors, fill="black",font=font )
    

    # Pow/Tough
    pow_tou = "" + card['power'] + '/' + card['toughness']
    draw.text((canvas_width-25,canvas_height -15), pow_tou, fill="black",font=font )

    wrapped_text = wrap_text(draw, text, font, text_area_width)
    # Draw each line of text
    y = text_area_top +45
    for line in wrapped_text:
        draw.text((3, y), line, fill="black", font=font)
        y += font.size + 5  # Adjust line spacing


    # # Format and center the text
    # lines = text.split("\n")  # Split text into lines if needed
    # line_height = text_area_height // (len(lines) + 1)

    # y = text_area_top + (line_height // 2)
    # for line in lines:
    #     bbox = draw.textbbox((0, 0), line, font=font)
    #     text_width = bbox[2] - bbox[0]  # Calculate text width
    #     x = (text_area_width - text_width) // 2  # Center align horizontally
    #     draw.text((x, y), line, fill="black", font=font)
    #     y += line_height

    # Save the final image
    canvas.save(file_name)
    print(f"Image saved at {file_name}")

