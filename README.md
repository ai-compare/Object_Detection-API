# Object Detection - Eden AI API
## Description
This repositery provides code to implement Eden AI Object Detection API. Eden AI Object Detection API allows to call Object Detection APIs from multpile object detection providers. It permits to get results from these providers, compare the results, siwtch between providers or combine them.

## What is AI-Compare ?
[Eden AI](https://www.edanai.co/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers for vision, text, audio, OCR, prediction and translation AI engines. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

Eden AI offers community offer (free) when you [create your account for free](https://app.edenai.run/user/login). You can then use [APIs](https://api.edenai.run/v1/redoc/), use the [interface](https://app.edenai.run/bricks/default), manage your account, access to cost management.

You can find APIs documentation here : https://api.edenai.run/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your account manager [here](https://www.ai-compare.com/accounts/login/?next=/my_apis/my_account).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://dev-api.edenai.run/v1/pretrained/vision/object_detection'
```
### Select parameters 
Set your file (.jpg, .png, .jpeg, .tiff), the attempted objects, and providers APIs you want to run :
```python
payload = {'providers': '[\'google_cloud\', \'microsoft\', \'aws\', \'ibm\']','objects_to_find': ''}
files = [  ('files', open('Picture/example.jpg','rb'))]
```
### Get results
```python
response = requests.request("POST", url, headers=headers, data = payload, files = files)
print(response.text.encode('utf8'))
```

## Response example
<details>
<summary>

```json
{
  "result": [
    {"solution_name": "Google cloud","execution_time": "0.912418","result": {"image_path": "media/data/files/object_detection_oSDc5Rj.jpg","labels": ["Bicycle","Bicyclewheel","Tire","Wheel"],"confidences": [0.97236437,0.94123334,0.9412165,0.6519385],
```

</summary>

```json
{
  "result": [
    {
      "solution_name": "Google cloud",
      "execution_time": "0.912418",
      "result": {
        "image_path": "media/data/files/object_detection_oSDc5Rj.jpg",
        "labels": [
          "Bicycle",
          "Bicycle wheel",
          "Tire",
          "Wheel"
        ],
        "confidences": [
          0.97236437,
          0.94123334,
          0.9412165,
          0.6519385
        ],
        "x_mins": [
          0.06473605,
          0.05486482,
          0.6285886,
          0.40014446
        ],
        "x_maxs": [
          0.9543211,
          0.42698047,
          0.961559,
          0.5116857
        ],
        "y_mins": [
          0.13989596,
          0.42574355,
          0.43271652,
          0.5569999
        ],
        "y_maxs": [
          0.7861735,
          0.78711677,
          0.77879936,
          0.6681271
        ]
      },
      "api_response": {
        "responses": [
          {
            "localizedObjectAnnotations": [
              {
                "mid": "/m/0199g",
                "name": "Bicycle",
                "score": 0.97236437,
                "boundingPoly": {
                  "normalizedVertices": [
                    {
                      "x": 0.06473605,
                      "y": 0.13989596
                    },
                    {
                      "x": 0.9543211,
                      "y": 0.13989596
                    },
                    {
                      "x": 0.9543211,
                      "y": 0.7861735
                    },
                    {
                      "x": 0.06473605,
                      "y": 0.7861735
                    }
                  ]
                }
              },
              {
                "mid": "/m/01bqk0",
                "name": "Bicycle wheel",
                "score": 0.94123334,
                "boundingPoly": {
                  "normalizedVertices": [
                    {
                      "x": 0.05486482,
                      "y": 0.42574355
                    },
                    {
                      "x": 0.42698047,
                      "y": 0.42574355
                    },
                    {
                      "x": 0.42698047,
                      "y": 0.78711677
                    },
                    {
                      "x": 0.05486482,
                      "y": 0.78711677
                    }
                  ]
                }
              },
              {
                "mid": "/m/0h9mv",
                "name": "Tire",
                "score": 0.9412165,
                "boundingPoly": {
                  "normalizedVertices": [
                    {
                      "x": 0.6285886,
                      "y": 0.43271652
                    },
                    {
                      "x": 0.961559,
                      "y": 0.43271652
                    },
                    {
                      "x": 0.961559,
                      "y": 0.77879936
                    },
                    {
                      "x": 0.6285886,
                      "y": 0.77879936
                    }
                  ]
                }
              },
              {
                "mid": "/m/083wq",
                "name": "Wheel",
                "score": 0.6519385,
                "boundingPoly": {
                  "normalizedVertices": [
                    {
                      "x": 0.40014446,
                      "y": 0.5569999
                    },
                    {
                      "x": 0.5116857,
                      "y": 0.5569999
                    },
                    {
                      "x": 0.5116857,
                      "y": 0.6681271
                    },
                    {
                      "x": 0.40014446,
                      "y": 0.6681271
                    }
                  ]
                }
              }
            ]
          }
        ]
      },
      "found_objects": 1
    },
    {
      "solution_name": "Ibm",
      "execution_time": "2.564770",
      "result": {
        "image_path": "media/data/files/object_detection_oSDc5Rj.jpg",
        "labels": [
          "mountain bike",
          "bicycle",
          "wheeled vehicle",
          "vehicle",
          "Indian red color"
        ],
        "confidences": [
          0.902,
          0.957,
          0.957,
          0.957,
          0.97
        ],
        "x_mins": [
          null,
          null,
          null,
          null,
          null
        ],
        "x_maxs": [
          null,
          null,
          null,
          null,
          null
        ],
        "y_mins": [
          null,
          null,
          null,
          null,
          null
        ],
        "y_maxs": [
          null,
          null,
          null,
          null,
          null
        ]
      },
      "api_response": {
        "images": [
          {
            "classifiers": [
              {
                "classifier_id": "default",
                "name": "default",
                "classes": [
                  {
                    "class": "mountain bike",
                    "score": 0.902,
                    "type_hierarchy": "/vehicle/wheeled vehicle/bicycle/mountain bike"
                  },
                  {
                    "class": "bicycle",
                    "score": 0.957
                  },
                  {
                    "class": "wheeled vehicle",
                    "score": 0.957
                  },
                  {
                    "class": "vehicle",
                    "score": 0.957
                  },
                  {
                    "class": "Indian red color",
                    "score": 0.97
                  }
                ]
              }
            ],
            "image": "object_detection_oSDc5Rj.jpg"
          }
        ],
        "images_processed": 1,
        "custom_classes": 0
      },
      "found_objects": 1
    },
    {
      "solution_name": "Microsoft Azure",
      "execution_time": "1.432489",
      "result": {
        "image_path": "media/data/files/object_detection_oSDc5Rj.jpg",
        "labels": [
          "Bicycle wheel",
          "Bicycle wheel",
          "bicycle"
        ],
        "confidences": [
          0.613,
          0.53,
          0.919
        ],
        "x_mins": [
          0.06172839506172839,
          0.6331569664902998,
          0.06878306878306878
        ],
        "x_maxs": [
          0.43386243386243384,
          0.9559082892416225,
          0.9611992945326279
        ],
        "y_mins": [
          0.4215167548500882,
          0.4285714285714286,
          0.20105820105820105
        ],
        "y_maxs": [
          0.7760141093474426,
          0.7777777777777778,
          0.7795414462081129
        ]
      },
      "api_response": {
        "objects": [
          {
            "rectangle": {
              "x": 35,
              "y": 239,
              "w": 211,
              "h": 201
            },
            "object": "Bicycle wheel",
            "confidence": 0.613,
            "parent": {
              "object": "Wheel",
              "confidence": 0.908
            }
          },
          {
            "rectangle": {
              "x": 359,
              "y": 243,
              "w": 183,
              "h": 198
            },
            "object": "Bicycle wheel",
            "confidence": 0.53,
            "parent": {
              "object": "Wheel",
              "confidence": 0.893
            }
          },
          {
            "rectangle": {
              "x": 39,
              "y": 114,
              "w": 506,
              "h": 328
            },
            "object": "bicycle",
            "confidence": 0.919,
            "parent": {
              "object": "cycle",
              "confidence": 0.927,
              "parent": {
                "object": "Land vehicle",
                "confidence": 0.93,
                "parent": {
                  "object": "Vehicle",
                  "confidence": 0.93
                }
              }
            }
          }
        ],
        "requestId": "dd79e7d8-9db6-477f-8120-c3db09a07e40",
        "metadata": {
          "width": 567,
          "height": 567,
          "format": "Jpeg"
        }
      },
      "found_objects": 1
    },
```

</details>

## Blog articles
We provides on our website some [blog articles on AI engines](https://www.edenai.co/blog)

## Contact
If you have any question or request, you can contact us at contact@edenai.com

## Terms of use
You can access to our terms [here](https://www.edenai.co/terms) on our website.

#
![Screenshot](https://github.com/ai-compare/Speech_to_text-API/blob/ba9d4f1668d8758141f24240d1287640b4211c63/Logo%20complet%20Eden%20AI%20-%20format%20PNG.png)
