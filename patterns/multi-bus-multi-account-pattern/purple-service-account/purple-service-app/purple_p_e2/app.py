# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import json
import boto3

# pull the devops event bus arn from an environment variable where 
# DEVOPS_EVENT_BUS_ARN = 'arn:aws:events:us-east-1:[ACCOUNT-B]:event-bus/devops-event-bus'
EVENT_BUS_ARN = os.environ['EVENT_BUS_ARN'] 

# Create EventBridge client
events = boto3.client('events')

def lambda_handler(event, context):

  # new order created event detail
  eventDetail  = {
    "purpleId": "789",
    "purpleDate": "2020-12-11T22:01:02Z",
    "purpleFoo": "bar",
  }

  try:
    # Put an event
    response = events.put_events(
        Entries=[
            {
                'EventBusName': EVENT_BUS_ARN,
                'Source': 'com.exampleCorp.PurpleService',
                'DetailType': 'Event2',
                'Detail': json.dumps(eventDetail)
            }
        ]
    )
    print(response['Entries'])
    print(f"Event sent to the event bus {EVENT_BUS_ARN}")
    print(f"EventID is {response['Entries'][0]['EventId']}")
  except Exception as e:
      print(e)