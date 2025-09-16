def get_prompt():
    return (
        f"You are an expert in diagrams, flowcharts, and technical images.\n"
        "Your goal is to assess whether a given image is technically correct and propose improvements to readability, flow, etc.\n"
        "You should return a JSON object with two fields:\n"
        "{'is_valid': a boolean indicating if the image is technically correct, 'issues': a string describing any issues found or 'None' if there are no issues.}\n"
    )
