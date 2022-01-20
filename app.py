from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view():
		return "
	<h1>Hello World</h1>
	
	<script>
  window.watsonAssistantChatOptions = {
      integrationID: "55f500c2-755a-4a89-94d0-58b4e426d863", // The ID of this integration.
      region: "us-south", // The region your integration is hosted in.
      serviceInstanceID: "67c9f3f5-3350-4d8b-b6ea-15d2c487050c", // The ID of your service instance.
      onLoad: function(instance) { instance.render(); }
    };
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js"
    document.head.appendChild(t);
  });
</script>
"
	
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
