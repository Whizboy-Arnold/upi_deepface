from deepface import DeepFace
import json 

# Load the images
# img1_path = "images/test/beyonce1.jpg"
# img2_path = "images/test/beyonce2.jpg"
# Load the images
img1_path = "images/test/warren1.jpg"
img2_path = "images/test/warren2.jpg"

# Verify the faces
result = DeepFace.verify(img1_path, img2_path)

# Print the result
# print("Are the faces similar?: ", result["verified"])
# print(" Result : ", json.dumps(result) )
print(" Result : ", result )
 