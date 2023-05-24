# Workshop: Inference Optimization on AWS SageMaker

Welcome to the Inference Optimization workshop on AWS SageMaker! This workshop will guide you through a series of labs to enhance your understanding of inference optimization techniques using SageMaker.

## Prerequisites

Before starting the workshop, make sure you have the following:

- An AWS account with access to AWS SageMaker or an AWS Instructor Led Lab Account
- Basic knowledge of AWS SageMaker and machine learning concepts.

## Workshop Setup

1. **Set up AWS SageMaker Studio:**
   - Log in to your AWS account.
   - Navigate to the AWS Management Console.
   - Open SageMaker Studio.
   - Set up a new SageMaker Studio instance or use an existing one.

2. **Clone the workshop repository:**
   - Open the terminal within your SageMaker Studio instance.
   - Execute the following command to clone the repository:
   
     ```bash
     
     git clone https://github.com/rppth/inference-optimization-sagemaker
     
     ```


3. **Explore the Labs:**
   - The workshop repository contains individual lab folders labeled "Lab 1" through "Lab 6".
   - There are no dependencies within the Labs so pick whichever interests you. 
   - Open the respective lab folder and follow the instructions provided in jupyter notebooks.


## Labs Overview

1. **Lab 1: Bring your own Model - Script Mode **
   - Bring your own model into AWS SageMaker with Script-Mode
   - Configure the model to use an AWS Managed Container for Training and Inference 
   
2. **Lab 2: Picking the right Infrastructure and Monitoring your endpoints**
   - Learn how to choose the appropriate infrastructure for your model.
   - Monitor your Inference Endpoints to ensure model and data quality

3. **Lab 3: Inference Pipelines**
   - Explore the concept of inference pipelines in SageMaker.
   - Learn how to chain multiple models or containers together to create an end-to-end inference workflow.

4. **Lab 4: Ensemble Modeling**
   - Discover the power of ensemble modeling for improved inference performance.
   - Learn how to combine multiple models to make more accurate predictions.

5. **Lab 5: Multi-Model Endpoints**
   - Understand how to deploy and manage multi-model endpoints in SageMaker.
   - Learn how to serve multiple models simultaneously for different inference tasks.

6. **Lab 6: Using SageMaker Feature Store**
   - Explore the SageMaker Feature Store and its role in inference optimization.
   - Learn how to leverage the Feature Store for efficient data access during inference.


## Feedback and Support

If you have any questions or encounter issues during the workshop, please reach out to the workshop facilitators or use the issue tracker in the workshop repository.

We hope you find this workshop valuable and enjoy exploring inference optimization techniques on AWS SageMaker!

