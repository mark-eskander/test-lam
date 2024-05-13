from llamaapi import LlamaAPI
from openai import OpenAI
from fastapi import FastAPI
import uvicorn

app = FastAPI( debug = True)

def check_for_positive(review):
        if "positive" in review.lower():
            return 1
        else:
            return 0

client = OpenAI(
    api_key="LL-1RC7LxETXTYzdwml76VfaP4ynaZunA7vsXXOTL9n0gMzuGB2VnJgb85xhAMKmlnv",
    base_url="https://api.llama-api.com"
)

@app.get('/predict/{rev}' , status_code=200)
def predict(rev : str):
    response = client.chat.completions.create(
    model="llama-13b-chat",
    messages=[
        {"role": "system", "content": "translate to english then Mention positive as the first word if the next sentiment is positive otherwise write negative the first word if the sentiment is negative "},
        {"role": "user", "content": rev }   

    ])

    review = response.choices[0].message.content
            
    return {'prediction is' : check_for_positive(review)}


    # Run through terminal
if __name__== '__main__' :
    uvicorn.run(app,host='127.0.0.1',port=8000)


# client = OpenAI(
#     api_key="LL-1RC7LxETXTYzdwml76VfaP4ynaZunA7vsXXOTL9n0gMzuGB2VnJgb85xhAMKmlnv",
#     base_url="https://api.llama-api.com"
# )

# response = client.chat.completions.create(
#     model="llama-13b-chat",
#     messages=[
#         {"role": "system", "content": "translate to english then Mention positive as the first word if the next sentiment is positive otherwise write negative the first word if the sentiment is negative "},
#         {"role": "user", "content": input("Write your review: ") }   

#     ]
# )

# review = response.choices[0].message.content


# def check_for_positive(review):
#     if "positive" in review.lower():
#         print("positive review")
#     else:
#         print("negative review")
        
# check_for_positive(review)
