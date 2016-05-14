// main.js
var ArticlesBox = React.createClass({
  getInitialState: function() {
    return {data: []};
  },
  loadArticlesFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: "json",
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.log("Oops!", xhr, status, err);
      }.bind(this),
    });
  },
  componentDidMount: function() {
    this.loadArticlesFromServer();
    // setInterval(this.loadArticlesFromServer, this.props.pollInterval);
  },
  render: function() {
    return (
      <pre><code>{this.state.data}</code></pre>
    );
  }
});

ReactDOM.render(
  <ArticlesBox url="http://ec2-54-187-86-84.us-west-2.compute.amazonaws.com/api/v1/ideas/?format=json" pollInterval={2000} />,
  document.getElementById('content')
)
