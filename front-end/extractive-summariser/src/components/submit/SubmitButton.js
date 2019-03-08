import React, { Component } from 'react';
import makeSummaryRequest from './SummaryRequest.js';
import makeTopicRequest from './TopicRequest.js';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';


const styles = theme => ({
  button: {
    margin: theme.spacing.unit,
  },
  input: {
    display: 'none',
  },
});

function onClick(){
  const text = document.querySelector(".textbox").value;
  var myJSON = {"text": text };
  makeSummaryRequest(myJSON);
  makeTopicRequest(myJSON);
  console.log(myJSON)
}

function SubmitButton(props){
  const { classes } = props;
    return (
      <Button onClick={onClick} variant="contained" color="secondary" className={classes.button} id = "submitButton">
        Submit
      </Button>
    );
}

SubmitButton.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(SubmitButton);
