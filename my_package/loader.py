import pandas as pd

class BuildingDatasetLoader:
    """Class to load and handle building dataset operations."""
    def __init__(self, file_path):
        """
        Initializes the BuildingDatasetLoader with a specified file path.

        Args:
        file_path (str): Path to the dataset file.
        """
        self.file_path = file_path
        self.building_dataset = None

    def load_building_dataset(self):
        """
        Loads the building dataset from the file path specified during initialization.

        This method attempts to read a CSV file from the provided file path and 
        load it into a pandas DataFrame. If the file is not found, it returns an error message.

        Returns:
        DataFrame or str: The loaded building dataset as a pandas DataFrame, or an error message if the file is not found.
        """
        try:
            self.building_dataset = pd.read_csv(self.file_path)
            return self.building_dataset
        except FileNotFoundError:
            return f"Error: File not found at {self.file_path}"

    def get_building_dataset(self):
        """
        Retrieves the loaded building dataset.

        This method returns the building dataset if it has been successfully loaded. 
        If the dataset has not been loaded yet, it returns an error message instructing 
        to use the load_building_dataset() method first.

        Returns:
        DataFrame or str: The loaded building dataset as a pandas DataFrame, or an error message if the dataset is not loaded.
        """
        if self.building_dataset is not None:
            return self.building_dataset
        else:
            return "Error: Building dataset not loaded. Use load_building_dataset() method first."
