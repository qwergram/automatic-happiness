jest.unmock('../js/tutorial1');

import React from 'react';
import ReactDOM from 'react-dom';
import TestUtils from 'react-addons-test-utils';

describe('CommentBox', () => {

  it('check sanity', () => {
    expect(true).toBe(true);
  })

  it('has children', () => {
    var commentBox = TestUtils.renderIntoDocument(React.createElement("CommentBox"));
    var commentBoxNode = ReactDOM.findDOMNode(commentBox);
    var hit_this = commentBoxNode.children;
    console.log(hit_this, 'adsfkladshglshdlkgsdlgjdaslgjsdaklg');
    expect(hit_this).not.toEqual(undefined);
    expect(hit_this).not.toEqual(null);
  });

  // it('has text', () => {
  //   var commentBox = TestUtils.renderIntoDocument(React.createElement("CommentBox"));
  //   var commentBoxNode = ReactDOM.findDOMNode(commentBox);
  //   var hit_this = commentBox.render;
  //   console.log(hit_this, 'adsfkladshglshdlkgsdlgjdaslgjsdaklg');
  //   expect(hit_this).not.toEqual(undefined);
  //   expect(hit_this).not.toEqual(null);
  // });

});
