import time
import numpy as np
import requests

from speech_to_text import get_text

# A simple function for choosing a number between (mi, ma) randomly. 
# We use it to stay undetecteed by google bot indentifier!
# Note: When you click buttons immediately or in fixed time, google will detect bot activity.
# (especially when you use it in loop)
def rnd_num(mi, ma):
    a = np.random.random(size=(5,5))
    a = np.random.choice(a[a>.4])
    b = np.random.randint(mi, ma)
    return a + b

def handle_recaptcha(driver, auth):
    # Find and switch to google recaptcha frame
    frame = driver.find_element_by_xpath('//iframe[@title="reCAPTCHA"]')
    driver.switch_to.frame(frame)
    time.sleep(rnd_num(4,7))

    # Find and click "Im not a robot" button.
    driver.find_element_by_id('recaptcha-anchor').click()
    driver.switch_to.default_content()
    time.sleep(rnd_num(3,5))
    
    # Find and switch to google recaptcha frame
    frame = driver.find_element_by_xpath('//iframe[@title="recaptcha challenge expires in two minutes"]')
    driver.switch_to.frame(frame)
    time.sleep(rnd_num(1,2))

    # Find and click the button that leads us to audio hearing section
    driver.find_element_by_id('recaptcha-audio-button').click()
    time.sleep(rnd_num(2,5))

    # With this code we can find out if we are detected as bot or not :)
    try:
        if driver.find_element_by_class_name('rc-doscaptcha-header'):
            print('Congratulations! You were identified as bot :) \n use VPN or whatever you know and try again!')
            # Mission Failed! Close the driver!
            driver.close()
    except:
        pass

    # We use a while loop because: Sometimes google asks you to hear and answer 2 or 3 times. 
    while True:
        # Use try to check if the element exists or not
        try:
            # Get audio's link
            t = driver.find_element_by_class_name('rc-audiochallenge-tdownload')
            t = t.find_element_by_tag_name('a')
            t = t.get_attribute('href')
            
            # Download audio file
            r = requests.get(t, allow_redirects=True)
            open('audio.mp3', 'wb').write(r.content)

            # Use get_text function in speech_to_text.py file to extract text
            text = get_text(auth)

            # Put text in the text holder and press verify
            driver.find_element_by_id('audio-response').send_keys(text)
            time.sleep(rnd_num(1,3))
            driver.find_element_by_class_name('verify-button-holder').click()
            time.sleep(rnd_num(2,4))
        except:
            # If the app doesn't find the element, it means we are done!
            break