import React from 'react'
//import {render} from 'react-dom'

import {connect} from 'react-redux'

import {changeCount} from './action.js'

class Counter extends React.Component {
    
    constructor(props) {
        super(props);
        this.state = { unused_counter_cnt: 5 }
        //this.onClk = this.onClk.bind(this);
    }

    onClk() {
        
        this.setState({cnt : this.state.cnt +1}); //this.states.cnt + 1});
        //alert("foo");
    }

    changeCnt() {
        //var mm = document.getElementById("myModal");
        //mm.modal("show");
        $('#myModal').modal("show")
        this.props.dispatch(changeCount(2));
    }

    render() {
        // { this.state.cnt }

        var bbb = React.DOM.button({
            className: "btn btn-lg btn-success",
            children: "Register"
        });
        return (
            <div>
                Cnt for {this.props.nnn}: {this.props.inc_cnt} 
                <button className="btn btn-primary" onClick={() => this.changeCnt()}>Click me</button>
                <bbb>foo</bbb>
            </div>
        );
    }


    /*
  constructor(props) {
    super(props);
    this.state = {likesCount : 0};
    this.onLike = this.onLike.bind(this);
  }

  onLike2 () {
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
*/
}

function mapStateToProps(state) {
    return {
        prop_cnt: state.cnt,
        inc_cnt: state.unused_counter_cnt, 
    }
}

//export default Counter;
export default connect(mapStateToProps)(Counter);
