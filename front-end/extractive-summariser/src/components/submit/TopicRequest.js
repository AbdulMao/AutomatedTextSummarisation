function makeTopicRequest(myJSON){
    var headers = {
      "Content-Type": "application/json",                                                                                                
      "Access-Control-Origin": "*"
   }
  
  fetch("http://localhost:9000/topic", {
    method: "POST",
    headers: headers,
    body:  JSON.stringify(myJSON)
  })
  .then(function(response){ 
    return response.json();
  })
  .then(function(myJson){
    const myTopics = myJson
    console.log(myTopics.topics)
    return myTopics.topics
  })
  }
  
  export default makeTopicRequest;