.PHONY: deploy-source deploy-destination get-source-event-bus-arn

SECURITY_ACCOUNT_NO := "999999999999"

TEMPLATE_FILE  	:= ""
TARGET_REGION  	:= "ap-southeast-1"
PROFILE        	:= "profile1"

deploy-source: source-1 source-2 source-3

get-source-bus-arns: get-source-1-bus-arn get-source-2-bus-arn get-source-3-bus-arn

get-source-1-bus-arn:
	$(MAKE) get-arn PREFIX=default TARGET_REGION=us-east-1 PROFILE=default

get-source-2-bus-arn:
	$(MAKE) get-arn PREFIX=cross-region-source- TARGET_REGION=us-east-1 PROFILE=demo

get-source-3-bus-arn:
	$(MAKE) get-arn PREFIX=cross-region-source- TARGET_REGION=eu-central-1 PROFILE=workshop

get-arn:
	aws events list-event-buses --name-prefix $(PREFIX) --query 'EventBuses[0].Arn' --region $(TARGET_REGION) --profile $(PROFILE)


source-1:
	$(MAKE) source \
		TEMPLATE_FILE=source_accounts\/account_111111111111/template.yaml \
		TARGET_REGION=us-east-1 \
		TARGET_ACCOUNT=111111111111 \
		PROFILE=default \
		PARAMETER_OVERRIDES="SecurityAccountNo=\"$(SECURITY_ACCOUNT_NO)\""

source-2:
	$(MAKE) source \
		TEMPLATE_FILE=source_accounts\/account_2222222222222/template.yaml \
		TARGET_REGION=us-east-1 \
		TARGET_ACCOUNT=2222222222222 \
		PROFILE=demo \
		PARAMETER_OVERRIDES="SecurityAccountNo=\"$(SECURITY_ACCOUNT_NO)\" EventBusName=\"cross-region-source-222222222222\""

source-3:
	$(MAKE) source \
		TEMPLATE_FILE=source_accounts\/account_333333333333/template.yaml \
		TARGET_REGION=eu-central-1 \
		TARGET_ACCOUNT=333333333333 \
		PROFILE=workshop \
		PARAMETER_OVERRIDES="SecurityAccountNo=\"$(SECURITY_ACCOUNT_NO)\" EventBusName=\"cross-region-source-333333333333\""

source:
	@echo "TEMPLATE_FILE:       $(TEMPLATE_FILE)"
	@echo "TARGET_REGION:       $(TARGET_REGION)"
	@echo "PROFILE:             $(PROFILE)"
	@echo "SECURITY_ACCOUNT_NO: $(SECURITY_ACCOUNT_NO)"
	@echo "PARAMETER_OVERRIDES: $(PARAMETER_OVERRIDES)"

	cfn-lint $(TEMPLATE_FILE)

	- sam deploy -t $(TEMPLATE_FILE) \
		--stack-name cross-region-source-$(TARGET_ACCOUNT) \
		--region $(TARGET_REGION) \
		--profile $(PROFILE) \
		--capabilities=CAPABILITY_IAM \
		--parameter-overrides $(PARAMETER_OVERRIDES)

deploy-destination:
	$(MAKE) destination \
			TEMPLATE_FILE=destination_account/account_111111111111/template.yaml
			PARAMETER_OVERRIDES="EventBusName=\"cross-region-destination-111111111111\" Source1EventBusArn=\"arn:aws:events:us-east-1:538510314095:event-bus/default\" Source2EventBusArn=\"arn:aws:events:us-east-1:490195310065:event-bus/cross-region-source-222222222222\" Source3EventBusArn=\"s\""

destination: 
	@echo "TEMPLATE_FILE:       $(TEMPLATE_FILE)"
	@echo "PARAMETER_OVERRIDES: $(PARAMETER_OVERRIDES)"
	
	cfn-lint $(TEMPLATE_FILE)

	- sam deploy -t $(TEMPLATE_FILE) \
		--stack-name cross-region-destination-1111111111111 \
		--capabilities=CAPABILITY_IAM \
		--region $(TARGET_REGION) \
		--profile $(PROFILE) \
		--parameter-overrides $(PARAMETER_OVERRIDES)