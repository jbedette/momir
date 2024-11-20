import cups
import os

def print_image(image_path, printer_name=None):
    # Ensure the image file exists
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        return

    # Connect to the CUPS server
    conn = cups.Connection()

    # Get a list of available printers
    printers = conn.getPrinters()

    # Use the specified printer or the default printer
    if printer_name and printer_name in printers:
        printer = printer_name
    else:
        printer = conn.getDefault()
        if not printer:
            print("No default printer found. Specify a printer name.")
            return

    print(f"Printing on printer: {printer}")

    # Print the image file
    try:
        job_id = conn.printFile(printer, image_path, "Python Image Print Job", {})
        print(f"Job submitted. Job ID: {job_id}")
    except cups.IPPError as e:
        print(f"Failed to print. Error: {e}")

# Example usage
if __name__ == "__main__":
    # Path to the image file you want to print
    image_path = "/path/to/your/image.jpg"
    
    # Replace 'printer_name' with your printer's name or leave it as None for default
    printer_name = None  # e.g., "HP_LaserJet"
    
    print_image(image_path, printer_name)
