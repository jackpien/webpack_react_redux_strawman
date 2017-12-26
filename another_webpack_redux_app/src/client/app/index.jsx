
import React from 'react';
import {render} from 'react-dom';

// No curly braces necessary since the reducer func is exported as default
// in reducers.js
// NOTE: you need to add "./" so bundler knows where to look for reducers.js
import blahBlahMainReducer from './reducers';

import {createStore} from 'redux';

import {Provider} from 'react-redux';

import AwesomeComponent from './AnotherComponent.jsx';

var store = createStore(blahBlahMainReducer)

class App extends React.Component {
    render () {
	return <div>
            <p> Hello React!</p>
            <AwesomeComponent />
            </div>;
    }
}

// Render a Provider wrapped React component so that the entire App
// component can use the reducer bound to the store created
render(<Provider store={store}><App/></Provider>, document.getElementById('app')); 
                                    
