function makeRequest(myJSON){
    var headers = {
      "Content-Type": "application/json",                                                                                                
      "Access-Control-Origin": "*"
   }
   var data = {
    "email": "peter@klaven",
    "password": "cityslicka"
  }
  
  fetch("http://localhost:5000/summary", {
    method: "POST",
    headers: headers,
    body:  JSON.stringify(myJSON)
  })
  .then(function(response){ 
    console.log(response.json())
  })
  }
  
  export default makeRequest;
