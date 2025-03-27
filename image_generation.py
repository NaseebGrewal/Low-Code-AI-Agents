"""
This script demonstrates how to use the Flux API to generate images based on a list of prompt descriptions.
file: image_generation.py
"""

# Importing the required libraries
import os
import asyncio
import aiohttp

# Load the API key from the .env file
from dotenv import load_dotenv

# Import the raw prompt text
from raw_prompt_text import raw_prompt_text

load_dotenv()

# Replace with your actual API key
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable is not set.")

# Ensure the Images directory exists
images_dir = "Images"
os.makedirs(images_dir, exist_ok=True)

# Global headers for the API requests
headers = {
    "Content-Type": "application/json",
    "x-key": API_KEY
}

# Process the raw prompt text into a list of prompt titles and descriptions
def process_raw_prompt_text(prompt_text)->tuple:
    """
    This function takes in a raw prompt text and returns a tuple of two lists: prompt_titles and prompt_descriptions.
    param raw_prompt_text: str
    return: tuple
    """
    image_prompts= prompt_text.split("\n\n")
    prompt_titles = []
    prompt_descriptions = []
    for prompt in image_prompts:
        prompt = prompt.split(":")
        prompt_titles.append(prompt[0])
        prompt_descriptions.append(prompt[1].strip())
    return prompt_titles, prompt_descriptions


async def post_request_flux(session, prompt_description)->str:
    """
    This function sends a POST request to the Flux API to generate an image based on the given prompt description.
    param session: aiohttp.ClientSession
    param prompt_description: str
    return: str
    """
    post_url = "https://api.bfl.ml/v1/flux-pro-1.1"
    payload = {"prompt": prompt_description}
    async with session.post(post_url, headers=headers, json=payload) as response:
        if response.status == 200:
            data = await response.json()
            image_id = data.get('id')
            if not image_id:
                print("No image ID found in the response.")
                return None
            print(f"Image request submitted. ID: {image_id}")
            return image_id
        else:
            text = await response.text()
            print(f"Error in POST request: {response.status}\n{text}")
            return None


async def get_request(session, image_id)->str:
    """
    This function sends a GET request to the Flux API to/
      retrieve the image URL based on the given image ID.
    param session: aiohttp.ClientSession
    param image_id: str
    return: str
    """
    get_url = f"https://api.bfl.ml/v1/get_result?id={image_id}"
    async with session.get(get_url, headers=headers) as response:
        if response.status == 200:
            data = await response.json()
            image_url = data.get("result", {}).get("sample")
            if not image_url:
                print("Image URL not found in the response.")
                return None
            print(f"Image URL retrieved: {image_url}")
            return image_url
        else:
            text = await response.text()
            print(f"Error in GET request: {response.status}\n{text}")
            return None


async def get_image(session, image_url, prompt)->None:
    """
    This function downloads the image from the given URL and saves it to the Images directory.
    param session: aiohttp.ClientSession
    param image_url: str
    param prompt: str
    return: None
    """
    async with session.get(image_url) as response:
        if response.status == 200:
            image_bytes = await response.read()
            image_name = f"{prompt}.jpeg"
            output_filename = os.path.join(images_dir, image_name)
            with open(output_filename, "wb") as img_file:
                img_file.write(image_bytes)
            print(f"Image downloaded and saved as {output_filename}")
        else:
            text = await response.text()
            print(f"Error retrieving the image: {response.status}\n{text}")


async def process_prompt(session, prompt, prompt_description)->None:
    """
    This function processes a single prompt by sending a POST request to the Flux API,/
      retrieving the image URL, and downloading the image.
    param session: aiohttp.ClientSession
    param prompt: str
    param prompt_description: str
    return: None
    """
    print(f"Prompt Title: {prompt}")
    print(f"Prompt Description: {prompt_description}\n")
    
    image_id = await post_request_flux(session, prompt_description)
    # if not image_id:
    #     return
    
    print("Waiting for 10 seconds to allow image generation...")
    await asyncio.sleep(10)  # asynchronous sleep

    image_url = await get_request(session, image_id)
    if not image_url:
        return
    
    await get_image(session, image_url, prompt)
    print("\n----------------------------------------------------\n")

async def main()->None:
    """
    This is the main function that processes a list of prompts concurrently.
    return: None
    """

    # Use the global prompt lists
    prompt_titles, prompt_descriptions = process_raw_prompt_text(raw_prompt_text)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for prompt, description in zip(prompt_titles, prompt_descriptions):
            tasks.append(process_prompt(session, prompt, description))
        # Run all prompt processes concurrently
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
