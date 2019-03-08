function makeSummaryRequest(myJSON){
    var headers = {
      "Content-Type": "application/json",                                                                                                
      "Access-Control-Origin": "*"
   }
  
  fetch("http://localhost:5000/summary", {
    method: "POST",
    headers: headers,
    body:  JSON.stringify(myJSON)
  })
  .then(function(response){ 
    return response.json();
  })
  .then(function(myJson){
    // const mySum = JSON.stringify(myJson)
    const mySum = myJson
    console.log(mySum.summary)
    return mySum.summary
  })
  }
  
  export default makeSummaryRequest;
