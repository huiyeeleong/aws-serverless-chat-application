# aws-serverless-multi-person-chat-application
This is a chat application project using container.

This is the serverless chat app architecture

https://github.com/huiyeeleong/aws-serverless-chat-application/blob/030e70b85e5e6f25673edeac61219c86586e8817/AWS%20Serverless%20Chat%20Application%20Architecture.png

Welcome to my first CDK Serverless Multi-Person-Chat Application

Please remember run AWS Configure to use the AWS CDK Environment. - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

🧰 Prerequisites

🛠 AWS CLI Installed & Configured - https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html

🛠 AWS CDK Installed & Configured - https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html

🛠 Python Packages, Change the below commands to suit your operating system, the following are written for _Amazon Linux 2

Python3 - yum install -y python3

Python Pip - yum install -y python-pip

Virtualenv - pip3 install virtualenv

🚀 Deployment using AWS CDK

If you DONT have cdk installed
npm install -g aws-cdk

If this is first time you are using cdk then, run cdk bootstrap
cdk bootstrap

Make sure you in root directory
python3 -m venv .env source .env/bin/activate

Install any dependencies
https://docs.aws.amazon.com/cdk/api/latest/python/modules.html pip install -r requirements.txt

Synthesize the template and deploy it
cdk synth cdk deploy 🧹 CleanUp If you want to destroy all the resources created by the stack, Execute the below command to delete the stack, or you can delete the stack from console as well

cdk destroy * This is not an exhaustive list, please carry out other necessary steps as maybe applicable to your needs.

!!!Please be mindful of all the resources this will occur the charges in your AWS Account!!!