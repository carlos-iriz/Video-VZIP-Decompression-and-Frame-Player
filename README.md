# Video-VZIP-Decompression-and-Frame-Player
Given a compressed file in .vzip format the program will decompress the data and play each decompressed frame found in the file

Project Description:
The play_frames.py program will take in a compressed file called video.vzip. This file will be decompressed and each frame found within
the video will be displayed in a new window. Each frame will be shown and the window should display each frame as a video.


Before running:
Ensure the compressed folder is found within the same folder/ directory as the play_frames.py program.
NOTE: If you wish to test a different file from the one provided in the zip, change its name to "video.vzip"
      The program was meant to work with the main compression project so it only accepts files of the name "video.vzip"

Ensure python3 is installed on the machine you wish to run the program on along with the following python libraries:
   - os
   - tkinter
   - from PIL, Image, ImageTk
   - from io, BytesIO  # Handles binary data
   - shutil
   - zlib

NOTE: If an executable file is needed for testing I can provide it but it does not allow for the user to change the input file for
      the program, the exectuable only runs with the video.vzip file that was packed into it


To Run:
Open terminal and change directory to folder where the program and video.vzip file are found.

Once within the directory run the following command:
    python3 play_frames.py

Along with displaying the frames in a new window the program will also save all the decompressed data to a new folder that maintains
the same naming format of the orignal frames folder provided at the start of the project. (Each frame's name corresponds to its order)

REMINDER: If a file is to be tested you MUST change its name to video.vzip, the program only works with the formatting of the
          original compression project IE: a folder that has been compressed using the .vzip format and is made up of a folder that
          contains ONLY .ppm files. Again this follows the specifications of the original project.

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
