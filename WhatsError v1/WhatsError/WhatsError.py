from patterns import *
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Windows.Forms import MessageBox, MessageBoxIcon
from System.Drawing import Icon
'''
ACT extonsion to visualize the true error message from APDL Solver Output
'''
# Create some variables
fileName = 'file0.err'
noErrorMessage = 'No error found'

# Get error message in case it's present
def GetError(analysis):
    '''
    Callback to visualize the true error message
    '''
    # Get folder path
    folderPath = analysis.Solution.ResultFileDirectory
    
    # Create a FileHelper instance with the path to the folder
    helper = FileHelper(folderPath)
    
    # Get the path to a file within the folder
    file_path = helper.get_file_path(fileName)
    
    # Read file
    reader = LocalFileReader(file_path)
    reader.read_file()
    
    # Get message if error is present
    if len(reader.output_blocks) != 0:
        MessageBox.Show(' '.join(reader.output_blocks))
    else:
        MessageBox.Show(' '.join(noErrorMessage))