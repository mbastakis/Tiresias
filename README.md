# Tiresias

<div id="header" align="center"><img src='https://svgshare.com/i/jLd.svg' title='tiresias-logo' width="500px" />
	<div id="badges">
		<br/>
		<a href="your-linkedin-URL">
		    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="your-youtube-URL">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>
  <a href="your-twitter-URL">
    <img src="https://img.shields.io/badge/Twitter-blue?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter Badge"/>
  </a>
</div>
</div>


> A Bilingual Question Answering over DBpedia Abstracts through Machine Translation and BERT.

**Description:** Tiresias is a research prototype that supports bilingual Question Answering (QA) over DBpedia abstracts. In particular, it retrieves a question either in Greek or in English language, and by exploiting popular Named Entity Recognition models for recognizing the entity of the question, the DBpedia abstracts written in the mentioned languages for the identified entity, Machine Translation (MT) tools, and popular BERT QA models (pretrained in English corpus), it produces the final answer.
<div align="center">
<img alt="Website" src="https://img.shields.io/website?down_color=red&down_message=down&label=Website Status&up_color=green&up_message=up&url=http%3A%2F%2Fwww.tiresias.com">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/mbastakis/Tiresias">
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/torch">
<img alt="GitHub branch checks state" src="https://img.shields.io/github/checks-status/mbastakis/Tiresias/master">
 </div>
 
**Visit the web application [here](http://www.tiresias.fun)** 

**Technology Stack:**
- HTML
- CSS
- JavaScript
- Tailwind

**Screenshot:**
[![webapp.png](https://i.postimg.cc/QxdHzvPm/webapp.png)](https://postimg.cc/yW21gp73)

## Requirements
In order to modify the web application you have to clone the repository and use one of the python versions listed above and download the dependencies. It is recommended to create and use a python environment and install the dependencies in the environment.

To create a python environment type:
```bash
$ python -m venv $environment_path
```
And to activate this environment: 
```bash
$ source $environment_path/bin/activate
```
Then you can install the dependencies like this:
```bash
$ pip install -r requirement.txt
```
## Deployment
The deployment of the web app was done with the help of Nginx and Gunicorn.
> NOTE: Before you continue make sure you have installed the requirements.

First of all we have to install Nginx so type:
```bash
$ sudo apt update
$ sudo apt install nginx
```
Now we need to create a configuration for our nginx web server allowing nginx to set up a reverse proxy for our flask application. 
```bash
$ sudo nano /etc/nginx/sites-enabled/$flask_application_name
```
Inside the file write this:
```
server {
	listen 80;
	locaction / {
		proxy_pass http://127.0.0.1:8000;
		proxy_set_header Host $host;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	}
}
```
Then you need to remove the default site of nginx to enable yours:
```bash
$ sudo unlink /etc/nginx/sites-enabled/default
```
Finally we can start workers for our app to make the web app go live:
> NOTE:  Running as a background process
```bash
$ gunicorn --workers=3 app:app --timeout 120 --daemon
```
> NOTE: Running as a  process

```bash
$ gunicorn --workers=3 app:app --timeout 120
```
## Folder Structure
```
├── app.py // This is the web application
├── controller.py // Main functions that use the utility scripts
├── README.md
├── requirements.txt // Pip requirements
├── resources // Logo of tiresias 
│   └── tiresias logo.svg
├── static
│   ├── css
│   │   └── style.css // Css of the frontend
│   └── js
│       └── main.js // Controlling the dom, and calling the backend
├── templates
│   └── index.html // frontend
└── utils
    ├── erm.py // Entity Recognition Models retrieve 
    |		    // main entity from a sentence.
    ├── __init__.py
    ├── text_splitter.py // Used for spliting the context to sentences.
    └── translator.py // Used for translating contexts and sentences.

```
## Credits and references
