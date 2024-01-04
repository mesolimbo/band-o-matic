# 🎵 Band Name Generator API

Welcome to the home of the Band Name Generator API! Conceived and developed during the winter break of 2023-2024, this **Django-based application** captures one man's reengagement with engineering from management. This project serves as a testament to not only a rejuvenating learning process but also an enjoyable stint of growing my work proficiency with **ChatGPT**.

## 🎯 Project Vision

The aim was to construct a full-featured **Content Management System (CMS)** and data pipeline utilizing a modern framework, and delivering a Minimum Viable Product (MVP) for a service powered by the **cognitive engines** of the future; all within a **2-week sprint**. You can [click here](https://bands.twerk.click/) to see the "production" demo app.

## 🚀 Deployment & Infrastructure

The developed solution is configured for deployment via **Continuous Integration and Continuous Deployment (CI/CD)** pipeline to a **Basic Heroku web Dyno** integrated with a **mini-PostgreSQL database add-on**. This brings the total cost to approximately **$12 per month**.

## 🛠 Application Design

The application boasts a straightforward design – it deals with two primary models, **Words** and **Categories**, assisted by a helper model, **WordCategory**, for managing many-to-many relationships. The simplicity of the underlying design makes this an excellent resource for beginners trying to grasp the intricacies of **Django**. It encompasses various crucial features of Django such as appropriately setting up the admin app, the REST framework, different kinds of views and templates, testing techniques, etc.

## 🤖 OpenAI GPT Action Endpoint

This project also functions as an **OpenAI GPT action endpoint**, making it a solid starting point if you aim to build your own endpoint or define an **OpenAPI specification**. Given the upcoming opening of the GPT store by OpenAI, the content will be periodically updated to keep pace with ongoing developments. [Click here if you want to try the Random Band Name Generator GPT.](https://chat.openai.com/g/g-cySOJm4lG-awesome-band-factory)

## 🌱 Future Directions

Although the functional enhancements for this project might be minimal, its design offers a compelling demonstration of a mini CMS. It will undergo further refining, and will likely serve as a springboard for exploring the synergistic use of **React** and **Django** REST APIs. Furthermore, it provides a suitable test-bed to follow disciplined **Python programming practices** within the **DevSecOps** framework, and to learn how to better leverage GitHub's tooling.
