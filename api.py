from flask import Flask, jsonify
import discordwebhook
app = Flask(__name__)
hook = discordwebhook.Webhook(url='https://discord.com/api/webhooks/1043796010834608178/zLMVOVYIq_K6cumFn51HZKMDDLGIceuShbHgINd6H_nQovHOHP8Bc6VQkNp9tCgXEI3b')
@app.route('/api/v1.0/reloadState/<string:State>', methods=['GET'])
def state(State):
    hook.send_sync(content=State)
    return jsonify({"newState": State})
if __name__ == "__main__":
    port_nr = int(os.environ.get("PORT", 5001))
    app.run(port=port_nr, host='0.0.0.0', debug=False)
