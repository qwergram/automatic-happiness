// main.js

var api_endpoints = {
  "ideas": "http://ec2-54-187-86-84.us-west-2.compute.amazonaws.com/api/v1/ideas/?format=json",
  "articles": "http://ec2-54-187-86-84.us-west-2.compute.amazonaws.com/api/v1/articles/?format=json",
  "shares": "http://ec2-54-187-86-84.us-west-2.compute.amazonaws.com/api/v1/shares/?format=json",
}

var IdeasBox = React.createClass({
  getInitialState: function() {
    return {data: [{
      'title': 'Hold on... grabbing the good stuff.',
      'pitch': '',
      'url': '',
      'date_created': '',
    }]};
  },
  loadIdeasFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: "json",
      cache: false,
      success: function(data) {
        if (this.props.latest) {
          this.setState({data: [data['results'][0]]});
        } else {
          this.setState({data: data['results']});
        }
      }.bind(this),
      error: function(xhr, status, err) {
        console.log("oops!", xhr, status, err);
      }.bind(this),
    });
  },
  componentDidMount: function() {
    this.loadIdeasFromServer();
    if (this.props.pollInterval) {
      setInterval(this.loadIdeasFromServer, this.props.pollInterval);
    };
  },
  render: function() {
    if (this.props.latest){
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
    } else {
      return (
        <div className="ideas">
          {
            this.state.data.map(function(idea) {
              return (
                <article className="post">
                  <header>
                    <div className="title">
                      <h2><a href="#">{idea['title']}</a></h2>
                    </div>
                    <div className="meta">
                      <time className="published" datetime={idea['date_created']}>
                        {idea['date_created'].split('T')[0]}
                      </time>
                      <a href="#" className="author">
                        <span className="name">
                          qwergram
                        </span>
                        <img src="images/avatar.jpg" alt="" />
                      </a>
                    </div>
                  </header>
                  <p>{idea['pitch']}</p>
                  <footer>
                    <ul className="actions">
                      <li><a href="#" className="button big">Continue Reading</a></li>
                    </ul>
                    <ul className="stats">
                      <li><a href="#">General</a></li>
                    </ul>
                  </footer>
                </article>
              )
            })
          }
        </div>
      );
    }
  }
});

var render_ideas = function() {
  var url = api_endpoints['ideas']
  ReactDOM.render(
    <IdeasBox url={url} pollInterval={60000}/>,
    document.getElementById('content')
  )
  ReactDOM.render(
    <IdeasBox url={url} latest={true}/>,
    document.getElementById('latest-links')
  )
};

render_ideas();
