# Flappy Bird High Scores API

https://docs.google.com/document/d/1ory-ypsUihfoD8Dh-k_Fcfnu6nhvrlStJB0A1hGCQmE/edit?usp=sharing

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
curl https://le0zofexj7.execute-api.us-west-2.amazonaws.com/api/leaderboard
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


