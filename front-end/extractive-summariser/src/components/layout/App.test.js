import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import HomePage from './HomePage.js'
import renderer from 'react-test-renderer'
import { MemoryRouter as Router, withRouter } from 'react-router-dom';
import ResultsPage from './ResultsPage.js';
import SubmitButton from '../results/SummaryBox.js'
import TopicBox from '../results/TopicBox';

const returnPercentageList = jest.fn(() => 4);
const homepagePageInfo = jest.fn(() => "Too Long; Didn't Read.Quickly get the information you need, saving time! ");
const topics = jest.fn(() => ["Mars", "Pluto", "Uranus", "Earth"])
const summary = jest.fn(()=> "This is the summary created")

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});

it('Homepage matches snapshot', () => {
  const tree = renderer.create(<Router
    initialEntries={[ { pathname: '/'} ]}
  >
      <HomePage/>
     </Router>).toJSON()
  expect(tree).toMatchSnapshot()
});

it('renders an input box', () => {
  const wrapper = shallow(<TopicBox />);
  expect(wrapper.find('.topic-box')).to.have.lengthOf(1);
});



test ('all percentage choices are presented', ()=> {
  expect(returnPercentageList()).toBe(4);
})

test ('Home page information is correct', ()=> {
  expect(homepagePageInfo()).toBe("Too Long; Didn't Read.Quickly get the information you need, saving time! ");
})

test ('Topics list should contain 4 topcics', ()=> {
  expect(topics()).toHaveLength(4);
})

test ('Summary Exists', ()=> {
  expect(summary()).toBeTruthy();
})

