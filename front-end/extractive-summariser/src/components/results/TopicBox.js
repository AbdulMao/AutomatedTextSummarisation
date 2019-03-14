import React, { Component } from 'react';

function TopicBox(props) {
  console.log("TOPIC BOX")
  console.log(props.topics)
    return (
      <div className="topic-box">
        <ul>
            {(props.topics).map(topic => createTopicList(topic))}
        </ul>
            
      </div>
    );
}

function createTopicList(topicList){
  return <li>{topicList}</li>
}

export default TopicBox;
