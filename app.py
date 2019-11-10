import boto3, datetime
from chalice import Chalice
from boto3.dynamodb.conditions import Key, Attr

app = Chalice(app_name='scores')

def get_scores_table():
    dynamodb = boto3.resource('dynamodb')

    return dynamodb.Table('scores')


@app.route('/scores/create', methods=['POST'])
def score():
    data = app.current_request.json_body

    table = get_scores_table()

    table.put_item(Item={
        'game_id': data['game_id'],
        'score': data['score'],
        'username': data['username'],
        'timestamp': datetime.datetime.utcnow().isoformat()
    })

    return {
        'code': 'success'
    }


@app.route('/leaderboard')
def leaderboard():
    table = get_scores_table()

    response = table.query(KeyConditionExpression=Key('game_id').eq(1), ScanIndexForward=False)


    return {
        'code': 'success',
        'results': response['Items']
    }

@app.route('/scores/{username}')
def user_scores(username):
    table = get_scores_table()

    response = table.scan(
        FilterExpression=Attr('username').eq(username)
    )

    return {
        'code': 'success',
        'results': response['Items']
    }