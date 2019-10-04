import os
import sys
import time

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

# Add Computer Vision subscription key and endpoint URL from environment variables
if 'COGNITIVE_SERVICE_KEY' in os.environ:
	subscription_key = os.environ['COGNITIVE_SERVICE_KEY']
else:
	print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")

if 'COMPUTER_VISION_ENDPOINT' in os.environ:
	endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
else:
	print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")

# Instantiate a client with key credentials and endpoint
credentials = CognitiveServicesCredentials(subscription_key)
computervision_client = ComputerVisionClient(endpoint, credentials)

# Retrieve a remote image for analysis
remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/printed_text.jpg"
print("\n\nRemote image URL:\n" + remote_image_url)

# Call the Read API
# Recognize text with the Read API in a remote image by:
#   1. Specifying whether the text to recognize is handwritten or printed.
#   2. Calling the Computer Vision service's batch_read_file_in_stream with the:
#      - context
#      - image
#      - text recognition mode
#   3. Extracting the Operation-Location URL value from the batch_read_file_in_stream
#      response
#   4. Waiting for the operation to complete.
#   5. Displaying the results.
text_recognition_mode = TextRecognitionMode.printed
num_chars_in_operation_id = 36
client_response = computervision_client.batch_read_file(remote_image_url, text_recognition_mode, raw=True)

# Get READ results
# Get the operation ID returned from the batch_read_file call, and use it to query the service for operation results.
# Checks the operation at one-second intervals until the results are returned.
# Print the extracted text data to the console.
operation_location = client_response.headers["Operation-Location"]
id_location = len(operation_location) - num_chars_in_operation_id
operation_id = operation_location[id_location:]

print("\nRecognizing text in a remote image with the batch READ API ... \n")

while True:
	result = computervision_client.get_read_operation_result(operation_id)
	if result.status not in ['NotStarted', 'Running']:
		break
	time.sleep(1)

if result.status == TextOperationStatusCodes.succeeded:
	for text_result in result.recognition_results:
		for line in text_result.lines:
			print(line.text)
			print(line.bounding_box)
			print()
