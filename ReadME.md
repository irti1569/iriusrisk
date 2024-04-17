# IriusRisk Technical Assessment

The IriusRisk technical assessment required me to develop a a RESTful API service that interfaces with a simple language model. I chose to implement a basic text summarization endpoint using Flask. 

### Setup

- Create a virtual environment ([reference](https://docs.python.org/3/library/venv.html))
- Install the required libraries via `pip install -r requirements.txt`
- Run the app via `python run.py`


### Deployment
- To deploy the application, create a package using `python setup.py install`


### Endpoints
The service has one endpoint `summarize_text`. The endpoint accept json as input (`{'text': 'YOUR TEXT HERE'}`). It returns a summary as json (`{'summary': 'summarized text here'}`)
![Sample Request and Response](C:\Users\Irtza\PycharmProjects\iriusRiskTechnicalAssessment\IriusRisk Technical Assessment.PNG)