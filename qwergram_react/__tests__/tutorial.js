jest.unmock('../js/tutorial21');

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
    expect(hit_this).not.toEqual(undefined);
    expect(hit_this).not.toEqual(null);
  });

  it('is mounted', () => {
    var commentBox = TestUtils.renderIntoDocument(React.createElement("CommentBox"));
    var hit_this = commentBox.isMounted;
    expect(hit_this).not.toEqual(undefined);
    expect(hit_this).not.toEqual(null);
  });

  it('has a state', () => {
    var commentBox = TestUtils.renderIntoDocument(React.createElement("CommentBox"));
    var hit_this = commentBox;
    expect(hit_this).not.toEqual(undefined);
    expect(hit_this).not.toEqual(null);
  });

});
