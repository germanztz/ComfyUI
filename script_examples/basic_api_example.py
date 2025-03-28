import json
from urllib import request

#This is the ComfyUI api prompt format.

#If you want it for a specific workflow you can "enable dev mode options"
#in the settings of the UI (gear beside the "Queue Size: ") this will enable
#a button on the UI to save workflows in api format.

#keep in mind ComfyUI is pre alpha software so this format will change a bit.

#this is the one for the default workflow
prompt_text = """
{
  "6": {
    "inputs": {
      "text": "",
      "clip": [
        "30",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Positive Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "31",
        0
      ],
      "vae": [
        "30",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "9": {
    "inputs": {
      "filename_prefix": "ComfyUI",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  },
  "27": {
    "inputs": {
      "width": 512,
      "height": 512,
      "batch_size": 1
    },
    "class_type": "EmptySD3LatentImage",
    "_meta": {
      "title": "EmptySD3LatentImage"
    }
  },
  "30": {
    "inputs": {
      "ckpt_name": "flux1-dev-fp8.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "31": {
    "inputs": {
      "seed": 805528666240043,
      "steps": 20,
      "cfg": 1,
      "sampler_name": "euler",
      "scheduler": "simple",
      "denoise": 1,
      "model": [
        "30",
        0
      ],
      "positive": [
        "35",
        0
      ],
      "negative": [
        "33",
        0
      ],
      "latent_image": [
        "27",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "33": {
    "inputs": {
      "text": "",
      "clip": [
        "30",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Negative Prompt)"
    }
  },
  "35": {
    "inputs": {
      "guidance": 3.5,
      "conditioning": [
        "6",
        0
      ]
    },
    "class_type": "FluxGuidance",
    "_meta": {
      "title": "FluxGuidance"
    }
  }
}
"""

def queue_prompt(prompt):

    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    print(p)
    req =  request.Request("http://127.0.0.1:8188/prompt", data=data)
    request.urlopen(req)


prompt = json.loads(prompt_text)
#set the text prompt for our positive CLIPTextEncode
prompt["6"]["inputs"]["text"] = "masterpiece best quality man"

#set the seed for our KSampler node
prompt["31"]["inputs"]["seed"] = 5


queue_prompt(prompt)


