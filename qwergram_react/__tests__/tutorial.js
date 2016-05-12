jest.unmock('../js/tutorial1');

import React from 'react';
import ReactDOM from 'react-dom';
import TestUtils from 'react-addons-test-utils';
import CommentBox from '../js/tutorial1';

describe('CommentBox', () => {

  it('contains the right text', () => {
    // Render a checkbox with label in the document
    const checkbox = TestUtils.renderIntoDocument(
      <CommentBox />
    );

    const checkboxNode = ReactDOM.findDOMNode(checkbox);

    // Verify that it's Off by default
    // expect(checkboxNode.textContent).toEqual('Off');

    // Simulate a click and verify that it is now On
    // TestUtils.Simulate.change(
      // TestUtils.findRenderedDOMComponentWithTag(checkbox, 'input')
    // );

    expect(checkboxNode.children).toEqual('Hello World! I am a comment box!');
  });

});
