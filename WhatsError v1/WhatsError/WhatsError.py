from patterns import *
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Windows.Forms import MessageBox, MessageBoxIcon
from System.Drawing import Icon
'''
ACT extonsion to visualization of true error from APDL Solver Output
'''
# Create some variables
folderPath = r'D:\projects\my_scripting\Ansys-whats-error\WhatsError v1\try_files\dp0\SYS\MECH'
fileName = 'file0.err'

def GetError(analysis):
    # Create a FileHelper instance with the path to the folder
    helper = FileHelper(folderPath)
    
    # Get the path to a file within the folder
    file_path = helper.get_file_path(fileName)
    
    reader = LocalFileReader(file_path)
    reader.read_file()
    MessageBox.Show(' '.join(reader.output_blocks))