import os
import clr

#clr.AddReference('System.Windows.Forms')
#clr.AddReference('System.Drawing')
#from System.Windows.Forms import MessageBox, MessageBoxIcon
#from System.Drawing import Icon

class NullFile:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_file(self):
        #MessageBox.Show(f"WARNING: File '{self.file_path}' not found", "File not found", MessageBoxButtons.OK, MessageBoxIcon.Warning)
        print(f"WARNING: File '{self.file_path}' not found", "File not found")

class LocalFileReader:
    __instance = None  # Singleton instance
    
    def __new__(cls, file_path):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = []
    
    def read_file(self):
        if not os.path.exists(self.file_path):
            null_file = NullFile(self.file_path)
            null_file.read_file()
            return
        self._open_file()
        self._read_lines()
        self._close_file()
    
    def _open_file(self):
        self.file = open(self.file_path, "r")
    
    def _read_lines(self):
        for line in self.file:
            self.content.append(line.strip())
    
    def _close_file(self):
        self.file.close()

# Example usage:
file_path = "example.txt"
reader = LocalFileReader(file_path)
reader.read_file()
MessageBox.Show("\n".join(reader.content), "File contents")
