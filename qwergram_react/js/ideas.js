// main.js

var api_endpoints = {
  "ideas": "http://ec2-54-187-86-84.us-west-2.compute.amazonaws.com/api/v1/ideas/?format=json",
  "articles": "http://ec2-54-187-86-84.us-west-2.compute.amazonaws.com/api/v1/articles/?format=json",
  "shares": "http://ec2-54-187-86-84.us-west-2.compute.amazonaws.com/api/v1/shares/?format=json",
  "repos": "http://ec2-54-187-86-84.us-west-2.compute.amazonaws.com/api/v1/repos/?format=json",
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
                      <a href="#me" className="author">
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


var SharesBox = React.createClass({
  getInitialState: function() {
    return {data: [{
      'title': 'loading...',
      'link': 'http://qwergram.github.com/',
      'short_description': 'Give me a sec...',
    }]};
  },
  loadSharesFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: "json",
      cache: false,
      success: function(data) {
        this.setState({data: data['results']});
      }.bind(this),
      error: function(xhr, status, err) {
        console.log("oops!", xhr, status, err);
      }.bind(this),
    });
  },
  componentDidMount: function() {
    this.loadSharesFromServer();
    if (this.props.pollInterval) {
      setInterval(this.loadSharesFromServer, this.props.pollInterval);
    };
  },
  render: function() {
    return (
      <div>
        {
          this.state.data.map(function(share) {
            return (
              <article className="mini-post">
                <header>
                  <a href={share['link']}>
                    <h3>{share['title']}</h3>
                    <p>{share['short_description']}</p>
                  </a>
                </header>

              </article>
            )
          })
        }
      </div>
    );
  }
});

var render_shares = function() {
  var url = api_endpoints['shares'];
  ReactDOM.render(
    <SharesBox url={url}/>,
    document.getElementById('mini-posts')
  );
};


var RepoBox = React.createClass({
  getInitialState: function() {
    return {data: [{
      'title': 'Getting latest repositories...',
      'link': 'http://qwergram.github.com/',
      'short_description': 'Hold on...',
      'updated_at': 'T',
      'full_name': '../..'
    }]};
  },
  loadReadmeFromGithubServer: function(url) {
    readme = "Error getting data...";
    $.ajax({
      url: url,
      cache: false,
      success: function(data) {
        readme = data;
      }.bind(this),
      error: function(xhr, status, err) {
        console.log("oops!", xhr, status, err)
      }.bind(this),
    });
    console.log(readme)
    return readme;
  },
  loadReposFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: "json",
      cache: false,
      success: function(data) {
        data[0]['readme'] = this.loadReadmeFromGithubServer(data[0]['readme']);
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.log("oops!", xhr, status, err);
      }.bind(this),
    });
  },
  componentDidMount: function() {
    this.loadReposFromServer();
    if (this.props.pollInterval) {
      setInterval(this.loadReposFromServer, this.props.pollInterval);
    };
  },
  render: function() {
    return (
      <div>
        {
          this.state.data.map(function(idea) {
            return (
              <article className="post">
                <header>
                  <div className="title">
                    <h2><a href="#">{idea['full_name'].split('/')[1]}</a></h2>
                    <strong>{idea['description']}</strong>
                  </div>
                  <div className="meta">
                    <time className="published" datetime={idea['updated_at']}>
                    </time>
                    <a href="#me" className="author">
                      <span className="name">
                        {idea['full_name'].split('/')[0]}
                      </span>
                      <img src="images/avatar.jpg" alt="" />
                    </a>
                  </div>
                </header>
                <p>{idea['readme']}
                </p>
                <footer>
                  <ul className="actions">
                    <li><a href={idea['html_url']} className="button big">View the Repo</a></li>
                  </ul>
                  <ul className="stats">
                    <li><a href="#">Repo</a></li>
                  </ul>
                </footer>
              </article>
            )
          })
        }
      </div>
    );
  }
});


var render_repos = function() {
  var url = api_endpoints['repos'];
  ReactDOM.render(
    <RepoBox url={url}/>,
    document.getElementById('content')
  );
};


var UrlBox = React.createClass({
  render: function() {
    return (
      <ul>
        <li><a href="#" onClick={this.renderHome}>Ideas</a></li>
        <li><a href="#repos" onClick={this.renderRepos}>Repos</a></li>
      </ul>
    );
  },
  renderHome: function(event) {
    console.log('Render Home')
    render_ideas();
    render_shares();
  },
  renderRepos: function(event) {
    console.log('Render Repos')
    render_repos();
  },
});


var render_urls = function() {
  ReactDOM.render(
    <UrlBox/>,
    document.getElementById('links')
  );
}

render_ideas();
render_shares();
render_urls();
