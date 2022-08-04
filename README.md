# Automate Google reCAPTCHA 

A Selenium Bot Written in Python for Automating Google reCAPTCHA Using IBM Watson (Speech to Text API).

Each line of the codes is described. So inspect the codes with comfort.

Feel free to try this well-documented project! :)

## Demo
#### Let's try the app for <a href="https://www.google.com/recaptcha/api2/demo" target="_blank">official google recaptcha demo</a> site:

<img src="https://drive.google.com/uc?export=download&id=1b5rMiJdTRod5EkNa7j7r7GbQ2aA3xZOG"/>
     
## Usage
1- Sign-up and create "Speech to Text" service:
* Go to the <a href="https://cloud.ibm.com/catalog/services/speech-to-text">Speech to Text page</a>
* Sign up for a free IBM Cloud account or log in.
* Click Create.

2-Access your credentials and copy the API Key:
* From the <a href="https://cloud.ibm.com/resources">IBM Cloud Resource list</a>, click on your Speech to Text service instance.
* Click Show Credentials on the Manage page.
* Copy the API Key.

3- Paste the API Key in ```auth``` variable in ```main.py```

4- Run ```main.py``` file :
```
$ python main.py
```
Note: You should install selenium, ibm_watson and fake-useragent libraries.

## File Description
* ```speech_to_text.py``` consists of a function called ```get_text```that sends the audio file to Speech to Text API and gets the result. Eventually, the funtion returns a string, including transcript of the audio.
* ```recaptcha.py``` is the place where magic happens! It finds the google recaptcha service in the web page using selenium driver, then clicks it automatically and goes to audio hearing section. Finally, It recieves the transcript from the ```get_text``` function from ```speech_to_text.py```.
* ```main.py``` wraps up the project. It initialize the driver with given link address and then calls the ```handle_recaptcha``` function from ```recapthca.py```.

## Note

I used the IBM Watson Speech to Text API for handling the audio transcription task. You could use your preferred model in ```speech_to_text.py``` and return the result.

I'd like to hear your ideas :)
