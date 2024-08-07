# 🎵 Band Name Generator API

[![Django CI Check](https://github.com/mesolimbo/band-o-matic/actions/workflows/django.yml/badge.svg)](https://github.com/mesolimbo/band-o-matic/actions/workflows/django.yml)

Welcome to the home of the Band Name Generator API! Conceived and developed during the winter break of 2023-2024, this **Django-based application** captures one man's reengagement with engineering from management. This project serves as a testament to not only a rejuvenating learning process but also an enjoyable stint of growing my work proficiency with **ChatGPT**.

## 🎯 Project Vision

The aim was to construct a full-featured **Content Management System (CMS)** and data pipeline utilizing a modern framework, and delivering a Minimum Viable Product (MVP) for a service powered by the **cognitive engines** of the future; all within a **2-week sprint**. For a while the app was live on Heroku, but I have since taken it down in favor of a simpled AWS based solution.

## 🚀 Deployment & Infrastructure

The developed solution is configured for deployment via **Continuous Integration and Continuous Deployment (CI/CD)** pipeline to a **Basic Heroku web Dyno** integrated with a **mini-PostgreSQL database add-on**. This brings the total cost to approximately **$12 per month**. With the move to AWS the cost is effectively zero, as the lambda function is within the free tier.

## 🛠 Application Design

The application boasts a straightforward design – it deals with two primary models, **Words** and **Categories**, assisted by a helper model, **WordCategory**, for managing many-to-many relationships. The simplicity of the underlying design makes this an excellent resource for beginners trying to grasp the intricacies of **Django**. It encompasses various crucial features of Django such as appropriately setting up the admin app, the REST framework, different kinds of views and templates, testing techniques, etc.

## 🤖 AWS Lambda Integration

The awslambda directory is configured to hold the dependencies and files needed to pick a random band name using DynamoDB and AWS Lamdba without the overhead of Django. The Django app is still useful to manage the content locally, and I've added an export endpoint to convert the Django data to a CVS which can then be ingested into AWS.

Because the Django classes build on top of the Lambda work, assembling the zip for AWS is a little tricky, but if you need to add new dependencies to the Lambda function do so via the awsrequirements.txt in that directory, then run:

```bash
    docker build -t lambda-bando-app .
    docker run --rm -v $(pwd):/tmp lambda-bando-app \
    /bin/sh -c "mkdir -p /tmp/dist && zip -r /tmp/dist/lambda_package.zip ."
 ```
You can upload the lambda_package.zip to AWS Lambda and configure the handler to be `lambda_function.lambda_handler`.

## 🌱 Future Directions

Although the functional enhancements for this project might be minimal, its design offers a compelling demonstration of a mini CMS. It will undergo further refining, and will likely serve as a springboard for exploring the synergistic use of **React** and **Django** REST APIs in a different pet project. Furthermore, it provided a suitable test-bed to follow disciplined **Python programming practices** within the **DevSecOps** framework, and to learn how to better leverage GitHub's tooling.
