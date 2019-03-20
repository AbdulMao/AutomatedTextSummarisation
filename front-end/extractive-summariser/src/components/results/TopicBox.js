import React, { Component } from 'react';

function TopicBox(props) {
    return (
      <div className="topic-box">
        <p className="topic-header">Topics detected:</p>
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
