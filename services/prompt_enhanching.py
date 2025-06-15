import  requests


def enhance_prompt(api_key: str, prompt: str):
    """"Enhance a text prompt using the Bria API."""
    
    url ='https://engine.prod.bria-api.com/v1/prompt_enhancer'
    headers = {
        'api_token': api_key,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt':prompt
    }
    
    try:
        req = requests.post(url=url,headers=headers, json=data)
        if req.status_code == 200:
            res = req.json()
            return {
                "prompt": prompt,
                "enhanced_prompt": res.get("prompt variations", prompt),
                "msg": "Prompt enhanced successfully"
            }
        else:
            return {
                "prompt": prompt,
                "msg": f"Failed to enhance prompt: {req.text}"
            }
        
    except Exception as e:
        print(f"Error enhancing prompt: {str(e)}")
        return {
            "prompt": prompt,
            "msg": "Failed to enhance prompt"
        }