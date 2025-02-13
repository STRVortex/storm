import os
import logging
from flask import Flask
from flask_restful import Resource, Api

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the Flask app
def create_app():
    app = Flask(__name__)
    api = Api(app)

    # Define a simple resource
    class Greeting(Resource):
        def get(self):
            logger.info("ɢʀᴇᴇᴛɪɴɢ ᴇɴᴅᴘᴏɪɴᴛ ᴡᴀꜱ ʀᴇᴀʜᴇᴅ")
            return "ꜱᴛᴏʀᴍ ɪꜱ ᴜᴘ ᴀɴᴅ ʀᴇᴀᴅʏ ꜰᴏʀ ᴅᴇꜱᴛʀᴜᴄᴛɪᴏɴ!"

    # Register the Greeting resource at the root endpoint
    api.add_resource(Greeting, '/')

    return app

# Only run the app if this script is executed directly
if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 8080))  # Set port from environment variable or default to 8080
    logger.info(f"ꜱᴛᴀʀᴛɪɴɢ ꜱᴇʀᴠᴇʀ ᴏɴ ᴘᴏʀᴛ {port}")
    app.run(host="0.0.0.0", port=port)
