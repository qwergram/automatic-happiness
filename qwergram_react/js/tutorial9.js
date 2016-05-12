// tutorial9.js
var CommentList = React.createClass({
  render: function() {
    var commentNodes = this.props.data.map(function(comment) {
      return (
        <Comment author={comment.author} key={comment.id}>
          {comment.text}
        </Comment>
      );
    });
    return (
      <div className="commentList">
        {commentNodes}
      </div>
    );
  }
});

var CommentForm = React.createClass({
  render: function() {
    return (
      <div className="commentForm">
        Hello World! I am a comment Form!
      </div>
    );
  }
});

var Comment = React.createClass({
  rawMarkup: function() {
    var rawMarkup = marked(this.props.children.toString(), {sanitize: true});
    return { __html: rawMarkup }
  },
  render: function() {
    return (
      <div className="comment">
        <h2 className="commentAuthor">
          {this.props.author}
        </h2>
        <span dangerouslySetInnerHTML={this.rawMarkup()} />
      </div>
    );
  }
});

var CommentBox = React.createClass({
  render: function() {
    return (
      <div className="commentBox">
        <h1>Comment Box</h1>
        <CommentList data={this.props.data}/>
        <CommentForm />
      </div>
    );
  }
});

// tutorial8.js
var data = [
  {id: 1, author: "Norton Pengra", text: "`print(\"Hello World!\")`"},
  {id: 2, author: "Oliver Collins", text: "Python is *the coolest language*"}
];

ReactDOM.render(
  <CommentBox data={data}/>,
  document.getElementById('content')
)
