from typing import Protocol
from aws_cdk import core as cdk
from aws_cdk import (
    core,
    aws_ec2 as _ec2,
    aws_ecs as _ecs,
    aws_ecs_patterns as _ecs_patterns
)


class AwsChatAppFileStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        #Define the VPC or we can reuse exsiting vpc
        #vpc = _ec2.Vpc.from_lookup(
        #    self,
        #    "ImportedVPC",
        #    vpc_id="vpc-d21e0fb0"
        #)

        #create vpc
        vpc = _ec2.Vpc(
            self,
            "chatappVPC",
            max_azs = 2,
            nat_gateways=1
        )

        # Create Fargate Cluster
        hui_chat_app_cluster = _ecs.Cluster(
            self,
            "chatAppCluster"
        )

        # Create chat service as Fargate Task
        hui_chat_app_task_def = _ecs.FargateTaskDefinition(
            self,
            "chatAppTaskDef"
        )

        # Create Container Definition
        hui_chat_app_container = hui_chat_app_task_def.add_container(
            "chatAppContainer",
            image=_ecs.ContainerImage.from_registry(
                "mystique/fargate-chat-app:latest"
            ),
            environment={
                "Environment" : "DEV"
            }
        )

        # Add Port Mapping to Container, Chat app runs on Port 3000
        hui_chat_app_container.add_port_mappings(
            _ecs.PortMapping(container_port=3000, protocol=_ecs.Protocol.TCP)
        )

        # Deploy Container in the micro Service & Attach a LoadBalancer
        chat_app_service = _ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "Service",
            cluster=hui_chat_app_cluster,
            task_definition=hui_chat_app_task_def,
            assign_public_ip=False,
            public_load_balancer=True,
            listener_port=80,
            desired_count=1,
            service_name="HuiChatApp"
        )

        # Output Chat App Url
        output_1 = core.CfnOutput(
            self,
            "chatAppServiceUrl",
            value=f"http://{chat_app_service.load_balancer.load_balancer_dns_name}",
            description="Access the chat app url from your browser"
        )



