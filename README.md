# Welcome to home of the Band Name Generator API!

During the winter break of 2023-2024, I developed this Django site. It's a blend of interview preparation and playful interaction with ChatGPT.

It might seem nerdy to some, but [let's explore what I've built](https://bands.twerk.click/): It's an application that generate an endless variety of Band Names, backed by a full-featured CMS and a RESTfult API (a testament to Django's ease of configuration).


Behind the scenes, I've deployed on Heroku, connected a Postgres DB with my app, constructed a secure API to interact programmatically with the DB, and set up Django's admin UI for full manual control. All in a few days' work!

But, the journey didn't end there:

I developed a special JSON GET endpoint that dispenses random band names, supplemented it with an [OpenAPI spec](https://bands.twerk.click/api/v1/openapi.html), and topped it off with a Privacy Policy. Why, you ask?

It's for a simple reason: to connect the JSON endpoint, the spec, and the policy to an OpenAI GPT. An autonomous agent was born from this artificial collaboration, serving you unique band names and matching art according to given inputs. [Give it whirl here!](https://chat.openai.com/g/g-cySOJm4lG-awesome-band-factory)

Silly it may seem, but the goal was to establish a pipeline with an AI, meticulously integrating it into a system I built from scratch. The idea? Connect our data with the cognitive engines of tomorrow.