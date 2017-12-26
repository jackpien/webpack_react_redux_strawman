
import React from 'react';

// The action function we want to dispatch upon user interaction
// NOTE: need to include "./" so bundler knows where to find actions.js
import { incLike } from './actions';

import { connect } from 'react-redux';

class AwesomeComponent extends React.Component {

    constructor(props) {
	super(props);
	this.state = {likesCount : 0};
	// this.onLike = this.onLike.bind(this);
    }
    
    onLike = () => {
	// This dispatches to action function
	this.props.dispatch(incLike(this.props.theLikes));
    }
    
    render = () => {
	return (
		<div>
		Likes (wraps at 3): <span>{this.props.theLikes}</span>
		<div><button onClick={this.onLike}>Like Me</button></div>
		</div>
	);
    }
    
}

// So we can access redux state (defined in reducers.js) via this.props
function mapProps(state) {
    return {
	theLikes: state.likes
    }
}

// Instead of export default AwesomeComponent
export default connect(mapProps)(AwesomeComponent);
                                    
