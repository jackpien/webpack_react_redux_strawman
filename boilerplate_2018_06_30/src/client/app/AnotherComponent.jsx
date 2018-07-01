
import React from 'react';

class AwesomeComponent extends React.Component {

  constructor(props) {
    super(props);
    this.state = {likesCount : 0};
    //this.onLike = this.onLike.bind(this);
  }

  // Fat arrow operator binds this which makes it unnecessary to explicitly 
  // bind in constructor
  // onLike() {...} turns into onLike = () => {...}
  onLike = () => {
    let newLikesCount = this.state.likesCount + 1;
    this.setState({likesCount: newLikesCount});
  }

  render() {
    return (
      <div>
        Likes : <span>{this.state.likesCount}</span>
        <div><button onClick={this.onLike}>Like Me</button></div>
      </div>
    );
  }

}

export default AwesomeComponent;
                                    
