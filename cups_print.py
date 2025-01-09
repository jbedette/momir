# import cups
from PIL import Image
def print_img(image_path):
    print(f"{image_path}")
    # try:
    #     # Open the image
    #     image = Image.open(image_path)
        
    #     # Rotate the image 90 degrees
    #     rotated_image = image.rotate(90, expand=True)
        
    #     # Save the rotated image temporarily
    #     temp_image_path = "/tmp/rotated_image.jpg"
    #     rotated_image.save(temp_image_path, "JPEG")
        
    #     # Connect to the CUPS server
    #     # conn = cups.Connection()
        
    #     # Print the image using the specified printer
    #     # job_id = conn.printFile(printer_name, temp_image_path, "Rotated Image Print", {})
        
    #     print(f"Image sent to printer '{printer_name}' with job ID {job_id}.")
    
    # except Exception as e:
    #     print(f"An error occurred: {e}")

