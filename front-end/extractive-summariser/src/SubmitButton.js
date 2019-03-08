import React, { Component } from 'react';
import './App.css';
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

function dothis(){
  const text = document.querySelector(".textbox").value;
  console.log(text)
}

function SubmitButton(props){
  const { classes } = props;
    return (
      <Button onClick={dothis} variant="contained" color="secondary" className={classes.button} id = "submitButton">
        Submit
      </Button>
    );
}

SubmitButton.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(SubmitButton);
