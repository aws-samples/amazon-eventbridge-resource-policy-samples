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

#!/bin/bash
counter=1
while [ $counter -le 21 ]
do
echo $counter
aws events put-events --entries '[{"EventBusName":"ecommerce", "Source": "com.exampleCorp.webStore", "DetailType": "newOrderCreated", "Detail": "{ \"orderNo\": \"123\", \"orderDate\": \"2020-09-09T22:01:02Z\", \"customerId\": \"789\", \"lineItems\": [ { \"productCode\": \"P1\", \"quantityOrdered\": 3, \"unitPrice\": 23.5, \"currency\": \"USD\" } ]}" }]'
((counter++))
done
echo All done