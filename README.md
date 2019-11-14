# Flappy Bird Leaderboard API

https://docs.google.com/document/d/1ory-ypsUihfoD8Dh-k_Fcfnu6nhvrlStJB0A1hGCQmE/edit?usp=sharing

## AWS Chalice

This API is built with AWS Chalice. Below are screencasts to learn more about getting started with AWS Chalice:

### Chalice Tutorial Screencast

Part 1 - https://www.youtube.com/watch?v=me-v7BCaZH0

Part 2 - https://www.youtube.com/watch?v=mRuBtE057aM

## API Endpoints

### Base API URL

https://le0zofexj7.execute-api.us-west-2.amazonaws.com/api

## Leaderboard 

returns all game scores, highest first

### GET /leaderboard

```
curl https://le0zofexj7.execute-api.us-west-2.amazonaws.com/api/leaderboard
```

## User Scores

Returns all scores for a particular username

### GET /scores/{username}

```
curl https://le0zofexj7.execute-api.us-west-2.amazonaws.com/api/scores/larry
```

## Create Score

### POST /scores/create

Content-Type application/json

Example Payload:

{
	"game_id": 1,
	"score": 123,
	"username": "john"
}

Example:

```
curl -d '{"game_id": 1, "score": 789, "username": "john"}' -H "Content-Type: application/json" -X POST https://le0zofexj7.execute-api.us-west-2.amazonaws.com/api/scores/create
```


