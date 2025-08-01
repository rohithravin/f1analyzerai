from fastapi import FastAPI
from fastf1_extractor.dummy import echo  # adjust based on your structure

app = FastAPI()


@app.get("/")
def root():
    "Root endpoint to check if the server is running."
    return {"message": "F1 API Server is live!"}


@app.get("/echo")
def echo_message(
    value: str = "This is a dummy function that does nothing but print a message.",
):
    "Endpoint to call the dummy echo function."
    return {"message": echo(value)}
