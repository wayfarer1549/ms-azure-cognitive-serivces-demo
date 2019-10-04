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
