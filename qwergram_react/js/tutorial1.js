// tutorial1.js
import React from 'react';
import ReactDOM from 'react-dom';

var CommentBox = React.createClass({
  render: function() {
    return (
      <div className="commentBox">
        Hello World! I am a comment box!
      </div>
    );
  }
});
ReactDOM.render(
  <CommentBox />,
  document.getElementById('content')
)
