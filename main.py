
import requests
from bs4 import BeautifulSoup
from langchain_groq import ChatGroq

def main():
    respond = requests.get("https://www.tensorflow.org/")
    fetch_website_content = BeautifulSoup(respond.text, 'html.parser')
    system_prompt="""
    You are a snarky assisstant that analyzes contents of websites,
    and provide a short , snarky , humorous summary , ignoring text
    that might be navigation related. Respond in markdown . Do not wrap the markdown in a code block - respond just with the markdown"""
    user_prompt="""
    Here are the contents of a website.
    Provide a short summary of this website.
    If it includes news or announcements, then summarize these too.
    """
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt + fetch_website_content.get_text()}
    ]
    response = ChatGroq(model="llama-3.3-70b-versatile",temperature=0)
    print("Response from Groq LLM: \n", response.choices[0].message.content)

if __name__=="__main__":
    main()
