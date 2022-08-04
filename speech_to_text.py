import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def get_text(auth):

    # insert API Key
    authenticator = IAMAuthenticator(auth)
    service = SpeechToTextV1(authenticator = authenticator)

    # insert service's url
    service.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/959e0b26-76e9-4256-997f-69eba25ae2f3')

    # open the download audio and 
    with open('audio.mp3','rb') as audio_file:
            # json loads convert a json to python dictionary.
            dic = json.loads(
                    # json dumps convert the python object ot json
                    json.dumps(
                        # recognize the audio using IBM service.
                        service.recognize(
                            audio=audio_file, 
                            model='en-US_NarrowbandModel', # which model you want to use.
                        continuous=True).get_result(), indent=2))

    # store the result in a variable
    str = ""
    while bool(dic.get('results')):
        str = dic.get('results').pop().get('alternatives').pop().get('transcript')+str[:]
	
    print(str)
    return str