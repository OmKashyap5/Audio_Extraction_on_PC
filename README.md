# Audio_Extraction_on_PC
Extracting the audio from a video or music in real time(for Windows).

Generates a .wav file of the audio running in background from one timestamp(x1) to another(x2).
In the code:
1. In the main give the values of x1, x2 and the path to output file path(if want to change otherwise a file named output.wav will be created in the same directory as the python script).
2. The device_id can be selected as per your refrence. Here the stereo mix was used(id=14 for my PC). You can have the list of the devices for your system by using "print(sd.query_devices())". This will list all the devices along with their indices, device names, and whether they are input or output devices. There will be format like(x in,y out) for each device. Choose the one wich has at least x=1.
3. While mentioning the number of channels in sd.rec() keep in mind that it does not exceed the maximum input channel(x) for that device.

To use just run the code(after some considerations as mentioned above) along with the audio you want to extract. Keep in mind the program extracts the part from time x1 to x2 after the code is run. Like if you use it to get audio of something say 60 seconds long and you need audio between 30s to 40s, in that case you must run the program and that video simultaneously with x1=30 and x2=40. If you run the code after 10 seconds have passed in the vedio it will give audio between 40s and 50s.
