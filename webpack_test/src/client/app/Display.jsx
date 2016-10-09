import React from 'react'

import {connect} from 'react-redux'

import {displayClick} from './action.js'

class Display extends React.Component {
    Click() {
        this.props.dispatch(displayClick())
    }
    
    render() {
        return <div onClick={() => this.Click()}>{this.props.counter_cnt}</div>
    }
}

function mapStateToProps(state) {
    return {
        counter_cnt: state.cnt,
    }
}

export default connect(mapStateToProps)(Display);
