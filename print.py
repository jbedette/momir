import cups

def print_file(filepath, printer_name=None):
    """
    Submits a file to a CUPS printer for printing.

    Args:
        filepath (str): Path to the file to be printed.
        printer_name (str, optional): Name of the printer to use. If None, the default printer is used.

    Raises:
        ValueError: If no default printer is set or the specified printer does not exist.
        Exception: For other errors during the print request.
    """
    try:
        # Connect to the CUPS server
        conn = cups.Connection()

        # Get the list of available printers
        printers = conn.getPrinters()

        if printer_name is None:
            # If no printer name is provided, use the default printer
            printer_name = conn.getDefault()
            if not printer_name:
                raise ValueError("No default printer set. Please specify a printer name.")

        if printer_name not in printers:
            raise ValueError(f"Printer '{printer_name}' not found. Available printers: {list(printers.keys())}")

        # Submit a print job
        print_job_id = conn.printFile(printer_name, filepath, "Print Job", {})
        print(f"Print job submitted successfully. Job ID: {print_job_id}")
    except Exception as e:
        print(f"Failed to submit print job: {e}")
