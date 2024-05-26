# AI-Chat-Bot
This is an AI Chat Bot Developed Using Gemini AI Pro.

![Gemini Image](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Gemini_SS.width-1300.jpg)

### Instructions to run
- Clone the repository by running the following command : 
```
git clone https://github.com/JabadeSusheelKrishna/AI-Chat-Bot.git
```
- Now go the the Local Repository directory by running the following command :
```
cd AI-Chat-Bot
```
- Now Install the Gemini Dependencies and Flask Modules by running the followeing commands :
```
pip3 install Flask
pip3 install -U google-generativeai
```
- Add your Gemini API Key in `server.py Line 13`. To avail Gemini API keys please visit [Gemini Documentation](https://ai.google.dev/gemini-api/docs/api-key?_gl=1*agejki*_up*MQ..&gclid=Cj0KCQjwu8uyBhC6ARIsAKwBGpQ0cdU2E1tZsmufWrn8Xk9cj-_qTFUeVVn5veLzmC9rQikXO8ghbGcaAmZNEALw_wcB)
- Now we need to run the server. to do that try following command : 
```
python3 server.py
```
- Now We are completely ready with the backend. After running the server, you should be able to see a link which looks like `http://127.0.0.XXXX`. Just go to the Browser and search this URL.
- Thats it, you should be now able to start chatting with Gemini.

### Contributions :
- Fork my repository
- if you want modify the UI part, you can directly go to `templates` directory and make modifications there.
- if you want to modify the Server part, you can change `server.py`. also each time when you change it, make sure that the AI remembers its previous chat in case of same user and forgets when user gets switched.