// main.js
var IdeasBox = React.createClass({
  getInitialState: function() {
    return {data: [{'title': 'Loading...', 'pitch': '', 'url': ''}]};
  },
  loadIdeasFromServer: function() {
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
    this.loadIdeasFromServer();
    setInterval(this.loadIdeasFromServer, this.props.pollInterval);
  },
  render: function() {
    return (
      <div className="ideas">
        {
          this.state.data.map(function(idea) {
            return (
              <div className='idea-node'>
                <h2>{idea['title']}</h2>
                <p>{idea['pitch']}</p>
              </div>
            )
          })
        }
      </div>
    );
  }
});

ReactDOM.render(
  <IdeasBox url="http://ec2-54-187-86-84.us-west-2.compute.amazonaws.com/api/v1/ideas/?format=json" pollInterval={2000} />,
  document.getElementById('content')
)
