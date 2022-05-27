from fastapi import FastAPI

from routes import route_auth, route_tweets, route_users

app = FastAPI()


@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}


app.include_router(route_auth.router, prefix="/auth", tags=["Auth"])
app.include_router(route_users.router, prefix="/users", tags=["Users"])
app.include_router(route_tweets.router, prefix="/tweets", tags=["Tweets"])
