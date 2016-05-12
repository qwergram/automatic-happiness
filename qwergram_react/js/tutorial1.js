// tutorial1.js
var CommentBox = React.createClass({
  render: function() {
    return (
      <div className="commentBox">
        Hello World! I am a comment box!
      </div>
    );
  }
});

function render() {
  ReactDOM.render(
    <CommentBox />,
    document.getElementById('content')
  );
}
