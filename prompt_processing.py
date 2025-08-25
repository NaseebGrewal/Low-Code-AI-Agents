"""
This module contains a function that processes raw prompt text and returns a tuple of two lists: prompt_titles and prompt_descriptions.
file: prompt_processing.py
"""

def process_raw_prompt_text(raw_prompt_text)->tuple:
    """
    This function takes in a raw prompt text and returns a tuple of two lists: prompt_titles and prompt_descriptions.
    param raw_prompt_text: str
    return: tuple
    """
    image_prompts= raw_prompt_text.split("\n\n")
    prompt_titles = []
    prompt_descriptions = []
    for prompt in image_prompts:
        prompt = prompt.split(":")
        prompt_titles.append(prompt[0])
        prompt_descriptions.append(prompt[1].strip())
    return prompt_titles, prompt_descriptions


