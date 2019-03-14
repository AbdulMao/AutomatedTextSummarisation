function makeSummaryRequest(myJSON){
    var headers = {
      "Content-Type": "application/json",                                                                                                
      "Access-Control-Origin": "*"
   }
  
  return fetch("http://localhost:5000/summary", {
    method: "POST",
    headers: headers,
    body:  JSON.stringify(myJSON)
  })
  .then(function(response){ 
    return response.json();
  })
  }
  
  export default makeSummaryRequest;
