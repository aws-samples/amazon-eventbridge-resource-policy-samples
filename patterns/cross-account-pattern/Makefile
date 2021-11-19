.PHONY: deploy-source deploy-destination get-source-event-bus-arn

SECURITY_ACCOUNT_NO := "999999999999"

TEMPLATE_FILE  	:= ""
TARGET_REGION  	:= "ap-southeast-1"

# Add your profile names here
PROFILE1        := "profile_for_account_1"
PROFILE2       	:= "profile_for_account_2"
PROFILE3       	:= "profile_for_account_3"

SECURITYEVENTBUSARN := ""
EVENTBUSARNACCOUNT1 := ""
EVENTBUSARNACCOUNT2 := ""
EVENTBUSARNACCOUNT3 := ""


deploy-source: source-1 source-2 source-3	

source-1:
	$(MAKE) source \
		TEMPLATE_FILE=applications/account_1/template.yaml \
		TARGET_REGION=us-east-1 \
		STACK_NAME=default-event-bus-policy-account-1 \
		PROFILE=$(PROFILE1) \
		PARAMETER_OVERRIDES="SecurityAccountNo=\"$(SECURITY_ACCOUNT_NO)\""

source-2:
	$(MAKE) source \
		TEMPLATE_FILE=applications/account_2/template.yaml \
		TARGET_REGION=us-east-1 \
		STACK_NAME=custom-bus-account-2 \
		PROFILE=$(PROFILE2) \
		PARAMETER_OVERRIDES="SecurityAccountNo=\"$(SECURITY_ACCOUNT_NO)\" EventBusName=\"custom-eventbus-account-2\""

source-3:
	$(MAKE) source \
		TEMPLATE_FILE=applications/account_3/template.yaml \
		TARGET_REGION=eu-central-1 \
		STACK_NAME=custom-bus-account-3 \
		PROFILE=$(PROFILE3) \
		PARAMETER_OVERRIDES="SecurityAccountNo=\"$(SECURITY_ACCOUNT_NO)\" EventBusName=\"custom-eventbus-account-3\""

source:
	cfn-lint $(TEMPLATE_FILE)

	- sam deploy -t $(TEMPLATE_FILE) \
		--stack-name $(STACK_NAME) \
		--region $(TARGET_REGION) \
		--profile $(PROFILE) \
		--capabilities=CAPABILITY_IAM \
		--parameter-overrides $(PARAMETER_OVERRIDES)

deploy-security-bus:
	$(MAKE) security-bus \
			TEMPLATE_FILE=security/account_1/template.yaml \
			PROFILE=$(PROFILE1)

security-bus: 
	cfn-lint $(TEMPLATE_FILE)

	- sam deploy -t $(TEMPLATE_FILE) \
		--stack-name security-event-bus \
		--capabilities=CAPABILITY_IAM \
		--region $(TARGET_REGION) \
		--profile $(PROFILE)

deploy-rules: rules-us rules-eu

rules-us:
	$(MAKE) rules \
		TEMPLATE_FILE=security/account_1/us-east-1-rules.yaml \
		TARGET_REGION=us-east-1 \
		STACK_NAME=us-east-1-rules \
		PROFILE=$(PROFILE1) \
		PARAMETER_OVERRIDES="SecurityEventBusArn=\"$(SECURITYEVENTBUSARN)\" EventBusArnAccount1=\"$(EVENTBUSARNACCOUNT1)\" EventBusArnAccount2=\"$(EVENTBUSARNACCOUNT2)\""

rules-eu:
	$(MAKE) rules \
		TEMPLATE_FILE=security/account_1/eu-central-1-rules.yaml \
		TARGET_REGION=eu-central-1 \
		STACK_NAME=eu-central-1-rules \
		PROFILE=$(PROFILE3) \
		PARAMETER_OVERRIDES="SecurityEventBusArn=\"$(SECURITYEVENTBUSARN)\" EventBusArnAccount3=\"$(EVENTBUSARNACCOUNT3)""

rules:
	cfn-lint $(TEMPLATE_FILE)

	- sam deploy -t $(TEMPLATE_FILE) \
		--stack-name $(STACK_NAME) \
		--region $(TARGET_REGION) \
		--profile $(PROFILE) \
		--capabilities=CAPABILITY_IAM \
		--parameter-overrides $(PARAMETER_OVERRIDES)





