# YOLOv3 Post Processing on ZCU104 
Tensor outputs form Vitis AI Runner Class for YOLOv3 are provided in the text files. Each image has the three output 
tensors associated with it. Output tensor dimensions are: (1,13,13,75), (1,26,26,75), and (1,52,52,75). Data from text 
files can be read as shown in the following code snippet. DPU tensors provide 4D tensors as output, so it is better to 
work directly with 4D tensons as shown below. 

    conv_out1  = np.loadtxt('image_3_output0.txt')
    conv_out2  = np.loadtxt('image_3_output1.txt')
    conv_out3  = np.loadtxt('image_3_output2.txt')
    conv_out1 = np.reshape(conv_out1, (1,13, 13, 75))
    conv_out2 = np.reshape(conv_out2, (1,26, 26, 75))  
    conv_out3 = np.reshape(conv_out3, (1,52, 52, 75))
    yolo_outputs = [conv_out1, conv_out2, conv_out3]  
    
For some reason, last four lines of the second tensor (IMAGE_NAME_output1.txt) is not printed/available from DPU output, 
it is replaced with zeros to be consistent with DPU output format. zeroGen.py is used to generate zeros as filler elements.

Information on Anchor boxes can be found in yolov3_voc.prototxt and class list is available in voc_classes.txt file.
