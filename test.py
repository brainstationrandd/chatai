import json
import requests

def test_function():
    # Default question for testing
    content = "Tell me about srk"
    
    # API endpoint
    api_url = 'http://35.211.66.55:1066/qna'
    
    # Prepare the payload
    payload = {
        "question": content
    }
    
    try:
        # Send the POST request to the external API
        response = requests.post(api_url, json=payload)
        
       
        
        # Check if the request was successful
        if response.status_code == 200:
            api_response = response.json()
        else:
            api_response = {"answer": "Sorry, there was an issue with the external service."}
    
    except Exception as e:
        api_response = {"answer": f"Error occurred: {str(e)}"}
    
    # Print the response
    print(api_response)

# Run the test function
if __name__ == "__main__":
    test_function()
