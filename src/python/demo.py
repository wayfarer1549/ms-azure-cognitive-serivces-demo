import os
import sys
import time

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

# Add Computer Vision subscription key and endpoint URL from environment variables
if 'COGNITIVE_SERVICE_KEY' in os.environ['COGNITIVE_SERVICE_KEY']
	subscription_key = os.environ['COGNITIVE_SERVICE_KEY']
else:
	print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")

if 'COMPUTER_VISION_ENDPOINT' in os.environ['COMPUTER_VISION_ENDPOINT']
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

