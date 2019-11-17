# KSP-IPH-2019-Table01
Table Number: 01

Synopsis:

This system endeavours to solve the particular problem of face recognition in real life. There are multiple facets 
to our proposed solution. It can calculate features across any images it has to search through, finding the closest neighbour
to the queried image. 

List of tools:

- Python 3.x.x+
- Face_recognition library
- Tensorflow 1.14
- Resnet 50.
- Opencv 3.x.x+


Procedure to generate the datasets: 
  - Run python whitespaces.py on any given datasets to remove redundancies.
  - Rotate any images not straight with rotation.py
  - Run "Splitting data on male and female.ipynb" on the 'to-be' queried datasets. 
  - Run "Resnet Feature Extraction" to create the final .pickle dataset files.
  
Final:
  - After running through the above steps, run the "Script.ipynb"
            - with image index names for specific
            - or loop for all the images to be scanned.
  - An output with a dictionary 'd' would be generated:
          - Format of d:
              (File to be located, Matched file), confidence level)
              
 Architecture of the entire course project is given in: "Final PPT Facial Recog.pptx"


Predefined DataSet link: https://www.dropbox.com/s/0wsmht0y8hvviy0/Images%20-%20Final%20Sub.zip?dl=0
