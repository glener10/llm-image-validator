# **llm-image-validator**

<p align="center"> 🚀 This script is designed to validate technical images such as diagrams and flowcharts using different LLM models and generate a new image correcting any identified issues.</p>

Example of execution without issues:

![example_no_issues](./docs/execution_without_issues_example.png)

Example of execution with issues:

![example_with_issues](./docs/execution_with_issues_example.png)

Check the generated image fixed the identified issues [`docs/image_with_issues_solved`](docs/image_with_issues_solved.png) and the input image with issues in [`input.jpg`](input.jpg)

<h3>🏁 Table of Contents</h3>

<br>

===================

<!--ts-->

💻 [Dependencies and Environment](#dependenciesandenvironment)

☕ [Using](#using)

👷 [Author](#author)

<!--te-->

===================

<div id="dependenciesandenvironment"></div>

## 💻 **Dependencies and Environment**

**Gemini**: This project uses the paid Google Gemini API, it's necessary to [configure a valid Gemini API Key](https://aistudio.google.com/apikey). Ensure you have a `.env` file with the environment variable **API_KEY**.

<div id="using"></div>

## ☕ **Using**

First, check the [dependencies](#dependenciesandenvironment) process

You can clean the environment using

```
$ make clean
```

Check files format with

```
$ make lint
```

Format files with

```
$ make format
```

to exec:

```
$ make run
```

Check the required and optional parameters in the [`src/args.py`](src/args.py) file.

Example executing with arguments:

```
$ make run ARGS="-i \"./input.jpg\""
```

you can run also using the script

```
$ python .\main.py -i './input.jpg'
```

<div id="author"></div>

#### **👷 Author**

Made by Glener Pizzolato! 🙋

[![Linkedin Badge](https://img.shields.io/badge/-Glener-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/glener-pizzolato/)](https://www.linkedin.com/in/glener-pizzolato-6319821b0/)
[![Gmail Badge](https://img.shields.io/badge/-glenerpizzolato@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:glenerpizzolato@gmail.com)](mailto:glenerpizzolato@gmail.com)
