import os  # Used for file operations
import tkinter as tk  # Used for displaying the data to a window
from PIL import Image, ImageTk  # Used for image processing
from io import BytesIO  # Handles binary data
import shutil # Used in the case that we need to overwrite a folder 
import zlib  # Used for decompression

#Function takes in an a compressed folder and decompresses each file in the folder, each decompressed file is then saved onto a new folder
def decompress_file(input_vzip):

    decompressed_folder = "Decompressed_Frames" #Sets name for where the files will go when the frames are decompressed

    # Reads data from input in binary and saves to compressed_data
    with open(input_vzip, 'rb') as f:
        compressed_data = f.read()

    # Create new folder to store uncompressed data, will overwrite if folder already exists (Delete folder and make new)
    if os.path.exists(decompressed_folder):  # Check if folder already exists
        #print(decompressed_folder + " already exists, folder has been overwritten with updated data.")
        shutil.rmtree(decompressed_folder)  # Remove existing folder and its contents

    os.mkdir(decompressed_folder)  # Create new folder

    file_count = 1 #Counts the amount of files being decompressed, used to name files
    index_files = 0 #Keeps track of file index in compressed data var
    data_len = 4  # Length of each part of compressed data inside of compressed data var

    while index_files < len(compressed_data):  # Loops through each file found in the input folder

        # Calcuation for length of current piece of data we want to decompress
        end_range = index_files + data_len # Calc for end of range for the length for current file in this iteration
        len_compressed = int.from_bytes(compressed_data[index_files:end_range], 'little') #Uses little endian format
        index_files += data_len  # Increments to next piece of data (4 bytes)

        # Decompress specified file in compressed_data
        end_range = index_files + len_compressed # Calc for end of range of data for current file in this iteration
        decompressed_file = zlib.decompress(compressed_data[index_files:end_range])

        # Decompressed data is saved to new file
        output_filename = decompressed_folder + '/' + '{:04d}'.format(file_count) + '.ppm' # Creates file to save decompressed data to
        f_out = open(output_filename, 'wb') # Writes to file in binary
        f_out.write(decompressed_file)
        f_out.close()

        index_files += len_compressed
        file_count += 1

    #print(f"Decompressed " + str(file_count - 1) + " files to " + str(decompressed_folder))
    return decompressed_folder #Returns name of folder with decompressed frames


# Function takes in folder of decompressed frames, the function will put each frame into a list of frames and then tkinter will
# display the frames in a created window that is matched to the size of the frames
def display_frames(folder):

    list_frames = []  # Creates list to store each decompressed file into a list

    root = tk.Tk()  # Creates Tkinter window
    root.title("Player")  # Title of window is set

    for filename in sorted(os.listdir(folder)):  # Iterate through all decompressed files in the folder
        filepath = os.path.join(folder, filename)  # Gets path of the given file
        f = open(filepath, 'rb')  # Open the file in binary mode
        data = f.read()  # Save contents of file inside of data
        f.close()  # Close the file
        list_frames.append(Image.open(BytesIO(data))) #Adds image to list of frames

    frame_width, frame_height = list_frames[0].size  # Get the width and height of the first frame to set size of the window

    canvas = tk.Canvas(root, width=frame_width, height=frame_height) #Sets size of window to match frame size
    canvas.pack()

    output_image = [ImageTk.PhotoImage(frame) for frame in list_frames] # Converts image in frame to image format Tkinter can display

    # Function to update frames
    def update_frame(index_frame):
        if index_frame < len(list_frames): #Checks to see if we still need to display frames
            canvas.delete("all")  # Clears canvas
            canvas.create_image(0, 0, anchor="nw", image=output_image[index_frame]) #Displays image onto window
            index_frame += 1  # Increments onto next frame
            root.after(30, update_frame, index_frame)  # Schedule the next frame update after 30 milliseconds
        else:
            root.quit()  # Once we reach the end of the folder we quit

    update_frame(0) # Start displaying frames from the first frame in the list of frames

    root.mainloop() # Start the Tkinter window

def main():
    #IF USER WANTS TO DISPLAY THEIR OWN COMPRESSED FOLDER CHANGE THE FUNCTION BELOW TO NAME OF FOLDER AND PLACE IN SAME DIRECTORY AS PROGRAM
    input_file = 'video.vzip'  # Filename of compressed file

    # Decompress zipped file (Original project calls compressed file video.vzip)
    decompressed_frames = decompress_file(input_file) # Creates folder with decompressed frames, name is saved to decompressed_frames

    display_frames(decompressed_frames) #Displays folder of decompressed frames to window using Tkinter

main() #Calls main to start program

