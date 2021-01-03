#* FastAPI setting *
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional # for Query param set as 'Optional'
from typing import Union
from pydantic import BaseModel
from datetime import datetime

import traceback # for easy to debug
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s:\t[%(filename)s:%(lineno)s - %(funcName)20s() ]\t%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


app = FastAPI()

# allow CORS setting
origins = [
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# security setting
# https://geekflare.com/http-header-implementation/https://geekflare.com/http-header-implementation/
HEADERS = {
    # CORS setting
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Allow-Headers": "*",
    # security setting
    "X-Frame-Options": "SAMEORIGIN",
    "X-Content-Type-Options": "nosniff",
    "X-XSS-Protection": "1; mode=block",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Expect-CT": "max-age=86400, enforce", # enforcement of Certificate Transparency for 24 hours
    "Content-Security-Policy": "default-src https:"
}

# OUTPUT_RESPONSE = {
#     "data": {},
#     "success": False,
#     "message": ""
# }


# * functions *

OUTPUT_RESPONSE = {
        "Action": "",
        "Agent": "DemoGLSHK",
        "Concept": "",
        "ID": "",
        "ImageURL": "",
        "Name": "Template all type",
        "ResolvedQuery": "",
        "Responses": [""],
        "Score": 100,
        "Speech": "",
        "Success": False,
        "messages": []
    }

class Query(BaseModel):
    session_id: str = 'xxx'
    text: str

# * main routing *

# @app.route('/', methods=['GET'])
@app.get("/", status_code=200)
@app.post("/", status_code=200)
async def root():
    # return {"message": f"app is running {datetime.now()}"}
    testing_dict = {
  "Action": "", 
  "Agent": "DemoGLSHK", 
  "Concept": "", 
  "ID": "000", 
  "ImageURL": "", 
  "Name": "Template all type", 
  "ResolvedQuery": "testing", 
  "Responses": [
    "template for ChatBubble"
  ], 
  "Score": 100, 
  "Speech": "", 
  "Success": True, 
  "messages": [
    {
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "style": "pulse", 
      "text": "This is test message", 
      "type": "text"
    }, 
    {
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "rating": {
        "buttons": [
          {
            "title": "1 star", 
            "type": "payload", 
            "value": "rating_0001_1star"
          }, 
          {
            "title": "2 star", 
            "type": "payload", 
            "value": "rating_0001_2star"
          }, 
          {
            "title": "3 star", 
            "type": "payload", 
            "value": "rating_0001_3star"
          }, 
          {
            "title": "4 star", 
            "type": "payload", 
            "value": "rating_0001_4star"
          }, 
          {
            "title": "5 star", 
            "type": "payload", 
            "value": "rating_0001_5star"
          }
        ], 
        "text": "rate it", 
        "type": "star"
      }, 
      "style": "pulse", 
      "text": "test message with rating (Star)", 
      "type": "text"
    }, 
    {
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "rating": {
        "buttons": [
          {
            "title": "thumb up", 
            "type": "payload", 
            "value": "rating_0001_thumbup"
          }, 
          {
            "title": "thumb down", 
            "type": "payload", 
            "value": "rating_0001_thumbdown"
          }
        ], 
        "text": "rate it", 
        "type": "thumb"
      }, 
      "style": "pulse", 
      "text": "test message with rating (thumbup)", 
      "type": "text"
    }, 
    {
      "image_url": "https://www.chatbot.hk/Image/AB/HKSTP/HKSTP.jpg", 
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "style": "fadeInLeft", 
      "type": "image", 
      "web_url": "https://www.hkstp.org/media/1225/corporate_leaflet_final_jan_2017.pdf"
    }, 
    {
      "buttons": [
        {
          "title": "This is 1st button label", 
          "type": "payload", 
          "value": "1stButtonValue"
        }, 
        {
          "title": "This is 2nd button label", 
          "type": "payload", 
          "value": "2ndButtonValue"
        }, 
        {
          "title": "This is 3rd button label", 
          "type": "web_url", 
          "value": "https://www.google.com"
        }
      ], 
      "input_disabled": True, 
      "input_placeholder": "Please select from the options ...", 
      "style": "pulse", 
      "type": "buttons"
    }, 
    {
      "buttons": [
        {
          "title": "This is 1st button label", 
          "type": "payload", 
          "value": "1stButtonValue"
        }, 
        {
          "title": "This is 2nd button label", 
          "type": "payload", 
          "value": "2ndButtonValue"
        }, 
        {
          "title": "This is 3rd button label", 
          "type": "web_url", 
          "value": "https://www.google.com"
        }
      ], 
      "input_disabled": True, 
      "input_placeholder": "Type something ...", 
      "style": "pulse", 
      "text": "This is Quick Reply text", 
      "type": "quick_replies"
    }, 
    {
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "style": "pulse", 
      "text": "This is test message (card)", 
      "type": "text"
    }, 
    {
      "cards": [
        {
          "buttons": [
            {
              "title": "1s", 
              "type": "payload", 
              "value": "1stButtonValue"
            }, 
            {
              "title": "2n", 
              "type": "payload", 
              "value": "2ndButtonValue"
            }, 
            {
              "title": "3r", 
              "type": "web_url", 
              "value": "https://www.google.com"
            }
          ], 
          "icon": "https://www.hkstp.org/media/2264/icon_excellence.png", 
          "image_url": "https://www.chatbot.hk/Image/AB/HKSTP/HKSTP_wBackground.jpg", 
          "subtitle": "01\u4e2d\u6587<br>New Line", 
          "title": "cArd \u4e2d\u6587Title 01"
        }, 
        {
          "buttons": [
            {
              "title": "This is 1st button label", 
              "type": "payload", 
              "value": "1stButtonValue"
            }, 
            {
              "title": "This is 2nd button label", 
              "type": "payload", 
              "value": "2ndButtonValue"
            }, 
            {
              "title": "This is 3rd button label", 
              "type": "web_url", 
              "value": "https://www.google.com"
            }
          ], 
          "icon": "https://www.hkstp.org/media/2264/icon_excellence.png", 
          "image_url": "https://www.chatbot.hk/Image/AB/HKSTP/HKSTP.jpg", 
          "subtitle": "01\u4e2d\u6587<br>New Line", 
          "title": "card \u4e2d\u6587Title 02"
        }, 
        {
          "buttons": [
            {
              "title": "This is 1st button label", 
              "type": "payload", 
              "value": "1stButtonValue"
            }, 
            {
              "title": "This is 2nd button label", 
              "type": "payload", 
              "value": "2ndButtonValue"
            }, 
            {
              "title": "This is 3rd button label", 
              "type": "web_url", 
              "value": "https://www.google.com"
            }
          ], 
          "icon": "https://www.hkstp.org/media/2264/icon_excellence.png", 
          "image_url": "https://www.chatbot.hk/Image/AB/HKSTP/HKSTP.jpg", 
          "subtitle": "01\u4e2d\u6587<br>New Line", 
          "title": "card \u4e2d\u6587Title 03"
        }
      ], 
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "style": "fadeIn", 
      "type": "cards"
    }, 
    {
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "list": {
        "button": [
          {
            "title": "ButtonTitleMore", 
            "type": "payload", 
            "value": "ListButtonValue"
          }
        ], 
        "elements": [
          {
            "buttons": [
              {
                "title": "This is 1st button label", 
                "type": "payload", 
                "value": "1stButtonValue"
              }
            ], 
            "image_url": "https://www.chatbot.hk/Image/AB/HKSTP/HKSTP.jpg", 
            "subtitle": "01\u4e2d\u6587Subtitle", 
            "title": "List Element 01"
          }, 
          {
            "buttons": [
              {
                "title": "This is 1st button label", 
                "type": "web_url", 
                "value": "https://www.google.com"
              }
            ], 
            "image_url": "https://www.chatbot.hk/Image/AB/HKSTP/HKSTP.jpg", 
            "subtitle": "01\u4e2d\u6587Subtitle", 
            "title": "List Element 02"
          }, 
          {
            "buttons": [
              {
                "title": "This is 1st button label", 
                "type": "payload", 
                "value": "1stButtonValue"
              }
            ], 
            "image_url": "https://www.chatbot.hk/Image/AB/HKSTP/HKSTP.jpg", 
            "subtitle": "01\u4e2d\u6587Subtitle", 
            "title": "List Element 03"
          }, 
          {
            "buttons": [
              {
                "title": "This is 1st button label", 
                "type": "payload", 
                "value": "1stButtonValue"
              }
            ], 
            "image_url": "https://www.chatbot.hk/Image/AB/HKSTP/HKSTP.jpg", 
            "subtitle": "01\u4e2d\u6587Subtitle", 
            "title": "List Element 04"
          }, 
          {
            "buttons": [
              {
                "title": "This is 1st button label", 
                "type": "payload", 
                "value": "1stButtonValue"
              }
            ], 
            "image_url": "https://www.chatbot.hk/Image/AB/HKSTP/HKSTP.jpg", 
            "subtitle": "01\u4e2d\u6587Subtitle", 
            "title": "List Element 05"
          }, 
          {
            "buttons": [
              {
                "title": "This is 1st button label", 
                "type": "payload", 
                "value": "1stButtonValue"
              }
            ], 
            "image_url": "https://www.chatbot.hk/Image/AB/HKSTP/HKSTP.jpg", 
            "subtitle": "01\u4e2d\u6587Subtitle", 
            "title": "List Element 06"
          }
        ]
      }, 
      "style": "slideInUp", 
      "type": "list"
    }, 
    {
      "buttons": [
        {
          "title": "1st option label", 
          "type": "payload", 
          "value": "1stOptionValue"
        }, 
        {
          "title": "2nd option label", 
          "type": "web_url", 
          "value": "https://www.google.com"
        }, 
        {
          "title": "3rd option label", 
          "type": "payload", 
          "value": "3rdOptionValue"
        }, 
        {
          "title": "4th option label", 
          "type": "payload", 
          "value": "3rdOptionValue"
        }
      ], 
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "style": "fadeInLeft", 
      "title": "Dropdown Title", 
      "type": "dropdown"
    }, 
    {
      "default_month": "2018-10-01", 
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "style": "zoomIn", 
      "type": "datepicker"
    }, 
    {
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "options": [
        {
          "buttons": [
            {
              "title": "10:30am", 
              "type": "payload", 
              "value": "10:30"
            }, 
            {
              "title": "Google", 
              "type": "web_url", 
              "value": "https://www.google.com"
            }, 
            {
              "title": "01:15pm", 
              "type": "payload", 
              "value": "13:15"
            }, 
            {
              "title": "02:45pm", 
              "type": "payload", 
              "value": "14:45"
            }
          ], 
          "title": "Option 1"
        }, 
        {
          "buttons": [
            {
              "title": "14:30pm", 
              "type": "payload", 
              "value": "14:30"
            }, 
            {
              "title": "15:15pm", 
              "type": "payload", 
              "value": "15:15"
            }, 
            {
              "title": "16:45pm", 
              "type": "payload", 
              "value": "16:45"
            }
          ], 
          "title": "Option 2"
        }
      ], 
      "style": "fadeInLeft", 
      "title": "2018\u5e74 10\u5e74 11\u65e5", 
      "type": "droplist"
    }, 
    {
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "style": "fadeInLeft", 
      "type": "video", 
      "video_url": "https://asiabots-ryan-test.s3-ap-southeast-1.amazonaws.com/test.mp4"
    }, 
    {
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "style": "fadeInLeft", 
      "type": "youtube", 
      "video_url": "https://youtu.be/3yVFawOmjpY"
    }, 
    {
      "audio_url": "https://asiabots-tts-prototype.azurewebsites.net/audio_cache/a97ac0d5b044eef07a41a0711a4e7790.wav", 
      "input_disabled": False, 
      "input_placeholder": "Type something ...", 
      "style": "fadeInLeft", 
      "type": "audio"
    }
  ]
}
    return testing_dict

