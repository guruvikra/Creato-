import requests
from typing import Dict, Any


def generate_hd_images(
    api_key:str,
    prompt:str,
    model_version:str="2.2",
    num_results:int=1,
    aspect_ratio:str="1:1",
    sync:bool=True,
    seed:int=None,
    negative_prompt:str="",
    steps_num:int=None,
    text_guidance_scale:float=None,
    medium:str=None,
    prompt_enhancement:bool=False,
    enhance_image:bool=False,
    content_moderation:bool=False,
    ip_signal:bool=False) -> Dict[str, Any]:
        """Generate HD image from prompt using Bria's text-to-image API."""
        
        if not prompt:
            raise ValueError("Prompt is required for image generation")
        
        data = {
            'prompt': prompt,
            'num_results': num_results,
            'sync': sync,
            'negative_prompt': negative_prompt
        }
        
        if aspect_ratio:
            data["aspect_ratio"] = aspect_ratio
        if seed is not None:
            data["seed"] = seed
        if steps_num is not None:
            data["steps_num"] = max(20, min(steps_num, 50))
        if text_guidance_scale is not None:
            data["text_guidance_scale"] = max(1.0, min(text_guidance_scale, 10.0))
        if medium:
            data["medium"] = medium
        if prompt_enhancement:
            data["prompt_enhancement"] = prompt_enhancement
        if enhance_image:
            data["enhance_image"] = enhance_image
        if content_moderation:
            data["content_moderation"] = content_moderation
        if ip_signal:
            data["ip_signal"] = ip_signal
            
        url = f'https://engine.prod.bria-api.com/v1/text-to-image/hd/{model_version}'
        headers = {
            'api_token': api_key,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        try:
            print(f"Making request to: {url}")
            print(f"Headers: {headers}")
            print(f"Data: {data}")
            
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            
            print(f"Response status: {response.status_code}")
            print(f"Response body: {response.text}")
            
            return response.json()
        except Exception as e:
            print(f"Error generating HD image: {str(e)}")
            return {"error": str(e)}  # Return error message in case of failure