# ChitChatty

## Description
ChitChatty is an innovative project designed to demonstrate the integration of Twilio, ngrok, and OpenAI in creating a customized chatbot. This project showcases the seamless communication capabilities of Twilio for handling messages, utilizes ngrok to expose local servers to the internet for easy access during development, and leverages the advanced conversational abilities of OpenAI to deliver a unique and engaging chatbot experience.

## Built With
* [Python](https://www.python.org/)
* [Twilio](https://www.twilio.com/en-us)
* [ngrok](https://ngrok.com/)
* [openai](https://openai.com/)

## Getting Started

### Dependencies
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [OpenAI](https://pypi.org/project/openai/)
* [Aiohttp](https://docs.aiohttp.org/en/stable/)
* [Requests](https://docs.python-requests.org/en/master/)

### Installing
1. Clone the repository:
   ```bash
   git clone https://github.com/swang308/ChitChatty.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ChitChatty
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Register a twilio and ngrok account, and create an **.env** file and put below information.
   ```bash
    # Twilio Credentials
    TWILIO_SID=SID_HERE
    TWILIO_AUTH_TOKEN=TOKEN_HERE
    FROM=whatsapp:NUMBER_HERE

    # OpenAI API Key
    OPENAI_API_KEY=OPENAI_API
   ```

### Executing program

1. Start the application:
   ```bash
   python app.py
   ```
2. Open your terminal and run 
   ```bash
   ngrok ngrok http 8080
   ```
3. Go to twilio, and create an account. Direct to Messaging -> Try it out -> Send a Whatsapp message -> Sandbox settings -> When a message comes in, fill the address you just run on terminal, it looks like this:
   ```bash
   https://ef51-173-35-56-48.ngrok-free.app/webhook
   ```
4. Open your Whatsapp and find twilio you just verify.
5. Start chatting~!

## Help

For any issues or questions, please feel free to open an issue on the [GitHub repository](https://github.com/swang308/ChitChatty/issues).

## Authors

Shanyun Wang  
[GitHub Profile](https://github.com/swang308)

## Version History

* 0.1
    * Initial Release

## License


## Acknowledgments

Inspiration, code snippets, etc.
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [OpenAI](https://pypi.org/project/openai/)
* [Aiohttp](https://docs.aiohttp.org/en/stable/)
* [Requests](https://docs.python-requests.org/en/master/)
* [GitHub README Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)