// main.js
var ArticlesBox = React.createClass({
  getInitialState: function() {
    return {data: [{'title': 'Loading...', 'pitch': '', 'url': ''}]};
  },
  loadArticlesFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: "json",
      cache: false,
      success: function(data) {
        this.setState({data: data['results']});
      }.bind(this),
      error: function(xhr, status, err) {
        console.log("Oops!", xhr, status, err);
      }.bind(this),
    });
  },
  componentDidMount: function() {
    this.loadArticlesFromServer();
    setInterval(this.loadArticlesFromServer, this.props.pollInterval);
  },
  render: function() {
    console.log(this.state.data)
    var ArticleNodes = this.state.data.map(function(article) {
      return (
        <div>
          <h2>{article}</h2>
        </div>
      );
    });
    return (
      <div className="articles">
        {
          this.state.data.map(function(article) {
            return (
              <div className='article-node'>
                <h2>{article['title']}</h2>
                <p>{article['pitch']}</p>
              </div>
            )
          })
        }
      </div>
    );
  }
});

ReactDOM.render(
  <ArticlesBox url="http://ec2-54-187-86-84.us-west-2.compute.amazonaws.com/api/v1/ideas/?format=json" pollInterval={2000} />,
  document.getElementById('content')
)
