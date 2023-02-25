import os

class NullFile:
    """
    A Null Object to represent a nonexistent file.
    This is used in place of an actual file object if the file could not be found.
    """
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_file(self):
        """
        This method is called if read_file() is called on a NullFile object.
        It displays a message indicating that the file was not found.
        """
        print(f"WARNING: File '{self.file_path}' not found")

class LocalFileReader:
    """
    A Singleton class that reads a file from the local file system and stores its contents in a list.
    If the file does not exist, a NullFile object is used instead.
    """
    __instance = None  # Singleton instance
    
    def __new__(cls, file_path):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.output_blocks = []  # list to store file contents
        self.current_block = []  # list to store target lines
    
    def read_file(self):
        """
        Reads the contents of the file and stores them in self.output_blocks.
        If the file does not exist, a NullFile object is used instead.
        """
        if not os.path.exists(self.file_path):
            null_file = NullFile(self.file_path)
            null_file.read_file()
            return
        self._open_file()
        self._read_lines()
        self._close_file()
    
    def _open_file(self):
        """
        Opens the file for reading and assigns the resulting file object to self.file.
        """
        self.file = open(self.file_path, "r")
    
    def _read_lines(self):
        """
        Reads the lines of the file and appends them to self.output_blocks.
        """
        inside_block = False
        start_str = '*** ERROR ***'
        end_str = '\n'
        for line in self.file:
            if start_str in line:
                inside_block = True
                self.current_block = []
            elif inside_block and line == end_str:
                inside_block = False
            elif inside_block:
                self.current_block = line.split('\n')[0].strip()
                self.output_blocks.append(self.current_block)
    
    def _close_file(self):
        """
        Closes the file.
        """
        self.file.close()

class FileHelper:
    def __init__(self, folder_path):
        """
        Constructor for the FileHelper class.

        Args:
            folder_path (str): Path to the folder containing the files.
        """
        self.folder_path = folder_path
        
    def get_file_path(self, filename):
        """
        Constructs the full path to a file within the folder.

        Args:
            filename (str): Name of the file.

        Returns:
            str: Full path to the file.
        """
        return os.path.join(self.folder_path, filename)


# Example usage:
folderPath = r'D:\projects\my_scripting\Ansys-whats-error\WhatsError v1\try_files\dp0\SYS\MECH'
fileName = 'file0.err'
# Create a FileHelper instance with the path to the folder
helper = FileHelper(folderPath)

# Get the path to a file within the folder
file_path = helper.get_file_path(fileName)

reader = LocalFileReader(file_path)
reader.read_file()
print(' '.join(reader.output_blocks))